# Ablation Study

STAT with 7 different LLM backbones on the 40 benchmark queries, plus
90 pipeline-stage queries (planner / skill matching / refined query).

```
queries.json                              40 benchmark queries
pipeline_queries.json                     90 pipeline-stage queries (sets A/B/C)
DATA.md                                   dataset download URL
raw_results/
  benchmark_40q/{model}/{Q01..Q40}/result.json
  pipeline_tests/{model}/set_{A,B,C}.json
evaluations/ablation_eval_merged.json     LLM-judge scores
scripts/
  run_stat_ablation.py                    STAT with chosen LLM on 40 queries
  run_pipeline_test.py                    pipeline-stage tests (no data needed)
```

## Reproduce

```bash
pip install stat-agent
# Download data (see DATA.md) for the 40-query run only.

# 40-query ablation (one model, one query)
python scripts/run_stat_ablation.py --api-key YOUR_KEY \
    --model Grok-4 --query Q05

# Pipeline-stage tests (no data; ~5 min for all 90 queries)
python scripts/run_pipeline_test.py --api-key YOUR_KEY \
    --model Claude-Sonnet-4
```

Supported `--provider`: `poe`, `openai`, `anthropic`, `google`, `xai`,
`deepseek`, `moonshot`, `zhipu`. Omit `--query` / use `--set all` to
run everything.

Outputs → `out/{model}/{Q}/` and `out_pipeline/{model}/set_{A,B,C}.json`.

## Models tested in the paper

Claude-Sonnet-4 (baseline), DeepSeek-V3.2, Grok-4, GPT5.4,
Gemini-3.1-Pro, Grok-3, GPT-4o — all via Poe.

## Results

| Model | 40-q success | Set A | Set B | Set C |
|-------|--------------|-------|-------|-------|
| Claude-Sonnet-4 | 39/40 | 29/30 | 30/30 | 30/30 |
| Grok-4 | 38/40 | 29/30 | 28/30 | 27/30 |
| Grok-3 | 38/40 | 30/30 | 30/30 | 29/30 |
| GPT5.4 | 37/40 | 29/30 | 29/30 | 27/30 |
| DeepSeek-V3.2 | 37/40 | 29/30 | 27/30 | 29/30 |
| Gemini-3.1-Pro | 37/40 | 26/30 | 30/30 | 30/30 |
| GPT-4o | 36/40 | 30/30 | 29/30 | 25/30 |

The pipeline-stage tests use `MockSession` (no real data) and the same
LLM-judge prompt as `../benchmarking/evaluations/evaluation_prompt.md`.
