# STAT-PaperRepro

Reproducibility code for **STAT — Spatial Transcriptomics Analytical agenT**.

- Software: <https://github.com/chenyhvvvv/STAT-agent>
- Preprint: <https://doi.org/10.64898/2026.05.01.722244>

## Layout

| Directory | Contents |
| --- | --- |
| `breast_cancer/` | <!-- TODO: short description --> |
| `colorectal_cancer/` | Two end-to-end STAT conversational analyses on a colorectal cancer dataset, with notebook + per-turn logs + UI screenshots |
| `benchmarking/` | 40-query benchmark of 4 systems (Vanilla / Biomni / SpatialAgent / STAT). Raw results + reproducible STAT runner |
| `ablation_study/` | STAT with 7 LLM backbones on the 40 queries, plus 90 pipeline-stage queries. Raw results + runnable scripts |

Each subdirectory has its own `README.md` and `DATA.md` (download URL).

## Install

```bash
pip install stat-agent
```

## Citation

<!-- TODO: BibTeX block once the paper has a stable citation -->
