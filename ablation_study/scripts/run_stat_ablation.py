#!/usr/bin/env python3
"""
Run STAT with a chosen LLM backbone on the 40-query benchmark.

This is the ablation runner: it sweeps the same 40 queries used in the main
benchmark, but lets you pick which LLM powers STAT. The default provider is
Poe (which exposes Claude, Grok, GPT, Gemini, and DeepSeek under one
OpenAI-compatible endpoint), matching the paper's setup.

Usage
-----
    # Single query, single model (~1–5 min)
    python run_stat_ablation.py --api-key sk-poe-XXXX \\
        --model Grok-4 --query Q05

    # All 40 queries on one model (~6–10 h)
    python run_stat_ablation.py --api-key sk-poe-XXXX --model Grok-4

    # Multiple queries
    python run_stat_ablation.py --api-key sk-poe-XXXX \\
        --model Gemini-3.1-Pro --query Q05,Q06,Q07

    # Non-Poe provider (direct vendor API)
    python run_stat_ablation.py --api-key sk-ant-XXXX \\
        --provider anthropic --model claude-sonnet-4-5 --query Q05

Models tested in the paper (via Poe)
------------------------------------
    Claude-Sonnet-4   (baseline)
    DeepSeek-V3.2
    Grok-4
    GPT5.4
    Gemini-3.1-Pro
    Grok-3
    GPT-4o

Output (per query)
------------------
    out/{model}/{query_id}/result.json
    out/{model}/{query_id}/output.h5ad
    out/{model}/summary.json
"""

from __future__ import annotations

import argparse
import asyncio
import json
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


def load_queries(query_filter: str | None) -> list[dict]:
    with open(QUERIES_FILE) as f:
        queries = json.load(f)
    if query_filter:
        ids = {qid.strip() for qid in query_filter.split(",")}
        queries = [q for q in queries if q["id"] in ids]
        if not queries:
            raise SystemExit(f"No queries matched --query {query_filter!r}")
    return queries


def resolve_input(q: dict, data_dir: Path):
    inp = q.get("input")
    if inp is None:
        return None, None
    if isinstance(inp, list):
        paths = [str(data_dir / p) for p in inp]
        return paths, paths[0]
    p = str(data_dir / inp)
    return p, p


def match_scripted(question: str, scripted: dict[str, str]) -> str:
    q = question.lower()
    matched, seen = [], set()
    for kw, resp in scripted.items():
        if kw.lower() in q and resp not in seen:
            matched.append(resp)
            seen.add(resp)
    if matched:
        return ". ".join(matched)
    return next(iter(scripted.values()), "yes") if scripted else "yes"


def run_stat(q: dict, out_dir: Path, *, model: str, api_key: str,
             base_url: str | None, data_dir: Path) -> dict:
    out_dir.mkdir(parents=True, exist_ok=True)

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

    all_inputs, primary = resolve_input(q, data_dir)

    if primary is None:
        openai.OpenAI.__init__ = _orig_init
        from openai import OpenAI as OAI
        client_kwargs = {"api_key": api_key}
        if base_url:
            client_kwargs["base_url"] = base_url
        client = OAI(**client_kwargs)
        start = time.time()
        # Strip provider prefix for direct LLM call
        raw_model = model.split("/", 1)[-1]
        resp = client.chat.completions.create(
            model=raw_model, max_tokens=4096,
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

    ds_dir = out_dir / "dataset"
    if ds_dir.exists():
        shutil.rmtree(ds_dir)
    ds_dir.mkdir(parents=True)
    inputs_list = all_inputs if isinstance(all_inputs, list) else [all_inputs]
    for p in inputs_list:
        shutil.copy2(p, ds_dir / Path(p).name)

    ref_path = None
    if q.get("reference"):
        ref_src = data_dir / q["reference"]
        ref_path = out_dir / Path(ref_src).name
        shutil.copy2(ref_src, ref_path)

    scripted = q.get("scripted_responses", {})

    async def _run():
        session = SimpleSession(name="bench")
        session.load_dataset(str(ds_dir))
        session.llm_config = {
            "api_key": api_key,
            "model": model.split("/", 1)[-1],
            "base_url": base_url,
        }

        agent = SpatialAgent(
            model=model, api_key=api_key,
            session=session, enable_planning=True, enable_skills=True,
        )

        all_events = []
        current_msg = q["query"]
        if ref_path:
            ref_name = Path(ref_path).name
            current_msg = re.sub(
                r"['\"]?\./?" + re.escape(ref_name) + r"['\"]?",
                f"'{ref_path}'", current_msg,
            )
            if str(ref_path) not in current_msg:
                current_msg += f"\n\nReference file is at: {ref_path}"

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


def parse_args():
    p = argparse.ArgumentParser(
        description="STAT ablation runner (LLM backbone sweep)",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    p.add_argument("--api-key", required=True,
                   help="LLM provider API key")
    p.add_argument("--model", required=True,
                   help="Model name (e.g. Claude-Sonnet-4, Grok-4, GPT5.4). "
                        "Pass a bare name + --provider, or a provider-prefixed name "
                        "like 'anthropic/claude-sonnet-4-5'.")
    p.add_argument("--provider", default="poe",
                   choices=["poe", "openai", "anthropic", "google",
                            "xai", "deepseek", "moonshot", "zhipu"],
                   help="LLM provider (default: poe)")
    p.add_argument("--base-url", default=None,
                   help="Override the provider's default base URL")
    p.add_argument("--query", default=None,
                   help="Query ID(s), comma-separated. Omit to run all 40.")
    p.add_argument("--data-dir", default=str(DEFAULT_DATA_DIR),
                   help=f"Dataset root (default: {DEFAULT_DATA_DIR})")
    p.add_argument("--out-dir", default=str(DEFAULT_OUT_DIR),
                   help=f"Where to write results (default: {DEFAULT_OUT_DIR})")
    return p.parse_args()


def main():
    args = parse_args()
    data_dir = Path(args.data_dir).resolve()
    if not data_dir.exists():
        sys.exit(
            f"\nERROR: data directory not found: {data_dir}\n"
            f"See {REPO_DIR}/DATA.md for the download URL.\n"
        )

    model = args.model
    if "/" not in model:
        model = f"{args.provider}/{model}"

    base_url = args.base_url
    if args.provider == "poe" and base_url is None:
        base_url = "https://api.poe.com/v1"

    # Use the bare model name (without provider prefix) for the output folder
    model_dir = Path(args.out_dir).resolve() / model.split("/", 1)[-1]
    model_dir.mkdir(parents=True, exist_ok=True)

    queries = load_queries(args.query)
    print(f"Loaded {len(queries)} queries. Model: {model}. Data: {data_dir}")
    print(f"Writing to: {model_dir}")

    summary = []
    for q in queries:
        qid = q["id"]
        out_dir = model_dir / qid
        print(f"\n=== {qid}: {q['query'][:80]}{'...' if len(q['query']) > 80 else ''} ===")
        result = run_stat(
            q, out_dir,
            model=model, api_key=args.api_key,
            base_url=base_url, data_dir=data_dir,
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

    with open(model_dir / "summary.json", "w") as f:
        json.dump(summary, f, indent=2)
    n_ok = sum(1 for s in summary if s["success"])
    print(f"\nDone. {n_ok}/{len(summary)} succeeded. "
          f"Summary at {model_dir}/summary.json")


if __name__ == "__main__":
    main()
