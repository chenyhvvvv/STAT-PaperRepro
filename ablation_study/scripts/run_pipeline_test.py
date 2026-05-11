#!/usr/bin/env python3
"""
Pipeline-stage accuracy benchmark for STAT.

Tests three STAT pipeline stages independently against expected outputs:

  Set A — QueryPlanner    target slices, step decomposition, clarification
  Set B — SkillFilter +   correct skill selection from the registry
          SemanticMatcher
  Set C — Full pipeline   refined query quality (S1→S4, no code execution),
                          judged by an LLM-as-judge

Queries and ground-truth come from ``../pipeline_queries.json``. No real
dataset is loaded — mock sessions describe the data shape so the test is
fast and deterministic.

Usage
-----
    # One model, all 3 sets (~5 min)
    python run_pipeline_test.py --api-key sk-poe-XXXX --model Claude-Sonnet-4

    # A single set
    python run_pipeline_test.py --api-key sk-poe-XXXX \\
        --model Grok-4 --set B

    # Subset of queries
    python run_pipeline_test.py --api-key sk-poe-XXXX \\
        --model GPT-4o --set A --queries PA01,PA17

Output
------
    out/{model}/set_A.json
    out/{model}/set_B.json
    out/{model}/set_C.json

Each output file is a list of per-query records with full inputs, the
pipeline's actual behavior, and the success verdict.
"""

from __future__ import annotations

import argparse
import asyncio
import json
import logging
import re
import sys
import time
from pathlib import Path

# ── Paths ───────────────────────────────────────────────────────────────────
SCRIPT_DIR = Path(__file__).resolve().parent
REPO_DIR = SCRIPT_DIR.parent
QUERIES_FILE = REPO_DIR / "pipeline_queries.json"
DEFAULT_OUT_DIR = REPO_DIR / "out_pipeline"

# Add scripts dir to path so we can import pipeline_test_sessions
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

logger = logging.getLogger("pipeline_test")


# ── Config helpers ──────────────────────────────────────────────────────────
def get_skills_root() -> Path:
    """Locate the SKILLS directory inside the installed stat_agent package."""
    import stat_agent
    return Path(stat_agent.__file__).resolve().parent / "skills"


def load_test_data(query_filter: str | None, test_set: str):
    with open(QUERIES_FILE) as f:
        data = json.load(f)
    sets: dict[str, list[dict]] = {}
    for set_name in ["set_A", "set_B", "set_C"]:
        key = set_name[-1]
        if test_set != "all" and test_set.upper() != key:
            continue
        queries = data[set_name]
        if query_filter:
            ids = {q.strip() for q in query_filter.split(",")}
            queries = [q for q in queries if q["id"] in ids]
        sets[key] = queries
    return data["sessions"], sets


def init_llm_backend(model: str, api_key: str, base_url: str | None):
    from stat_agent.agent.llm_backend import LLMBackend
    return LLMBackend(
        system_prompt="You are a spatial transcriptomics analysis expert.",
        model=model, api_key=api_key, endpoint=base_url,
    )


def init_skill_registry():
    from stat_agent.agent.skill_registry import SkillRegistry
    registry = SkillRegistry(get_skills_root(), progressive_disclosure=True)
    registry.load()
    return registry


def build_mock_session(session_def: dict):
    from pipeline_test_sessions import MockSession, MockSlice
    slices = {}
    for sl in session_def["slices"]:
        slices[sl["slice_id"]] = MockSlice(
            slice_id=sl["slice_id"],
            modality=sl["modality"],
            data_level=sl["data_level"],
            n_obs=sl.get("n_obs", 5000),
            n_vars=sl.get("n_vars", 500),
            _has_celltype=sl.get("has_celltype", False),
            celltypes=sl.get("celltypes", []),
            tissue_name=sl.get("tissue_name", f"slice_{sl['slice_id']}"),
            image_names=sl.get("image_names", []),
            columns=sl.get("columns", []),
        )
    return MockSession(name="pipeline_test", slices=slices)


# ── Set A: Planner ──────────────────────────────────────────────────────────
async def run_set_A(queries, sessions_def, llm):
    from stat_agent.agent.query_planner import QueryPlanner
    planner = QueryPlanner(llm)
    results = []
    for q in queries:
        qid = q["id"]
        session = build_mock_session(sessions_def[q["session"]])
        print(f"  {qid}: {q['query'][:60]}...", end=" ", flush=True)
        start = time.time()
        try:
            plan = await planner.plan(
                user_query=q["query"], session_summary=session.get_summary(),
                previous_clarifications=[], conversation_history="",
            )
            actual_clarify = plan.needs_clarification
            actual_steps = len(plan.steps) if not actual_clarify else None
            actual_slices = (
                [step.target_slice_ids for step in plan.steps]
                if not actual_clarify else None
            )

            expected_clarify = q["expected_needs_clarification"]
            clarify_ok = actual_clarify == expected_clarify

            if expected_clarify:
                steps_ok = slices_ok = True
            elif q.get("alt_expected"):
                match_any = False
                for alt in q["alt_expected"]:
                    if actual_steps == alt["num_steps"]:
                        na = [sorted(s) for s in actual_slices] if actual_slices else []
                        ne = [sorted(s) for s in alt["target_slice_ids"]] if alt["target_slice_ids"] else []
                        if na == ne:
                            match_any = True
                            break
                steps_ok = slices_ok = match_any
            else:
                steps_ok = actual_steps == q["expected_num_steps"]
                exp_sl = q["expected_target_slice_ids"]
                if actual_slices is not None and exp_sl is not None:
                    slices_ok = [sorted(s) for s in actual_slices] == [sorted(s) for s in exp_sl]
                else:
                    slices_ok = actual_slices == exp_sl
            success = clarify_ok and steps_ok and slices_ok
            elapsed = round(time.time() - start, 1)
            print(f"{'+' if success else 'x'} ({elapsed}s)")
            results.append({
                "query_id": qid, "set": "A",
                "query_text": q["query"], "session": q["session"],
                "category": q["category"], "edge_case": q["edge_case"],
                "actual": {
                    "needs_clarification": actual_clarify,
                    "num_steps": actual_steps,
                    "target_slice_ids": actual_slices,
                    "clarification_question": plan.clarification_question if actual_clarify else None,
                    "refined_queries": [s.refined_query for s in plan.steps] if not actual_clarify else None,
                },
                "expected": {
                    "needs_clarification": expected_clarify,
                    "num_steps": q.get("expected_num_steps"),
                    "target_slice_ids": q.get("expected_target_slice_ids"),
                },
                "evaluation": {
                    "clarification_correct": clarify_ok,
                    "num_steps_correct": steps_ok,
                    "target_slices_correct": slices_ok,
                    "success": success,
                },
                "wall_s": elapsed,
            })
        except Exception as e:
            elapsed = round(time.time() - start, 1)
            print(f"ERR ({elapsed}s): {str(e)[:100]}")
            results.append({
                "query_id": qid, "set": "A",
                "query_text": q["query"], "session": q["session"],
                "category": q["category"], "edge_case": q["edge_case"],
                "actual": {"error": str(e)[:2000]},
                "evaluation": {"success": False, "error": True},
                "wall_s": elapsed,
            })
    return results


# ── Set B: Skill matching ───────────────────────────────────────────────────
async def _semantic_match(llm, query: str, available_skills: dict, top_k: int = 5):
    if not available_skills:
        return []
    skills_list = [
        f"- **{slug}**: {skill.description}"
        for slug, skill in sorted(available_skills.items(), key=lambda x: x[1].name.lower())
    ]
    matching_prompt = (
        "You are a strict skill matching system. Match skills ONLY when the user's "
        "request SPECIFICALLY asks for what the skill provides.\n\n"
        f"User Request: \"{query}\"\n\n"
        f"Available Skills:\n" + "\n".join(skills_list) + "\n\n"
        "MATCHING CRITERIA:\n"
        "- Match: User's request DIRECTLY asks for the skill's specific task/output\n"
        "- Don't match: Request is only loosely related or shares general themes\n"
        "- Don't match: User can accomplish their goal WITHOUT this skill\n"
        "- Be conservative: When in doubt, return empty array\n\n"
        "Your task:\n"
        "1. Identify the SPECIFIC task the user is asking for\n"
        "2. Match ONLY if a skill provides EXACTLY that task\n"
        f"3. Return at most {top_k} skill slugs, or fewer if not specifically relevant\n"
        "4. Respond with ONLY a JSON array: [\"skill-slug\"] or []\n\n"
        "CRITICAL: Return [] (empty array) unless the skill is SPECIFICALLY needed "
        "for the user's request.\n\nResponse (JSON array only):"
    )
    response = await llm.run(matching_prompt)
    m = re.search(r"\[.*?\]", response, re.DOTALL)
    if m:
        matched = json.loads(m.group(0))
        return [s for s in matched if s in available_skills]
    return []


async def run_set_B(queries, sessions_def, llm):
    from stat_agent.agent.skill_filter import SkillFilter
    registry = init_skill_registry()
    skill_filter = SkillFilter()
    disabled = {slug for slug, m in registry.skill_metadata.items() if not m.default_skill}
    results = []
    for q in queries:
        qid = q["id"]
        session = build_mock_session(sessions_def[q["session"]])
        print(f"  {qid}: {q['query'][:60]}...", end=" ", flush=True)
        start = time.time()
        try:
            all_skills = {
                k: v for k, v in registry.skill_metadata.items() if k not in disabled
            }
            compatible = skill_filter.filter_skills(q["target_slice_ids"], session, all_skills)
            compat_d = {s.slug: s for s in compatible}
            matched = await _semantic_match(llm, q["query"], compat_d)
            elapsed = round(time.time() - start, 1)

            if q["expected_no_skill"]:
                success = len(matched) == 0
            else:
                success = len(matched) > 0 and matched[0] in q["expected_skill_slugs"]
            print(f"{'+' if success else 'x'} matched={matched} ({elapsed}s)")
            results.append({
                "query_id": qid, "set": "B",
                "query_text": q["query"], "session": q["session"],
                "category": q["category"], "task_type": q["task_type"],
                "actual": {
                    "matched_slugs": matched,
                    "compatible_skills": list(compat_d.keys()),
                    "n_compatible": len(compat_d),
                },
                "expected": {
                    "skill_slugs": q["expected_skill_slugs"],
                    "no_skill": q["expected_no_skill"],
                },
                "evaluation": {"success": success},
                "wall_s": elapsed,
            })
        except Exception as e:
            elapsed = round(time.time() - start, 1)
            print(f"ERR ({elapsed}s): {str(e)[:100]}")
            results.append({
                "query_id": qid, "set": "B",
                "query_text": q["query"], "session": q["session"],
                "category": q["category"], "task_type": q["task_type"],
                "actual": {"error": str(e)[:2000]},
                "expected": {
                    "skill_slugs": q["expected_skill_slugs"],
                    "no_skill": q["expected_no_skill"],
                },
                "evaluation": {"success": False, "error": True},
                "wall_s": elapsed,
            })
    return results


# ── Set C: Full pipeline refined-query test ─────────────────────────────────
async def run_set_C(queries, sessions_def, llm):
    from stat_agent.agent.query_planner import QueryPlanner
    from stat_agent.agent.skill_filter import SkillFilter
    from stat_agent.agent.skill_verifier import SkillVerifier
    from stat_agent.agent.pipeline_executor import PipelineExecutor

    registry = init_skill_registry()
    planner = QueryPlanner(llm)
    skill_filter = SkillFilter()
    verifier = SkillVerifier(llm)

    async def matcher(request, available_skills, top_k=5):
        return await _semantic_match(llm, request, available_skills, top_k)

    results = []
    for q in queries:
        qid = q["id"]
        session = build_mock_session(sessions_def[q["session"]])
        executor = PipelineExecutor(
            query_planner=planner, skill_filter=skill_filter,
            skill_verifier=verifier, skill_registry=registry,
            semantic_matcher=matcher, session=session,
        )
        print(f"  {qid}: {q['query'][:60]}...", end=" ", flush=True)
        start = time.time()
        try:
            pr = await executor.execute_pipeline(
                user_query=q["query"], session_summary=session.get_summary(),
            )
            elapsed = round(time.time() - start, 1)
            results.append({
                "query_id": qid, "set": "C",
                "query_text": q["query"], "session": q["session"],
                "category": q["category"],
                "expected_behavior": q["expected_behavior"],
                "actual": {
                    "result_type": pr.type,
                    "final_query": pr.final_query or "",
                    "selected_skill": pr.selected_skill.slug if pr.selected_skill else None,
                    "skill_options": getattr(pr, "skill_options", []),
                    "clarification_question": pr.clarification_question,
                    "verifier_questions": getattr(pr, "verifier_questions", []),
                    "advice_message": pr.advice_message or "",
                    "plan_steps": len(pr.plan_steps) if pr.plan_steps else 0,
                },
                "evaluation": {"success": None},  # filled by judge later
                "wall_s": elapsed,
            })
            print(f"type={pr.type} ({elapsed}s)")
        except Exception as e:
            elapsed = round(time.time() - start, 1)
            print(f"ERR ({elapsed}s): {str(e)[:100]}")
            results.append({
                "query_id": qid, "set": "C",
                "query_text": q["query"], "session": q["session"],
                "category": q["category"],
                "expected_behavior": q["expected_behavior"],
                "actual": {"error": str(e)[:2000]},
                "evaluation": {"success": False, "error": True},
                "wall_s": elapsed,
            })
    return results


async def judge_set_C(results, llm):
    for r in results:
        if r["evaluation"].get("error") or r["evaluation"]["success"] is not None:
            continue
        actual = r["actual"]
        prompt = (
            f"You are evaluating the output of a spatial transcriptomics analysis pipeline.\n\n"
            f"Original user query: \"{r['query_text']}\"\n"
            f"Expected behavior: {r['expected_behavior']}\n\n"
            f"Pipeline output:\n"
            f"- Result type: {actual['result_type']}\n"
            f"  (success = ready to execute, advice = prerequisite missing,\n"
            f"   skill_selection = multiple skills found, verifier_clarification = needs info,\n"
            f"   planner_clarification = ambiguous, no_skill = out of scope)\n"
            f"- Selected skill: {actual.get('selected_skill', 'None')}\n"
            f"- Skill options: {actual.get('skill_options', [])}\n"
            f"- Final refined query: \"{actual.get('final_query', '')}\"\n"
            f"- Verifier questions: {actual.get('verifier_questions', [])}\n"
            f"- Clarification question: {actual.get('clarification_question', 'None')}\n"
            f"- Advice message: \"{actual.get('advice_message', '')}\"\n\n"
            "Evaluate whether the pipeline output matches the expected behavior. Consider:\n"
            "1. Is the result type appropriate? \"skill_selection\" counts as success if the\n"
            "   correct task type was identified. \"planner_clarification\" counts as success\n"
            "   if the expected behavior says the query should ask for clarification.\n"
            "2. If the refined query exists, does it preserve all user-specified parameters?\n"
            "3. Does the output avoid hallucinating information not in the original query?\n"
            "4. Is the overall routing correct?\n\n"
            "Respond with ONLY \"SUCCESS\" or \"FAIL\" followed by a brief reason.\n\n"
            "Your verdict:"
        )
        try:
            verdict = (await llm.run(prompt)).strip()
            r["evaluation"]["success"] = verdict.upper().startswith("SUCCESS")
            r["evaluation"]["judge_verdict"] = verdict
        except Exception as e:
            r["evaluation"]["success"] = False
            r["evaluation"]["judge_verdict"] = f"Judge error: {e}"
        print(f"  {r['query_id']}: {'PASS' if r['evaluation']['success'] else 'FAIL'}")


def save_results(results, out_dir: Path, set_name: str, model_name: str):
    model_dir = out_dir / model_name.replace(" ", "_").replace("/", "_")
    model_dir.mkdir(parents=True, exist_ok=True)
    fname = model_dir / f"set_{set_name}.json"
    # Merge with existing run if present
    if fname.exists():
        with open(fname) as f:
            existing = json.load(f)
        em = {r["query_id"]: r for r in existing}
        for r in results:
            em[r["query_id"]] = r
        merged = sorted(em.values(), key=lambda x: x["query_id"])
    else:
        merged = results
    with open(fname, "w") as f:
        json.dump(merged, f, indent=2, default=str)
    total = len(merged)
    passed = sum(1 for r in merged if r["evaluation"].get("success"))
    print(f"\n  Set {set_name} | {model_name}: {passed}/{total} ({100*passed/total:.0f}%)")
    return passed, total


def parse_args():
    p = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--api-key", required=True, help="LLM provider API key")
    p.add_argument("--model", required=True,
                   help="Model name (e.g. Claude-Sonnet-4, Grok-4). "
                        "Pass --provider to specify the backend.")
    p.add_argument("--provider", default="poe",
                   choices=["poe", "openai", "anthropic", "google",
                            "xai", "deepseek", "moonshot", "zhipu"],
                   help="LLM provider (default: poe)")
    p.add_argument("--base-url", default=None,
                   help="Override the provider's default base URL")
    p.add_argument("--set", default="all", choices=["A", "B", "C", "all"],
                   help="Which set to run (default: all)")
    p.add_argument("--queries", default=None,
                   help="Comma-separated query IDs (e.g. PA01,PA17). "
                        "Omit to run the full set.")
    p.add_argument("--judge-model", default=None,
                   help="Model for Set C judging (default: same as --model)")
    p.add_argument("--out-dir", default=str(DEFAULT_OUT_DIR),
                   help=f"Output directory (default: {DEFAULT_OUT_DIR})")
    return p.parse_args()


def main():
    args = parse_args()
    logging.basicConfig(level=logging.WARNING)

    model = args.model if "/" in args.model else f"{args.provider}/{args.model}"
    base_url = args.base_url
    if args.provider == "poe" and base_url is None:
        base_url = "https://api.poe.com/v1"

    out_dir = Path(args.out_dir).resolve()
    out_dir.mkdir(parents=True, exist_ok=True)

    sessions_def, query_sets = load_test_data(args.queries, args.set)
    print("=" * 70)
    print(f"STAT Pipeline Test | Model: {model}")
    print(f"Sets: {list(query_sets.keys())} | "
          f"Queries: {sum(len(v) for v in query_sets.values())}")
    print("=" * 70)

    llm = init_llm_backend(model, args.api_key, base_url)

    async def _run():
        if "A" in query_sets:
            print(f"\n--- Set A: Planner ({len(query_sets['A'])} queries) ---")
            results = await run_set_A(query_sets["A"], sessions_def, llm)
            save_results(results, out_dir, "A", args.model)
        if "B" in query_sets:
            print(f"\n--- Set B: Skill Matching ({len(query_sets['B'])} queries) ---")
            results = await run_set_B(query_sets["B"], sessions_def, llm)
            save_results(results, out_dir, "B", args.model)
        if "C" in query_sets:
            print(f"\n--- Set C: Refined Query ({len(query_sets['C'])} queries) ---")
            results = await run_set_C(query_sets["C"], sessions_def, llm)
            judge_name = args.judge_model or args.model
            judge_model_full = (
                judge_name if "/" in judge_name else f"{args.provider}/{judge_name}"
            )
            print(f"\n  Judging Set C with {judge_model_full}...")
            judge_llm = init_llm_backend(judge_model_full, args.api_key, base_url)
            await judge_set_C(results, judge_llm)
            save_results(results, out_dir, "C", args.model)

    asyncio.run(_run())
    print("\n" + "=" * 70 + "\nDone.")


if __name__ == "__main__":
    main()
