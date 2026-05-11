# Benchmark dataset

The 40 benchmark queries operate on three public spatial transcriptomics
datasets plus their ground-truth annotations.

## Download

A pre-packaged tarball containing all four directories is available at:

> <https://drive.google.com/file/d/1H5SePwMJh7c03oac-Epwk55tBJpu2Uuo/view?usp=sharing>

Total size: ~2.6 GB uncompressed.

```bash
# After download, extract under this directory:
tar -xzf stat_benchmark_data.tar.gz -C .
# Resulting layout: ./data/{dlpfc,mouse_brain,breast_cancer,ground_truth}
```

The default expected location is `paper/PaperRepro/benchmarking/data/`.
Override with `--data-dir` on `run_stat.py`.

## Directory layout

```
data/
├── dlpfc/                                Human DLPFC (10x Visium)
│   ├── dlpfc_151673.h5ad                 Single-slice queries (Q05-Q10, Q17, Q18, …)
│   ├── dlpfc_151507.h5ad
│   ├── dlpfc_151508.h5ad
│   ├── dlpfc_151509.h5ad                 Combined for Q25 (4-slice integration)
│   └── dlpfc_reference.h5ad              scRNA-seq reference for Q17 deconvolution
│
├── mouse_brain/                          Mouse brain cortex (MERFISH)
│   ├── mouse_brain_no_celltype.h5ad      For annotation queries (Q01, Q03, …)
│   ├── mouse_brain_section_A.h5ad        With cell-type labels (Q11, Q14, …)
│   ├── mouse_brain_section_B.h5ad        Second slice for Q26 integration
│   └── …
│
├── breast_cancer/                        Human breast cancer (Xenium)
│   ├── breast_cancer.h5ad
│   └── breast_cancer_reference.h5ad      scRNA-seq reference (Q02, Q04, Q33)
│
└── ground_truth/                         Expert annotations for Track-B metrics
    ├── dlpfc_layers.csv                  Cortical layer labels (Q05-Q07)
    ├── mouse_brain_celltype.csv          Expert cell-type labels (Q01, Q03)
    └── …
```

## Dataset details

| ID | Tissue | Technology | Cells / spots | Genes | Source |
|----|--------|-----------|---------------|-------|--------|
| D1 | Human DLPFC | 10x Visium | 3,611 (×4 slices) | 33,538 | Maynard et al., Nature Neuroscience 2021 |
| D2 | Mouse brain cortex | MERFISH | 31,982 (slice A) | 1,122 | Allen Institute mouse brain atlas |
| D3 | Human breast cancer | 10x Xenium | 160,286 | 306 | 10x Genomics demo dataset |

## License

All three datasets are public and re-distributed here for reproducibility
under their original licenses. Please cite the original publications if you
re-use them outside this benchmark.
