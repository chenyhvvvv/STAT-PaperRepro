#!/usr/bin/env python3
"""
Run STAT on one or more benchmark queries.

This script reproduces System D (STAT) results in the paper. Run a single query
to verify the pipeline quickly, or omit --query to run the full 40-query suite.

Usage
-----
    # Single query
    python run_stat.py --api-key sk-poe-XXXX --query Q05

    # Full 40-query suite (writes to ./out by default)
    python run_stat.py --api-key sk-poe-XXXX

    # Other Poe-hosted model (ablation-style)
    python run_stat.py --api-key sk-poe-XXXX --model Grok-4 --query Q05

    # Non-Poe provider (e.g. direct Anthropic)
    python run_stat.py \\
        --api-key sk-ant-XXXX --provider anthropic \\
        --model claude-sonnet-4-5 --query Q05

Output (per query)
------------------
    out/{query_id}/result.json    response, tokens, timing, success flag
    out/{query_id}/output.h5ad    agent's modified AnnData (if any)

Dataset
-------
    By default the script looks for data under ./data/ (sibling of this script's
    parent). Use --data-dir to override. See ../DATA.md for the download URL.
"""

from __future__ import annotations

import argparse
import asyncio
import json
import os
import re
import shutil
import sys
import time
from functools import wraps
from pathlib import Path

# ── Paths ───────────────────────────────────────────────────────────────────
SCRIPT_DIR = Path(__file__).resolve().parent
REPO_DIR = SCRIPT_DIR.parent
QUERIES_FILE = REPO_DIR / "queries.json"
DEFAULT_DATA_DIR = REPO_DIR / "data"
DEFAULT_OUT_DIR = REPO_DIR / "out"

QUERY_TIMEOUT = 600  # seconds


# ── Query loading ───────────────────────────────────────────────────────────
def load_queries(query_filter: str | None = None) -> list[dict]:
    with open(QUERIES_FILE) as f:
        queries = json.load(f)
    if query_filter:
        ids = {qid.strip() for qid in query_filter.split(",")}
        queries = [q for q in queries if q["id"] in ids]
        if not queries:
            raise SystemExit(f"No queries matched --query {query_filter!r}")
    return queries


def resolve_input(q: dict, data_dir: Path):
    """Return (all_inputs, primary_path). Both None for no-data queries."""
    inp = q.get("input")
    if inp is None:
        return None, None
    if isinstance(inp, list):
        paths = [str(data_dir / p) for p in inp]
        return paths, paths[0]
    p = str(data_dir / inp)
    return p, p


# ── Scripted clarification matcher ──────────────────────────────────────────
def match_scripted(question: str, scripted: dict[str, str]) -> str:
    """Collect every scripted answer whose keyword appears in the question.

    STAT may bundle multiple clarification questions into one turn; we join all
    matching scripted answers with ". " so each sub-question gets covered.
    """
    q = question.lower()
    matched, seen = [], set()
    for kw, resp in scripted.items():
        if kw.lower() in q and resp not in seen:
            matched.append(resp)
            seen.add(resp)
    if matched:
        return ". ".join(matched)
    return next(iter(scripted.values()), "yes") if scripted else "yes"


# ── STAT runner ─────────────────────────────────────────────────────────────
def run_stat(q: dict, out_dir: Path, *, model: str, provider: str,
             api_key: str, base_url: str | None) -> dict:
    """Run STAT on a single query and write outputs to ``out_dir``."""
    out_dir.mkdir(parents=True, exist_ok=True)

    # Token tracking — monkey-patch openai.OpenAI to count tokens across all
    # internal LLM calls. STAT issues many short calls via the OpenAI-compatible
    # client, so we attach the counter once at construction time.
    import openai

    calls = pt = ct = 0

    _orig_init = openai.OpenAI.__init__

    @wraps(_orig_init)
    def _tracked_init(self, *a, **kw):
        _orig_init(self, *a, **kw)
        _orig_create = self.chat.completions.create

        @wraps(_orig_create)
        def _tracked(*ca, **ckw):
            nonlocal calls, pt, ct
            resp = _orig_create(*ca, **ckw)
            if hasattr(resp, "usage") and resp.usage:
                calls += 1
                pt += getattr(resp.usage, "prompt_tokens", 0) or 0
                ct += getattr(resp.usage, "completion_tokens", 0) or 0
            return resp

        self.chat.completions.create = _tracked

    openai.OpenAI.__init__ = _tracked_init

    from stat_agent.agent.spatial_agent_core import SpatialAgent
    from stat_agent.core.session import SimpleSession

    all_inputs, primary = resolve_input(q, args_data_dir)

    # ── No-data queries: bypass session, call LLM directly ──
    if primary is None:
        openai.OpenAI.__init__ = _orig_init
        from openai import OpenAI as OAI
        client_kwargs = {"api_key": api_key}
        if base_url:
            client_kwargs["base_url"] = base_url
        client = OAI(**client_kwargs)
        start = time.time()
        resp = client.chat.completions.create(
            model=model, max_tokens=4096,
            messages=[{"role": "user", "content": q["query"]}],
        )
        return {
            "query_id": q["id"], "system": "stat", "model": model,
            "response": resp.choices[0].message.content,
            "output_h5ad": None, "success": True,
            "prompt_tokens": resp.usage.prompt_tokens,
            "completion_tokens": resp.usage.completion_tokens,
            "total_tokens": resp.usage.total_tokens,
            "llm_calls": 1, "wall_s": round(time.time() - start, 1),
        }

    # ── Stage dataset for the agent ──
    ds_dir = out_dir / "dataset"
    if ds_dir.exists():
        shutil.rmtree(ds_dir)
    ds_dir.mkdir(parents=True)
    inputs_list = all_inputs if isinstance(all_inputs, list) else [all_inputs]
    for p in inputs_list:
        shutil.copy2(p, ds_dir / Path(p).name)

    # Reference file goes next to ds_dir so load_dataset doesn't try to load it
    # as a slice (references typically lack x/y columns).
    ref_path = None
    if q.get("reference"):
        ref_src = args_data_dir / q["reference"]
        ref_path = out_dir / Path(ref_src).name
        shutil.copy2(ref_src, ref_path)

    scripted = q.get("scripted_responses", {})

    async def _run():
        session = SimpleSession(name="bench")
        session.load_dataset(str(ds_dir))
        # Skills (e.g. LLM-assisted annotation) read llm_config off the session.
        session.llm_config = {
            "api_key": api_key,
            "model": model.split("/", 1)[-1],
            "base_url": base_url,
        }

        # SpatialAgent accepts a model with a provider prefix (e.g. "poe/...")
        # or a bare ID with provider= specified.
        agent = SpatialAgent(
            model=model, api_key=api_key,
            session=session, enable_planning=True, enable_skills=True,
        )

        all_events = []
        current_msg = q["query"]
        if ref_path:
            # Replace the user-stated relative reference path with the
            # absolute path the agent can actually read.
            ref_name = Path(ref_path).name
            current_msg = re.sub(
                r"['\"]?\./?" + re.escape(ref_name) + r"['\"]?",
                f"'{ref_path}'",
                current_msg,
            )
            if str(ref_path) not in current_msg:
                current_msg += f"\n\nReference file is at: {ref_path}"

        # Up to 5 clarification turns
        for _ in range(5):
            got_clarification = False
            async for ev in agent.chat_with_events(current_msg, execute_code=True):
                all_events.append(ev)
                if ev["type"] in ("clarification_needed", "prerequisites_needed"):
                    question = str(ev.get("question", ev.get("questions", "")))
                    current_msg = match_scripted(question, scripted)
                    got_clarification = True
                    break
                if ev["type"] == "skill_selection":
                    options = ev.get("skills", ev.get("options", []))
                    has_ref = bool(q.get("reference"))
                    task = q.get("task", "")
                    pick = "1"
                    if options:
                        for i, opt in enumerate(options):
                            name = str(
                                opt.get("name", opt) if isinstance(opt, dict)
                                else opt
                            ).lower()
                            if task == "T2" and (
                                "domain" in name or "spagcn" in name
                                or "cluster" in name or "statist" in name
                            ):
                                pick = str(i + 1)
                                break
                            if not has_ref and (
                                "marker" in name or "cluster" in name
                                or "auto" in name
                            ):
                                pick = str(i + 1)
                                break
                    current_msg = pick
                    got_clarification = True
                    break
            if not got_clarification:
                break

        # Aggregate response text from event stream
        step_responses, exec_lines = [], []
        for ev in all_events:
            t = ev["type"]
            if t == "step_execution_complete" and ev.get("response"):
                step_responses.append(ev["response"])
            elif t == "pipeline_complete" and ev.get("all_responses"):
                step_responses.extend(ev["all_responses"])
            elif t == "advice" and ev.get("message"):
                step_responses.append(ev["message"])
            elif t == "execution_output" and ev.get("line"):
                exec_lines.append(ev["line"])
            elif t == "agent_text" and ev.get("text"):
                exec_lines.append(ev["text"])
        full_response = (
            "\n\n".join(step_responses) if step_responses else "\n".join(exec_lines)
        )

        # Save output h5ad
        output_path = out_dir / "output.h5ad"
        if len(session.slices) > 1:
            import anndata as _ad
            adatas = [sl.adata for sl in session.slices.values()]
            combined = _ad.concat(
                adatas, join="outer", label="slice_id",
                keys=[str(sid) for sid in session.slices.keys()],
            )
            combined.write(str(output_path))
        else:
            for _, sl in session.slices.items():
                sl.adata.write(str(output_path))
                break
        return full_response

    start = time.time()
    try:
        response = asyncio.run(_run())
        success = bool(response) or (out_dir / "output.h5ad").exists()
    except Exception as e:
        response, success = f"ERROR: {e!s}"[:5000], False
    finally:
        openai.OpenAI.__init__ = _orig_init

    return {
        "query_id": q["id"], "system": "stat", "model": model,
        "response": response,
        "output_h5ad": (
            str(out_dir / "output.h5ad") if (out_dir / "output.h5ad").exists()
            else None
        ),
        "success": success,
        "prompt_tokens": pt, "completion_tokens": ct, "total_tokens": pt + ct,
        "llm_calls": calls, "wall_s": round(time.time() - start, 1),
    }


# ── Main ────────────────────────────────────────────────────────────────────
def parse_args():
    p = argparse.ArgumentParser(
        description="Run STAT on benchmark queries",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    p.add_argument("--api-key", required=True,
                   help="LLM provider API key")
    p.add_argument("--query", default=None,
                   help="Query ID(s) to run, comma-separated (e.g. Q05 or Q05,Q06). "
                        "If omitted, all 40 queries run.")
    p.add_argument("--model", default="Claude-Sonnet-4",
                   help="Model name (default: Claude-Sonnet-4 via Poe). "
                        "Use a provider-prefixed name like 'anthropic/claude-sonnet-4-5' "
                        "for non-Poe providers, or pass --provider explicitly.")
    p.add_argument("--provider", default="poe",
                   choices=["poe", "openai", "anthropic", "google",
                            "xai", "deepseek", "moonshot", "zhipu"],
                   help="LLM provider (default: poe). "
                        "Determines base URL and API conventions.")
    p.add_argument("--base-url", default=None,
                   help="Override the provider's default base URL "
                        "(rare; only needed for custom endpoints).")
    p.add_argument("--data-dir", default=str(DEFAULT_DATA_DIR),
                   help=f"Path to dataset root (default: {DEFAULT_DATA_DIR}). "
                        "See ../DATA.md for the download URL.")
    p.add_argument("--out-dir", default=str(DEFAULT_OUT_DIR),
                   help=f"Where to write results (default: {DEFAULT_OUT_DIR})")
    return p.parse_args()


def main():
    args = parse_args()
    # ``run_stat`` consults this module-level path for input resolution
    global args_data_dir
    args_data_dir = Path(args.data_dir).resolve()
    out_root = Path(args.out_dir).resolve()
    out_root.mkdir(parents=True, exist_ok=True)

    if not args_data_dir.exists():
        sys.exit(
            f"\nERROR: data directory not found: {args_data_dir}\n"
            f"See {REPO_DIR}/DATA.md for the download URL.\n"
        )

    # Prefix model with provider unless the user has already done so.
    model = args.model
    if "/" not in model:
        model = f"{args.provider}/{model}"

    # If --base-url not provided, leave None — SpatialAgent will look it up.
    base_url = args.base_url
    if args.provider == "poe" and base_url is None:
        base_url = "https://api.poe.com/v1"

    queries = load_queries(args.query)
    print(f"Loaded {len(queries)} queries. Model: {model}. Data: {args_data_dir}")

    summary = []
    for q in queries:
        qid = q["id"]
        out_dir = out_root / qid
        print(f"\n=== {qid}: {q['query'][:80]}{'...' if len(q['query']) > 80 else ''} ===")
        result = run_stat(
            q, out_dir,
            model=model, provider=args.provider,
            api_key=args.api_key, base_url=base_url,
        )
        with open(out_dir / "result.json", "w") as f:
            json.dump(result, f, indent=2, default=str)
        status = "OK " if result["success"] else "FAIL"
        print(f"  [{status}] {result['wall_s']}s  "
              f"tokens={result['total_tokens']}  llm_calls={result['llm_calls']}")
        summary.append({
            "id": qid, "success": result["success"],
            "wall_s": result["wall_s"], "tokens": result["total_tokens"],
        })

    with open(out_root / "summary.json", "w") as f:
        json.dump(summary, f, indent=2)
    n_ok = sum(1 for s in summary if s["success"])
    print(f"\nDone. {n_ok}/{len(summary)} succeeded. Summary at {out_root}/summary.json")


if __name__ == "__main__":
    args_data_dir = DEFAULT_DATA_DIR  # set by main(); module-level so run_stat sees it
    main()
