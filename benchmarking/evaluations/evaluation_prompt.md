# LLM Judge Evaluation — Prompt Template

## For Paper Methods Section

We evaluated each system's output using Claude Opus 4.6 as an expert judge. For each of the 40 benchmark queries, the judge reviewed the complete output of all four systems — including the generated code, execution output, error messages, and the resulting AnnData object — and assessed each system on three dimensions:

### Evaluation Dimensions

**1. Task Success (Binary: Yes/No)**

A system is judged successful if it accomplished the stated analysis goal and produced usable results. Specifically:

| Task Type | Success Criteria |
|-----------|-----------------|
| Cell type annotation (T1) | Produced a celltype/annotation column with biologically meaningful labels (not just numeric cluster IDs) |
| Spatial domain detection (T2) | Assigned spatial domain labels to cells/spots |
| Spatially variable genes (T3) | Identified genes with spatial statistics (e.g., Moran's I, SpatialDE q-values), not just expression variance |
| Cell-cell communication (T4) | Identified ligand-receptor interactions or communication patterns using a proper database (e.g., CellPhoneDB, CellChat, LIANA) |
| Neighborhood enrichment (T5) | Performed spatial co-localization or enrichment analysis with statistical testing |
| Deconvolution (T6) | Estimated cell type proportions per spot using the provided reference |
| Niche detection (T7) | Identified spatial niches/microenvironments based on local cell type composition |
| Differential expression (T8) | Identified differentially expressed genes between specified groups with statistical testing |
| GO/Pathway enrichment (T9) | Performed formal statistical enrichment analysis (not manual gene categorization) |
| Batch integration (T10) | Loaded ALL input files and applied batch correction (e.g., Harmony, BBKNN, scVI) |
| General/Exploratory (T11) | Provided meaningful summary or analysis of the dataset |
| Multi-step (Q31-Q34) | ALL steps completed — partial completion is judged as failure |
| Infeasible (Q35) | Attempted a reasonable alternative approach OR correctly explained the limitation |
| Out-of-scope (Q36-Q38) | Correctly explained why the task cannot be done with the available data/tools |
| Missing prerequisite (Q39-Q40) | Identified the missing prerequisite OR performed it as a preliminary step |

**2. Quality Score (1-5 scale, only for successful systems)**

| Score | Description |
|-------|-------------|
| 5 — Excellent | Correct, well-established method; appropriate parameters; clear, interpretable output; biologically sound results |
| 4 — Good | Correct method with minor issues (e.g., suboptimal parameters, verbose output, slightly unconventional approach) |
| 3 — Acceptable | Task completed but with notable issues (e.g., unusual method choice, partial results, over/under-segmentation) |
| 2 — Marginal | Technically produced output, but results are questionable or barely useful |
| 1 — Poor | Produced output but results are clearly wrong or misleading |

**3. Comparative Rank (among successful systems per query)**

All successful systems are ranked from 1 (best) to N. Ties are allowed when systems produce comparable quality. Systems that failed receive no rank.

### Judge Input Per Query

For each query, the judge received:
- The user query text and dataset description
- For each system: full text response, generated Python code, stdout/stderr from execution, and a summary of the output AnnData object (number of cells/spots, new columns added, obsm keys, uns keys, and sample values from key result columns)

### Aggregated Metrics

From the 40 per-query judgments, we computed:
- **Success rate**: Fraction of queries where the system was judged successful
- **Mean quality**: Average quality score across successful queries
- **Mean rank**: Average rank across successful queries (lower is better)
- **Win rate**: Fraction of queries where the system achieved rank 1
