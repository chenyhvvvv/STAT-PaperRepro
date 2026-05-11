# Ablation dataset

The 40-query benchmark portion of the ablation uses the **same dataset** as
`../benchmarking/`. The pipeline-stage tests use mock sessions only and need
no real data.

## Download

A pre-packaged tarball containing all four directories is available at:

> <https://drive.google.com/file/d/1H5SePwMJh7c03oac-Epwk55tBJpu2Uuo/view?usp=sharing>

(Same URL as the main benchmarking dataset — they share data.)

```bash
# After download, extract under this directory:
tar -xzf stat_benchmark_data.tar.gz -C .
# Resulting layout: ./data/{dlpfc,mouse_brain,breast_cancer,ground_truth}
```

If you have already downloaded the dataset for `../benchmarking/`, you can
symlink instead of copying:

```bash
ln -s ../benchmarking/data data
```

## Directory layout

```
data/
├── dlpfc/                                Human DLPFC (10x Visium)
├── mouse_brain/                          Mouse brain cortex (MERFISH)
├── breast_cancer/                        Human breast cancer (Xenium)
└── ground_truth/                         Expert annotations (Track-B metrics)
```

See `../benchmarking/DATA.md` for full dataset details and citations.

## Pipeline-stage tests need no data

`run_pipeline_test.py` uses `MockSession` objects defined in
`scripts/pipeline_test_sessions.py`. They expose the same interface as
`SimpleSession` but carry only metadata (slice IDs, modality, data level,
n_obs, n_vars, has_celltype, etc.) — no real expression matrices. This makes
the pipeline-stage tests fast (~5 min) and deterministic.
