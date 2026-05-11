# Benchmarking

40-query benchmark of 4 spatial transcriptomics agents:
**Vanilla LLM**, **Biomni**, **SpatialAgent**, **STAT**.

```
queries.json                    40 benchmark queries
DATA.md                         dataset download URL + layout
raw_results/{system}/{Q01..Q40}/result.json
                                full per-query outputs (text only)
evaluations/                    LLM-judge prompt, scores, rationale
scripts/run_stat.py             reproduce STAT outputs
```

## Reproduce

```bash
pip install stat-agent
# Download data (see DATA.md), then:
python scripts/run_stat.py --api-key YOUR_KEY --query Q05
```

Defaults to Poe (`--model Claude-Sonnet-4`). Other providers:

```bash
python scripts/run_stat.py --api-key sk-ant-XXX \
    --provider anthropic --model claude-sonnet-4-5 --query Q05
```

Supported `--provider`: `poe`, `openai`, `anthropic`, `google`, `xai`,
`deepseek`, `moonshot`, `zhipu`. Omit `--query` to run all 40.

Output → `out/{Q}/result.json` + `output.h5ad`.

## Results (from `evaluations/eval_all_merged.json`)

| System | Success | Mean quality | Win rate |
|--------|---------|--------------|----------|
| Vanilla LLM | 9/40 | 3.78 | 2/40 |
| Biomni | 35/40 | 3.83 | 10/40 |
| SpatialAgent | 37/40 | 4.22 | 17/40 |
| **STAT** | **39/40** | **4.51** | **31/40** |

The `.h5ad` outputs are not committed (large, regenerable). `result.json`
holds the full response, code, stdout, tokens, and timing — what the
LLM judge scored.
