# Comprehensive Benchmark Evaluation — All 40 Queries

## Overall Summary

| Metric | Vanilla LLM | Biomni | SpatialAgent | STAT |
|--------|------------|--------|--------------|------|
| **Success Rate** | 9/40 | 35/40 | 37/40 | 39/40 |
| **Avg Quality** | 3.78 | 3.83 | 4.22 | 4.51 |
| **Avg Rank** | 2.33 | 2.09 | 1.62 | 1.26 |
| **Win Rate (R=1)** | 2/40 | 10/40 | 17/40 | 31/40 |

## Success Rate by Task Category

| Task | Vanilla LLM | Biomni | SpatialAgent | STAT |
|------|------------|--------|--------------|------|
| T1: Cell Type Annotation | 1/4 | 4/4 | 4/4 | 4/4 |
| T2: Spatial Domain Detection | 0/3 | 3/3 | 3/3 | 3/3 |
| T3: Spatially Variable Genes | 0/3 | 3/3 | 3/3 | 3/3 |
| T4: Cell-Cell Communication | 0/3 | 3/3 | 3/3 | 3/3 |
| T5: Neighborhood Enrichment | 0/3 | 3/3 | 3/3 | 3/3 |
| T6: Deconvolution | 2/2 | 2/2 | 2/2 | 2/2 |
| T7: Niche Detection | 1/2 | 2/2 | 2/2 | 2/2 |
| T8: Differential Expression | 2/2 | 2/2 | 2/2 | 2/2 |
| T9: GO/Pathway Enrichment | 0/2 | 1/2 | 1/2 | 2/2 |
| T10: Batch Integration | 0/2 | 2/2 | 2/2 | 2/2 |
| T11: General/Exploratory | 2/4 | 4/4 | 4/4 | 4/4 |
| multi-step: Multi-Step Pipeline | 0/4 | 4/4 | 4/4 | 4/4 |
| infeasible: Infeasible Task | 1/1 | 1/1 | 1/1 | 1/1 |
| out-of-scope: Out-of-Scope Task | 0/3 | 0/3 | 1/3 | 2/3 |
| missing-prereq: Missing Prerequisite | 0/2 | 1/2 | 2/2 | 2/2 |

## Success Rate by Difficulty

| Difficulty | Vanilla LLM | Biomni | SpatialAgent | STAT |
|-----------|------------|--------|--------------|------|
| Clear (16) | 6/16 | 15/16 | 15/16 | 16/16 |
| Vague (14) | 2/14 | 14/14 | 14/14 | 14/14 |
| Multi (4) | 0/4 | 4/4 | 4/4 | 4/4 |
| Special (6) | 1/6 | 2/6 | 4/6 | 5/6 |

## Average Quality by Task Category (successful queries only)

| Task | Vanilla LLM | Biomni | SpatialAgent | STAT |
|------|------------|--------|--------------|------|
| T1: Cell Type Annotation | 4.0 | 4.8 | 4.0 | 4.5 |
| T2: Spatial Domain Detection | — | 3.3 | 3.7 | 4.3 |
| T3: Spatially Variable Genes | — | 3.3 | 4.0 | 5.0 |
| T4: Cell-Cell Communication | — | 3.7 | 5.0 | 5.0 |
| T5: Neighborhood Enrichment | — | 3.7 | 5.0 | 5.0 |
| T6: Deconvolution | 3.0 | 2.0 | 3.0 | 5.0 |
| T7: Niche Detection | 4.0 | 4.0 | 4.5 | 4.5 |
| T8: Differential Expression | 4.0 | 5.0 | 5.0 | 4.0 |
| T9: GO/Pathway Enrichment | — | 4.0 | 4.0 | 4.5 |
| T10: Batch Integration | — | 3.5 | 4.5 | 4.5 |
| T11: General/Exploratory | 5.0 | 4.8 | 4.8 | 4.8 |
| multi-step: Multi-Step Pipeline | — | 3.5 | 4.2 | 4.8 |
| infeasible: Infeasible Task | 2.0 | 3.0 | 3.0 | 3.0 |
| out-of-scope: Out-of-Scope Task | — | — | 3.0 | 3.5 |
| missing-prereq: Missing Prerequisite | — | 4.0 | 3.5 | 3.5 |

## Per-Query Results (S=Success, Q=Quality, R=Rank)

| QID | Task | Difficulty | Vanilla | Biomni | SpAgent | STAT |
|-----|------|-----------|---------|--------|---------|------|
| Q01 | T1 | clear | N/Q-/R- | Y/Q5/R1 | Y/Q4/R2 | Y/Q4/R2 |
| Q02 | T1 | clear | Y/Q4/R2 | Y/Q5/R1 | Y/Q4/R2 | Y/Q5/R1 |
| Q03 | T1 | vague | N/Q-/R- | Y/Q4/R1 | Y/Q4/R2 | Y/Q4/R2 |
| Q04 | T1 | vague | N/Q-/R- | Y/Q5/R1 | Y/Q4/R2 | Y/Q5/R1 |
| Q05 | T2 | clear | N/Q-/R- | Y/Q2/R3 | Y/Q4/R2 | Y/Q5/R1 |
| Q06 | T2 | vague | N/Q-/R- | Y/Q4/R2 | Y/Q3/R3 | Y/Q5/R1 |
| Q07 | T2 | vague | N/Q-/R- | Y/Q4/R2 | Y/Q4/R2 | Y/Q3/R3 |
| Q08 | T3 | clear | N/Q-/R- | Y/Q4/R2 | Y/Q4/R2 | Y/Q5/R1 |
| Q09 | T3 | vague | N/Q-/R- | Y/Q3/R3 | Y/Q4/R2 | Y/Q5/R1 |
| Q10 | T3 | clear | N/Q-/R- | Y/Q3/R3 | Y/Q4/R2 | Y/Q5/R1 |
| Q11 | T4 | clear | N/Q-/R- | Y/Q3/R3 | Y/Q5/R1 | Y/Q5/R1 |
| Q12 | T4 | clear | N/Q-/R- | Y/Q4/R2 | Y/Q5/R1 | Y/Q5/R1 |
| Q13 | T4 | vague | N/Q-/R- | Y/Q4/R2 | Y/Q5/R1 | Y/Q5/R1 |
| Q14 | T5 | clear | N/Q-/R- | Y/Q4/R2 | Y/Q5/R1 | Y/Q5/R1 |
| Q15 | T5 | clear | N/Q-/R- | Y/Q3/R3 | Y/Q5/R1 | Y/Q5/R1 |
| Q16 | T5 | vague | N/Q-/R- | Y/Q4/R2 | Y/Q5/R1 | Y/Q5/R1 |
| Q17 | T6 | clear | Y/Q3/R3 | Y/Q2/R4 | Y/Q3/R3 | Y/Q5/R1 |
| Q18 | T6 | vague | Y/Q3/R3 | Y/Q2/R4 | Y/Q3/R3 | Y/Q5/R1 |
| Q19 | T7 | clear | Y/Q4/R3 | Y/Q4/R3 | Y/Q4/R2 | Y/Q5/R1 |
| Q20 | T7 | vague | N/Q-/R- | Y/Q4/R2 | Y/Q5/R1 | Y/Q4/R2 |
| Q21 | T8 | clear | Y/Q4/R2 | Y/Q5/R1 | Y/Q5/R1 | Y/Q4/R2 |
| Q22 | T8 | vague | Y/Q4/R2 | Y/Q5/R1 | Y/Q5/R1 | Y/Q4/R2 |
| Q23 | T9 | clear | N/Q-/R- | N/Q-/R- | N/Q-/R- | Y/Q4/R1 |
| Q24 | T9 | vague | N/Q-/R- | Y/Q4/R2 | Y/Q4/R2 | Y/Q5/R1 |
| Q25 | T10 | clear | N/Q-/R- | Y/Q4/R2 | Y/Q5/R1 | Y/Q5/R1 |
| Q26 | T10 | vague | N/Q-/R- | Y/Q3/R3 | Y/Q4/R2 | Y/Q4/R1 |
| Q27 | T11 | clear | Y/Q5/R1 | Y/Q5/R1 | Y/Q5/R1 | Y/Q5/R1 |
| Q28 | T11 | clear | Y/Q5/R1 | Y/Q5/R1 | Y/Q5/R1 | Y/Q5/R1 |
| Q29 | T11 | vague | N/Q-/R- | Y/Q4/R2 | Y/Q4/R2 | Y/Q5/R1 |
| Q30 | T11 | vague | N/Q-/R- | Y/Q5/R1 | Y/Q5/R1 | Y/Q4/R2 |
| Q31 | multi-step | multi | N/Q-/R- | Y/Q3/R3 | Y/Q4/R2 | Y/Q4/R1 |
| Q32 | multi-step | multi | N/Q-/R- | Y/Q4/R2 | Y/Q5/R1 | Y/Q5/R1 |
| Q33 | multi-step | multi | N/Q-/R- | Y/Q4/R2 | Y/Q4/R2 | Y/Q5/R1 |
| Q34 | multi-step | multi | N/Q-/R- | Y/Q3/R3 | Y/Q4/R2 | Y/Q5/R1 |
| Q35 | infeasible | special | Y/Q2/R4 | Y/Q3/R2 | Y/Q3/R2 | Y/Q3/R1 |
| Q36 | out-of-scope | special | N/Q-/R- | N/Q-/R- | N/Q-/R- | Y/Q3/R1 |
| Q37 | out-of-scope | special | N/Q-/R- | N/Q-/R- | Y/Q3/R1 | N/Q-/R- |
| Q38 | out-of-scope | special | N/Q-/R- | N/Q-/R- | N/Q-/R- | Y/Q4/R1 |
| Q39 | missing-prereq | special | N/Q-/R- | Y/Q4/R1 | Y/Q4/R1 | Y/Q3/R3 |
| Q40 | missing-prereq | special | N/Q-/R- | N/Q-/R- | Y/Q3/R1 | Y/Q4/R1 |

## Evaluation Criteria

- **Success (Y/N)**: Whether the system accomplished the stated analysis goal
- **Quality (1-5)**: 5=Excellent, 4=Good, 3=Acceptable, 2=Marginal, 1=Poor
- **Rank**: Among successful systems, 1=best. Ties allowed.

## Detailed Per-Query Evaluation

---
### Q01: Cell Type Annotation (clear) — Dataset: D2
**Query**: "Annotate cell types on this tissue. It is a mouse brain cortex sample."

**Vanilla LLM (A)**: Ran Leiden clustering and marker-based annotation but output h5ad contains only 1463 of 31982 cells, with 6 cell types identified.
  - Success: **N** | Quality: **-** | Rank: **-**
  - Output contains only 1463 cells (4.6% of data), likely due to timeout or partial write. Incomplete result is unusable.

**Biomni (B)**: Performed Leiden clustering at multiple resolutions and annotated 9 cell types (Oligodendrocytes, Excitatory_Neurons, Astrocytes, Endothelial, Pericytes, Inhibitory_Neurons, OPCs, Microglia, Choroid_Plexus) across 31941 cells.
  - Success: **Y** | Quality: **5** | Rank: **1**
  - Comprehensive annotation with 9 biologically meaningful cell types covering all major brain cell populations. Processed nearly all cells. Multiple resolution analysis adds robustness.

**SpatialAgent (C)**: Performed Leiden clustering and annotated 7 cell types (Excitatory neuron, Inhibitory neuron, Mixed neuron, etc.) across 31966 cells.
  - Success: **Y** | Quality: **4** | Rank: **2**
  - Good annotation with meaningful cell types across nearly all cells. Fewer cell types than B_biomni (7 vs 9) - missing some distinct populations like OPCs and Microglia.

**STAT (D)**: Used LLM-based clustering annotation to identify 22 cell types including layer-specific excitatory neurons across 31757 cells.
  - Success: **Y** | Quality: **4** | Rank: **2**
  - Produced detailed layer-specific neuron subtypes (Layer 2/3, Layer 4, etc.) which is biologically sophisticated. However, 22 types may be over-segmented for MERFISH data. Processed slightly fewer cells (31757 vs 31982).

---
### Q02: Cell Type Annotation (clear) — Dataset: D3
**Query**: "Identify cell types in this breast cancer tissue sample. I have a single-cell reference dataset at './breast_cancer_reference.h5ad' with cell type annotations that you can optionally use."

**Vanilla LLM (A)**: Used reference-based label transfer to annotate 17 cell types including Invasive Tumor, Macrophages, T cells, etc.
  - Success: **Y** | Quality: **4** | Rank: **2**
  - Successfully used the reference dataset for label transfer. Identified all 17 cell types. Added confidence scores.

**Biomni (B)**: Applied reference-based annotation transferring 17 cell types from the scRNA-seq reference, with prediction scores and filtering.
  - Success: **Y** | Quality: **5** | Rank: **1**
  - Comprehensive reference-based annotation with QC filtering and confidence scores. All 17 cell types transferred correctly.

**SpatialAgent (C)**: Used KNN classification to transfer 17 cell types from reference to spatial data.
  - Success: **Y** | Quality: **4** | Rank: **2**
  - Successfully identified all 17 cell types using KNN-based transfer. Straightforward and effective approach.

**STAT (D)**: Used scANVI deep learning model for reference-based label transfer, identifying 17 cell types.
  - Success: **Y** | Quality: **5** | Rank: **1**
  - Used scANVI which is a state-of-the-art method for label transfer that accounts for batch effects. All 17 cell types correctly identified. Though slower (686s), method is more robust.

---
### Q03: Cell Type Annotation (vague) — Dataset: D2
**Query**: "What cell types are present in this tissue?"

**Vanilla LLM (A)**: Filtered to only 1463 cells, produced 20 cluster numbers as celltype labels (0-19) with only 3 named predicted_celltype values.
  - Success: **N** | Quality: **-** | Rank: **-**
  - Only processed 1463 of 31982 cells. The celltype column contains cluster numbers (0-19), not meaningful cell type names. The predicted_celltype has only 3 types for a subset. Fundamentally incomplete.

**Biomni (B)**: Performed clustering and annotated 9 cell types (Oligodendrocytes, Excitatory_neurons, Pericytes, Endothelial, Astrocytes, Inhibitory_neurons, OPCs, Ependymal, Unknown) across all 31982 cells.
  - Success: **Y** | Quality: **4** | Rank: **1**
  - Good annotation with 9 meaningful cell types across all cells. Includes an 'Unknown' category which is honest. Comprehensive brain cell type coverage.

**SpatialAgent (C)**: Clustered and annotated 11 cell types including Glutamatergic_Neurons, Neurons, GABAergic_Neurons across 31941 cells.
  - Success: **Y** | Quality: **4** | Rank: **2**
  - Good annotation with 11 cell types across nearly all cells. Some types like generic 'Neurons' are less informative than B_biomni's more specific labels.

**STAT (D)**: Used LLM-based annotation to identify 22 cell types with layer-specific neuron subtypes across 31757 cells.
  - Success: **Y** | Quality: **4** | Rank: **2**
  - Detailed layer-specific annotations are biologically meaningful. 22 types may be over-segmented but captures fine structure. Slightly fewer cells processed.

---
### Q04: Cell Type Annotation (vague) — Dataset: D3
**Query**: "Can you identify the different cell populations here? I have a reference scRNA-seq dataset at './breast_cancer_reference.h5ad' if that helps."

**Vanilla LLM (A)**: Code timed out without producing an output h5ad file.
  - Success: **N** | Quality: **-** | Rank: **-**
  - TIMEOUT - no output produced. Complete failure.

**Biomni (B)**: Used reference-based annotation to transfer 17 cell types from scRNA-seq reference dataset.
  - Success: **Y** | Quality: **5** | Rank: **1**
  - Successfully transferred all 17 cell types using the reference. Included confidence metrics and validation.

**SpatialAgent (C)**: Identified 17 cell types using the reference dataset, with confidence scores for each cell.
  - Success: **Y** | Quality: **4** | Rank: **2**
  - Good reference-based annotation with all 17 cell types. Added confidence scores.

**STAT (D)**: Used scANVI for deep learning-based label transfer from reference, identifying 17 cell types.
  - Success: **Y** | Quality: **5** | Rank: **1**
  - State-of-the-art scANVI method for label transfer. All 17 cell types correctly identified.

---
### Q05: Spatial Domain Detection (clear) — Dataset: D1
**Query**: "Identify spatial domains in this brain tissue. There should be about 7 distinct regions including cortical layers and white matter."

**Vanilla LLM (A)**: Code errored with KeyError for missing 'neighbors' in .uns after building spatial graph.
  - Success: **N** | Quality: **-** | Rank: **-**
  - Runtime error - pipeline failed to build neighbors graph correctly before Leiden clustering.

**Biomni (B)**: Identified spatial domains but only found 4 (L3, L5, WM, L6) instead of the expected 7 cortical layers + WM.
  - Success: **Y** | Quality: **2** | Rank: **3**
  - Only 4 spatial domains found when 7 were expected. Missing L1, L2, L4. Significantly under-segmented despite extensive clustering attempts at multiple resolutions.

**SpatialAgent (C)**: Identified 8 spatial domains (close to the target of 7) with cortical layer annotations.
  - Success: **Y** | Quality: **4** | Rank: **2**
  - Found 8 domains, close to the expected 7. Reasonable spatial domain identification with biological annotations.

**STAT (D)**: Used SpaGCN to identify exactly 7 spatial domains matching the expected cortical layer structure.
  - Success: **Y** | Quality: **5** | Rank: **1**
  - Used SpaGCN (specialized spatial domain tool) and found exactly 7 domains matching the expected cortical layers + WM. Best match to ground truth.

---
### Q06: Spatial Domain Detection (vague) — Dataset: D1
**Query**: "Can you find the spatial structure in this tissue?"

**Vanilla LLM (A)**: Code errored with KeyError trying to access 'leiden_0.5' column that doesn't exist in obs.
  - Success: **N** | Quality: **-** | Rank: **-**
  - Runtime error - code generated invalid column reference. No output produced.

**Biomni (B)**: Identified 7 spatial domains with descriptive names (Deep_Layer, Superficial_Layer, White_Matter_Core, etc.).
  - Success: **Y** | Quality: **4** | Rank: **2**
  - Found 7 domains matching expected count. Descriptive domain names though they don't directly correspond to cortical layers (e.g., 'Layer_Transition' vs 'L2').

**SpatialAgent (C)**: Used GraphST and identified 10 spatial domains, over-segmenting the expected 7 layers.
  - Success: **Y** | Quality: **3** | Rank: **3**
  - Found 10 domains, somewhat over-segmented compared to 7 expected. Numeric domain labels without biological annotation.

**STAT (D)**: Used SpaGCN to identify exactly 7 spatial domains matching the cortical layer structure.
  - Success: **Y** | Quality: **5** | Rank: **1**
  - SpaGCN correctly identified 7 domains. Best match to the expected cortical layer architecture.

---
### Q07: Spatial Domain Detection (vague) — Dataset: D2
**Query**: "Identify distinct tissue regions based on spatial gene expression."

**Vanilla LLM (A)**: Code timed out without producing an output h5ad file.
  - Success: **N** | Quality: **-** | Rank: **-**
  - TIMEOUT - no output produced.

**Biomni (B)**: Identified 12 tissue regions using combined PCA and K-means spatial clustering with biological annotations.
  - Success: **Y** | Quality: **4** | Rank: **2**
  - Found 12 distinct regions with tissue annotations and marker genes. Comprehensive analysis with region centroids stored.

**SpatialAgent (C)**: Used Leiden clustering to identify 14 spatial domains with biological annotations including oligodendrocytes, endothelial, astrocyte regions.
  - Success: **Y** | Quality: **4** | Rank: **2**
  - Found 14 domains with meaningful biological annotations. Good spatial domain identification for MERFISH data.

**STAT (D)**: Used KMeans clustering on gene expression to identify spatial regions stored in 'spatial_region' column.
  - Success: **Y** | Quality: **3** | Rank: **3**
  - Produced spatial regions but used basic KMeans rather than spatial-aware methods. No biological annotation of regions in the output.

---
### Q08: Spatially Variable Genes (clear) — Dataset: D1
**Query**: "Find genes that show significant spatial expression patterns across this tissue."

**Vanilla LLM (A)**: Attempted Moran's I via Squidpy but crashed with RuntimeError during computation.
  - Success: **N** | Quality: **-** | Rank: **-**
  - Runtime error during Squidpy spatial analysis (multiprocessing EOFError). No SVG results produced.

**Biomni (B)**: Identified spatially variable genes using spatial statistics, results stored in uns['spatial_analysis'].
  - Success: **Y** | Quality: **4** | Rank: **2**
  - Successfully identified SVGs with spatial statistics. Results stored in AnnData. Used appropriate methods.

**SpatialAgent (C)**: Computed Moran's I for spatial autocorrelation, results stored in uns['moranI'] and uns['spatial_analysis_summary'].
  - Success: **Y** | Quality: **4** | Rank: **2**
  - Used Moran's I which is a standard SVG detection method. Results properly stored with p-values.

**STAT (D)**: Used SpatialDE (Gaussian process regression) to identify SVGs, with results stored as DataFrame in uns['spatialde_results'].
  - Success: **Y** | Quality: **5** | Rank: **1**
  - SpatialDE is a gold-standard method specifically designed for SVG detection in spatial transcriptomics. Produces proper statistical framework with model-based p-values.

---
### Q09: Spatially Variable Genes (vague) — Dataset: D1
**Query**: "Which genes have interesting spatial patterns?"

**Vanilla LLM (A)**: Attempted Moran's I via Squidpy but crashed with RuntimeError during computation.
  - Success: **N** | Quality: **-** | Rank: **-**
  - Runtime error during Squidpy spatial analysis. Same issue as Q08.

**Biomni (B)**: Identified top spatially variable genes using spatial coefficient of variation (MAG, MOBP, PPP1R14A, TF, etc.).
  - Success: **Y** | Quality: **3** | Rank: **3**
  - Identified biologically relevant SVGs but used a simplistic 'Spatial CV' metric rather than proper spatial statistics like Moran's I or SpatialDE. No formal statistical testing stored in the h5ad.

**SpatialAgent (C)**: Computed Moran's I identifying top SVGs (SCGB2A2, MOBP, GFAP, TF, CNP, MAG, etc.).
  - Success: **Y** | Quality: **4** | Rank: **2**
  - Used proper Moran's I spatial autocorrelation. Identified biologically meaningful genes. MOBP, GFAP, MAG are well-known spatially patterned genes in brain.

**STAT (D)**: Used SpatialDE Gaussian process regression to identify SVGs with full statistical results stored.
  - Success: **Y** | Quality: **5** | Rank: **1**
  - SpatialDE is the gold-standard SVG method. Full statistical results (DataFrame) stored in uns. Proper model-based inference.

---
### Q10: Spatially Variable Genes (clear) — Dataset: D2
**Query**: "Identify spatially variable genes in this mouse brain section."

**Vanilla LLM (A)**: Attempted Moran's I via Squidpy but crashed with RuntimeError during computation.
  - Success: **N** | Quality: **-** | Rank: **-**
  - Runtime error during Squidpy spatial analysis. Same multiprocessing issue as Q08/Q09.

**Biomni (B)**: Identified SVGs using spatial variability scores (correlation with spatial coordinates), stored in uns['spatial_variable_genes'].
  - Success: **Y** | Quality: **3** | Rank: **3**
  - Found SVGs but used simplistic correlation with spatial coordinates rather than proper spatial autocorrelation methods. Found 65 genes with score > 0.2.

**SpatialAgent (C)**: Computed Moran's I for 1000 genes, finding 947 significant (p<0.05), with top hits including Htr7, Gzmk, Arhgap36.
  - Success: **Y** | Quality: **4** | Rank: **2**
  - Used proper Moran's I with permutation testing. 947/1000 significant suggests possible multiple testing issue, but identified meaningful SVGs.

**STAT (D)**: Used Moran's I via Squidpy for all 1122 genes, finding 1060 significant SVGs, stored results in adata.var and uns.
  - Success: **Y** | Quality: **5** | Rank: **1**
  - Properly used Moran's I for the large dataset (>10K cells), correctly chose it over SpatialDE for scalability. Tested all genes. Results properly stored in adata.var for per-gene access.

---
### Q11: Cell-Cell Communication (clear) — Dataset: D2
**Query**: "Analyze ligand-receptor interactions between cell types in this mouse brain tissue."

**Vanilla LLM (A)**: Attempted LIANA analysis but failed with TypeError on rank_aggregate methods parameter; no output h5ad produced.
  - Success: **N** | Quality: **-** | Rank: **-**
  - Code crashed due to incorrect LIANA API usage (wrong keyword argument 'methods'). No LR interaction results saved.

**Biomni (B)**: Performed custom ligand-receptor analysis identifying 3 LR pairs (Ntf3-Ntrk3, Wnt5a-Fzd2, Sema6a-Epha10) with spatial interaction scoring across 28 cell types.
  - Success: **Y** | Quality: **3** | Rank: **3**
  - Completed analysis but used only 3 manually curated LR pairs rather than a comprehensive database. Results are biologically reasonable but limited in scope compared to standard CCI tools.

**SpatialAgent (C)**: Ran LIANA with multiple algorithms (CellPhoneDB, Connectome, NATMI) detecting 4,089 total interactions with 2,431 significant, identifying dominant neuropeptide signaling pathways.
  - Success: **Y** | Quality: **5** | Rank: **1**
  - Used proper LIANA multi-method consensus approach with comprehensive LR database. Identified biologically meaningful pathways (Penk signaling, opioid receptors) with statistical testing. Results stored in uns['liana_analysis'].

**STAT (D)**: Ran LIANA+ with mouse-specific LR database on the brain tissue, identifying significant communication pathways between cell populations with proper species configuration.
  - Success: **Y** | Quality: **5** | Rank: **1**
  - Used LIANA+ with correct mouse species database, proper preprocessing, and stored comprehensive results in uns['liana_res']. Efficient execution (87s vs 376s for C).

---
### Q12: Cell-Cell Communication (clear) — Dataset: D3
**Query**: "Find cell-cell communication patterns between tumor and immune cells in this human breast cancer sample."

**Vanilla LLM (A)**: Attempted LIANA but it failed; fell back to spatial proximity analysis between tumor (Invasive/Prolif) and immune cells (Macrophages only), computing distances but no actual LR interactions.
  - Success: **N** | Quality: **-** | Rank: **-**
  - LIANA failed and fallback only computed spatial distances between 2 tumor and 2 immune types. Missed most immune types (T cells, B cells, DCs). No actual ligand-receptor interaction analysis performed.

**Biomni (B)**: Analyzed tumor-immune communication identifying 57,377 tumor and 50,385 immune cells with spatial neighborhood analysis and LR pair detection.
  - Success: **Y** | Quality: **4** | Rank: **2**
  - Correctly identified all tumor and immune cell categories. Performed spatial neighborhood and LR analysis. Good biological interpretation but custom implementation rather than established CCI tool.

**SpatialAgent (C)**: Comprehensive CCI analysis detecting 179 LR interactions between tumor and immune cells, identifying spatial avoidance patterns (immune exclusion) and molecular communication despite separation.
  - Success: **Y** | Quality: **5** | Rank: **1**
  - Excellent analysis combining spatial co-occurrence (z-scores for avoidance) with molecular LR interactions. Identified immune exclusion pattern which is biologically important in breast cancer. Stored results in uns.

**STAT (D)**: Ran LIANA+ with human LR database identifying significant ligand-receptor interactions between all 17 cell types including tumor-immune communication patterns.
  - Success: **Y** | Quality: **5** | Rank: **1**
  - Used proper LIANA+ framework with human species database and comprehensive cell type coverage. Stored results in uns['liana_res'] and uns['cell_communication']. Fast execution (174s).

---
### Q13: Cell-Cell Communication (vague) — Dataset: D3
**Query**: "How are the cells communicating with each other?"

**Vanilla LLM (A)**: Ran LIANA but execution appears to have stalled during cell type proximity computation; no output h5ad produced.
  - Success: **N** | Quality: **-** | Rank: **-**
  - LIANA ran but process did not complete within time limit. No output file saved. Progress stuck at computing cell type proximities.

**Biomni (B)**: Built spatial neighborhood graphs at multiple radii (30/50/100um) and analyzed LR expression patterns across 17 cell types with interaction matrices.
  - Success: **Y** | Quality: **4** | Rank: **2**
  - Good multi-scale spatial analysis with neighborhood diversity metrics. Stored communication summary and LR expression by cell type. Interpreted vague query correctly as CCI analysis.

**SpatialAgent (C)**: Performed comprehensive LIANA analysis identifying dominant S100A4-ERBB2 and CXCL12-CXCR4 signaling pathways with 148 immune-to-tumor and 31 tumor-to-immune interactions.
  - Success: **Y** | Quality: **5** | Rank: **1**
  - Excellent interpretation of vague query. Identified biologically significant pathways (S100A4-ERBB2 for tumor progression, CXCL12-CXCR4 for immune recruitment). Detailed breakdown by cell type pairs.

**STAT (D)**: Ran LIANA+ with human LR database identifying significant ligand-receptor interactions between all 17 cell types in the breast cancer dataset.
  - Success: **Y** | Quality: **5** | Rank: **1**
  - Correctly interpreted vague query as CCI task and used LIANA+ with proper human species config. Results stored in uns['liana_res']. Efficient (103s).

---
### Q14: Neighborhood Enrichment (clear) — Dataset: D2
**Query**: "Test whether certain cell types tend to co-localize or avoid each other spatially in this mouse brain tissue."

**Vanilla LLM (A)**: Attempted squidpy co_occurrence but crashed with TypeError on spatial_connectivities_key parameter.
  - Success: **N** | Quality: **-** | Rank: **-**
  - Code error due to incorrect squidpy API usage. No co-localization results produced.

**Biomni (B)**: Performed KNN-based spatial analysis (k=10) on 16 cell types with chi-square testing, finding 205/240 significant pairs including 38 co-localized and 167 avoidance patterns.
  - Success: **Y** | Quality: **4** | Rank: **2**
  - Good statistical approach with FDR correction. Identified biologically meaningful patterns (HY GABA-HY Glut co-localization). Stored results in uns['spatial_colocalization_summary'].

**SpatialAgent (C)**: Ran neighborhood enrichment analysis identifying strong co-localization (HY GABA-HY Glut z=35.2) and avoidance (IT-ET Glut-OPC-Oligo z=-70.04) patterns with z-score statistics.
  - Success: **Y** | Quality: **5** | Rank: **1**
  - Used squidpy neighborhood enrichment with permutation testing. Excellent biological interpretation of cortical laminar structure, neurovascular units, and gray/white matter segregation. Z-scores stored properly.

**STAT (D)**: Performed squidpy neighborhood enrichment analysis with permutation testing on all 28 cell types, computing z-scores for spatial relationships.
  - Success: **Y** | Quality: **5** | Rank: **1**
  - Used proper squidpy nhood_enrichment with permutation-based statistical testing. Results stored in uns['celltype_nhood_enrichment'] and uns['nhood_enrichment_zscore']. Fast execution (52s).

---
### Q15: Neighborhood Enrichment (clear) — Dataset: D3
**Query**: "Analyze spatial co-localization patterns between cell types in this breast cancer sample."

**Vanilla LLM (A)**: Started squidpy spatial_neighbors and co-occurrence analysis but crashed with multiprocessing error during execution.
  - Success: **N** | Quality: **-** | Rank: **-**
  - Execution failed with multiprocessing spawn error. No results produced despite correct approach selection.

**Biomni (B)**: Analyzed spatial neighborhoods computing mean neighbor distances and nearest-neighbor distances for each cell type, detecting tumor-immune interactions with 8-10x enrichment.
  - Success: **Y** | Quality: **3** | Rank: **3**
  - Completed analysis but methodology is simplistic (distance-based rather than permutation-based). Claims 8-10x enrichment but storage suggests limited statistical rigor.

**SpatialAgent (C)**: Comprehensive analysis with neighborhood enrichment, interaction matrices, and Ripley's L function detecting tumor co-localization (z=251.2), immune clustering (CD8-CD4 z=94.4), and immune exclusion patterns.
  - Success: **Y** | Quality: **5** | Rank: **1**
  - Used multiple methods (squidpy nhood enrichment, co-occurrence, Ripley's L). Excellent biological interpretation of immune exclusion and tumor spatial organization. Most comprehensive analysis.

**STAT (D)**: Performed squidpy neighborhood enrichment analysis with permutation testing across all 17 cell types, computing z-scores stored in structured format.
  - Success: **Y** | Quality: **5** | Rank: **1**
  - Used proper squidpy nhood_enrichment with permutation testing. Results well-stored in uns. Very fast execution (58s vs 1043s for C) while maintaining statistical rigor.

---
### Q16: Neighborhood Enrichment (vague) — Dataset: D2
**Query**: "Are certain cell types found near each other in this tissue?"

**Vanilla LLM (A)**: Attempted to compute full pairwise distance matrix for 31,982 cells which caused a timeout (memory/compute explosion).
  - Success: **N** | Quality: **-** | Rank: **-**
  - Tried to compute a 32K x 32K distance matrix using scipy pdist, which is computationally infeasible. Timed out at 338s.

**Biomni (B)**: Analyzed spatial enrichment with diversity and homogeneity metrics, identifying hypothalamic neuron co-localization (3.9x enrichment) and neurovascular units.
  - Success: **Y** | Quality: **4** | Rank: **2**
  - Good results with spatial enrichment matrix and significance tests stored in uns. Identified biologically meaningful patterns. Clear presentation for vague query.

**SpatialAgent (C)**: Performed neighborhood enrichment analysis with z-scores identifying strong co-localization (HY GABA-HY Glut z=35.59) and avoidance (IT-ET Glut-OPC-Oligo z=-70.04) patterns.
  - Success: **Y** | Quality: **5** | Rank: **1**
  - Used proper squidpy neighborhood enrichment. Excellent biological interpretation including E-I balance, striatal GABAergic organization, and perivascular niches. Comprehensive z-score reporting.

**STAT (D)**: Performed squidpy neighborhood enrichment analysis with permutation-based z-scores across 25 cell types in the brain tissue.
  - Success: **Y** | Quality: **5** | Rank: **1**
  - Correct method (squidpy nhood_enrichment), proper statistical testing, well-structured output. Fastest execution (49s). Correctly interpreted vague query.

---
### Q17: Deconvolution (clear) — Dataset: D1
**Query**: "Estimate cell type proportions for each spot in this Visium tissue. I have a single-cell reference dataset at './dlpfc_reference.h5ad' with cell type annotations."

**Vanilla LLM (A)**: Implemented custom NNLS-based deconvolution using reference cell type signatures, estimating proportions for all 33 reference cell types across 3,611 spots.
  - Success: **Y** | Quality: **3** | Rank: **3**
  - Custom NNLS implementation works but lacks the statistical rigor of dedicated deconvolution tools (RCTD, cell2location). Proportions stored in obs columns. Reasonable results but not optimal.

**Biomni (B)**: Performed NNLS deconvolution with reference data, finding Mix_1 dominant in 92.5% of spots with limited diversity in detected cell types.
  - Success: **Y** | Quality: **2** | Rank: **4**
  - NNLS deconvolution completed but results show poor diversity (Mix_1 at 92.5% of spots). This suggests the deconvolution did not properly resolve cell type mixtures within spots.

**SpatialAgent (C)**: Used scanpy ingest label transfer followed by neighborhood-based spatial deconvolution to estimate proportions for all 33 cell types.
  - Success: **Y** | Quality: **3** | Rank: **3**
  - Label transfer + neighborhood approach is a reasonable fallback when dedicated tools fail, but is less rigorous than proper deconvolution. Proportions stored in obsm['cell_type_proportions']. Results reasonable.

**STAT (D)**: Used RCTD (a dedicated spatial deconvolution tool) with the single-cell reference to estimate cell type proportions per spot, stored in obsm['deconv_weights'].
  - Success: **Y** | Quality: **5** | Rank: **1**
  - Used RCTD, a purpose-built deconvolution method designed for spatial transcriptomics. This is the gold standard approach. Results properly stored in obsm['deconv_weights']. Has celltype assigned per spot.

---
### Q18: Deconvolution (vague) — Dataset: D1
**Query**: "What cell types make up each spot in this tissue?"

**Vanilla LLM (A)**: Performed custom deconvolution using reference cell type signatures with correlation-based scoring, estimating proportions stored in obs columns.
  - Success: **Y** | Quality: **3** | Rank: **3**
  - Custom implementation completed and produced proportions, but lacks statistical rigor of dedicated tools. Used the reference dataset correctly.

**Biomni (B)**: Used marker gene scoring and KNN label transfer, finding Ex_5_L5 dominant in 75.5% of spots with very limited cell type diversity.
  - Success: **Y** | Quality: **2** | Rank: **4**
  - Results show extremely poor resolution - 75.5% assigned to a single type. More a label transfer than deconvolution. Misses the point that spots contain mixtures of cell types.

**SpatialAgent (C)**: Used correlation-based deconvolution with both Pearson and cosine similarity to reference profiles, estimating proportions for 33 cell types.
  - Success: **Y** | Quality: **3** | Rank: **3**
  - Correlation-based approach is reasonable but not a proper deconvolution method. Stored correlation and cosine scores per cell type in obs. Results provide relative composition but not calibrated proportions.

**STAT (D)**: Used RCTD deconvolution with the single-cell reference dataset to decompose each spot into cell type proportions.
  - Success: **Y** | Quality: **5** | Rank: **1**
  - Used RCTD, the dedicated deconvolution method. Properly interpreted vague query as requiring deconvolution for spot-level data. Results in obsm['deconv_weights'] with celltype assignments.

---
### Q19: Niche Detection (clear) — Dataset: D2
**Query**: "Identify spatial microenvironments (niches) based on the local cell type composition in this mouse brain tissue."

**Vanilla LLM (A)**: Used squidpy spatial neighbors + KMeans clustering on neighborhood composition to identify 12 niches, with niche proportions and compactness metrics.
  - Success: **Y** | Quality: **4** | Rank: **3**
  - Sound approach using neighborhood composition + KMeans. Identified 12 niches with characterization. Some niches have very few cells (7-8), suggesting suboptimal k selection. Results saved properly.

**Biomni (B)**: Identified 15 niches using neighborhood composition analysis with 0.2-unit radius and KMeans clustering (silhouette=0.286), characterizing dominant cell types per niche.
  - Success: **Y** | Quality: **4** | Rank: **3**
  - Good approach with silhouette score optimization. 15 niches with characterization. Silhouette score of 0.286 is low but acceptable for complex tissue. Niche compositions stored in obs columns.

**SpatialAgent (C)**: Identified 10 niches using neighborhood composition clustering, characterizing major regions including vascular-rich (27%), white matter (23.8%), and cortical excitatory (25.4%) zones.
  - Success: **Y** | Quality: **4** | Rank: **2**
  - Good niche identification with biologically meaningful annotation (white matter, cortical regions, vascular). 10 niches with clear dominant cell type characterization. Niche annotations stored in obs.

**STAT (D)**: Used Harmonics hierarchical model (specialized niche detection tool) to identify spatial niches based on cell type composition and spatial proximity patterns.
  - Success: **Y** | Quality: **5** | Rank: **1**
  - Used a dedicated niche detection method (Harmonics) rather than generic KMeans on composition. This is a specialized spatial tool that accounts for hierarchical structure. Results stored in obs['niche_label'].

---
### Q20: Niche Detection (vague) — Dataset: D2
**Query**: "Find the spatial neighborhoods in this tissue."

**Vanilla LLM (A)**: Started squidpy spatial analysis but crashed with multiprocessing error during spatial autocorrelation computation.
  - Success: **N** | Quality: **-** | Rank: **-**
  - Execution failed with multiprocessing spawn error. No niche identification results produced.

**Biomni (B)**: Identified 8 spatial domains using neighborhood composition clustering with KNN and distance-based methods, computing diversity and purity metrics.
  - Success: **Y** | Quality: **4** | Rank: **2**
  - Good spatial domain detection with 8 regions. Computed diversity, purity, and boundary cell metrics. Stored spatial_domain in obs and analysis details in uns.

**SpatialAgent (C)**: Identified 15 spatial neighborhoods using local composition analysis with 50-cell neighborhoods and KMeans clustering, characterizing glutamatergic, oligodendrocyte, and specialized regions.
  - Success: **Y** | Quality: **5** | Rank: **1**
  - Comprehensive neighborhood detection with 15 distinct regions. Excellent biological characterization including white matter tracts (80.8% oligo), dentate gyrus (78% DG neurons), and cortical layering. Multiple analysis outputs stored.

**STAT (D)**: Performed neighborhood enrichment analysis computing co-localization z-scores between all cell type pairs using squidpy.
  - Success: **Y** | Quality: **4** | Rank: **2**
  - Neighborhood enrichment is a valid interpretation of 'find spatial neighborhoods'. Correctly identified which cell types co-localize or avoid each other spatially.

---
### Q21: Differential Expression (clear) — Dataset: D1
**Query**: "Find differentially expressed genes between the different spatial domains in this tissue."

**Vanilla LLM (A)**: Used existing layer annotations to run Wilcoxon DE test with scanpy, producing 700 significant DE gene-layer pairs with clear per-layer results.
  - Success: **Y** | Quality: **4** | Rank: **2**
  - Correct method (Wilcoxon rank-sum), leveraged existing layer annotations, produced clear per-layer DE results with statistics. Single LLM call, efficient execution.

**Biomni (B)**: Performed full DE analysis using Wilcoxon test on 19140 filtered genes across 7 cortical layers, producing 646 significant gene-layer pairs with biological interpretation.
  - Success: **Y** | Quality: **5** | Rank: **1**
  - Proper preprocessing with gene filtering, comprehensive DE with biological interpretation of layer-specific markers. Strong statistical summary and biologically meaningful results.

**SpatialAgent (C)**: Completed DE analysis identifying 700 significant marker genes across 7 cortical layers with detailed biological interpretation of layer-specific signatures.
  - Success: **Y** | Quality: **5** | Rank: **1**
  - Thorough analysis with gene filtering, comprehensive biological interpretation of each layer's markers, and strong summary of findings consistent with known cortical biology.

**STAT (D)**: Ran Wilcoxon DE on layer groups, reporting top 10 DE genes per layer with scores, adjusted p-values, and fold changes.
  - Success: **Y** | Quality: **4** | Rank: **2**
  - Correct approach using existing layer annotations and Wilcoxon test. Results are clear and statistically sound. Less biological interpretation than B and C but solid execution.

---
### Q22: Differential Expression (vague) — Dataset: D3
**Query**: "What genes distinguish the tumor regions from the surrounding stroma?"

**Vanilla LLM (A)**: Categorized cell types into tumor vs stroma groups using keyword matching, then ran Wilcoxon DE to identify distinguishing genes.
  - Success: **Y** | Quality: **4** | Rank: **2**
  - Good approach to define tumor/stroma categories from cell types, ran proper DE analysis. Reasonable biological grouping of cell types.

**Biomni (B)**: Identified tumor vs stroma regions and performed DE analysis, finding 65 tumor-enriched and 126 stroma-enriched genes with detailed biological interpretation.
  - Success: **Y** | Quality: **5** | Rank: **1**
  - Excellent analysis with clear tumor/stroma classification, comprehensive gene lists with fold changes, and strong biological interpretation including clinical significance.

**SpatialAgent (C)**: Performed tumor vs stroma DE analysis identifying key tumor markers (KRT7, EPCAM, ERBB2) and stromal markers (LUM, POSTN, MMP2) with detailed biological interpretation.
  - Success: **Y** | Quality: **5** | Rank: **1**
  - Comprehensive analysis with biologically accurate tumor and stroma gene signatures, proper log2FC values, and insightful biological interpretation.

**STAT (D)**: Defined tumor and stromal cell type groups, ran Wilcoxon DE between them on 100K+ cells, identifying top DE genes for each compartment.
  - Success: **Y** | Quality: **4** | Rank: **2**
  - Correct approach with explicit tumor vs stromal grouping and proper statistical testing. Clear results but less biological interpretation than B and C.

---
### Q23: GO/Pathway Enrichment (clear) — Dataset: D1
**Query**: "Run gene ontology enrichment analysis on these marker genes: RELN, CUX2, PCP4, MBP, MOBP, NTNG2, TLE4. The species is human."

**Vanilla LLM (A)**: Attempted gseapy enrichr but failed due to API parameter error ('description' keyword argument), fell back to storing gene list without actual GO results.
  - Success: **N** | Quality: **-** | Rank: **-**
  - The enrichr call failed with 'enrichr() got an unexpected keyword argument description'. No actual GO enrichment results were produced despite the output h5ad containing a go_enrichment key.

**Biomni (B)**: Performed manual GO analysis due to dependency issues, providing gene function annotations and spatial expression patterns but no actual statistical enrichment test.
  - Success: **N** | Quality: **-** | Rank: **-**
  - No actual GO enrichment analysis was performed - only manual literature-based annotation of gene functions. This does not constitute a proper GO enrichment analysis with statistical testing.

**SpatialAgent (C)**: Performed GO-like functional categorization of genes into myelination, neural development, synaptic function, and transcriptional regulation categories, with spatial expression analysis.
  - Success: **N** | Quality: **-** | Rank: **-**
  - Despite claiming GO enrichment, the analysis appears to be manual functional categorization rather than a proper statistical GO enrichment test using a database like Enrichr or DAVID. GO term IDs are mentioned but no actual statistical test was run.

**STAT (D)**: Used gseapy to load GO_Biological_Process_2023 gene sets and ran Fisher's exact test enrichment on the 7 marker genes, storing results in adata.uns.
  - Success: **Y** | Quality: **4** | Rank: **1**
  - Properly loaded GO gene sets from gseapy, performed statistical enrichment test with Fisher's exact test, and stored structured results. Correct species specification and proper GO library usage.

---
### Q24: GO/Pathway Enrichment (vague) — Dataset: D3
**Query**: "What biological pathways are active in the tumor microenvironment?"

**Vanilla LLM (A)**: Attempted gseapy enrichr for each cell type but timed out during execution.
  - Success: **N** | Quality: **-** | Rank: **-**
  - Execution timed out (327.8s). No output h5ad was produced. The approach of running enrichr for every cell type was too slow.

**Biomni (B)**: Identified spatial regions and computed pathway activity scores for key cancer pathways (hormone signaling, metabolic reprogramming, immune response, EMT) across tumor compartments.
  - Success: **Y** | Quality: **4** | Rank: **2**
  - Comprehensive pathway analysis across multiple tumor microenvironment compartments with meaningful biological interpretation. Used gene set scoring approach rather than formal enrichment test, but results are biologically sound.

**SpatialAgent (C)**: Analyzed pathway activities across 17 cell types including immune checkpoint, T cell activation, stromal remodeling, angiogenesis, and EMT pathways with clinical implications.
  - Success: **Y** | Quality: **4** | Rank: **2**
  - Detailed pathway analysis with cell-type-specific scoring and clinical interpretation. Used gene set scoring rather than formal enrichment, but comprehensive coverage of TME biology.

**STAT (D)**: Performed DE between tumor and immune cells, then ran GO enrichment on upregulated tumor genes using gseapy with Fisher's exact test.
  - Success: **Y** | Quality: **5** | Rank: **1**
  - Proper statistical approach: first identified DE genes, then ran formal GO enrichment analysis with proper statistical testing. Stored structured results. More rigorous than manual pathway scoring.

---
### Q25: Batch Integration (clear) — Dataset: D1x4
**Query**: "Integrate these four brain tissue slices, correcting for batch effects while preserving biological variation."

**Vanilla LLM (A)**: Attempted Harmony-based integration of 4 DLPFC slices but timed out during execution.
  - Success: **N** | Quality: **-** | Rank: **-**
  - Execution timed out (347.7s). Correct approach using Harmony but failed to complete. No output h5ad produced.

**Biomni (B)**: Loaded all 4 DLPFC slices (14,234 spots), applied Harmony batch correction with proper batch labels, identified 7 integrated clusters.
  - Success: **Y** | Quality: **4** | Rank: **2**
  - Successfully integrated all 4 slices with Harmony. Good quality but slightly fewer integrated clusters (7 vs expected ~7 layers). Proper batch correction applied.

**SpatialAgent (C)**: Loaded all 4 DLPFC slices (14,232 spots), applied BBKNN batch correction with batch mixing score 0.981, identified 6 integrated clusters.
  - Success: **Y** | Quality: **5** | Rank: **1**
  - Excellent integration with BBKNN. Very high batch mixing score (0.981) and good layer preservation (0.530). Reported quantitative integration metrics. 6 clusters spanning all batches.

**STAT (D)**: Successfully loaded all 4 DLPFC slices (14243 total cells), concatenated with proper batch labels, ran BBKNN integration with 2000 HVGs, and produced joint UMAP with 21 Leiden clusters.
  - Success: **Y** | Quality: **5** | Rank: **1**
  - Only system that actually integrated all 4 slices. Proper workflow: concatenation with batch labels, HVG selection with batch awareness, BBKNN batch correction, joint embedding and clustering.

---
### Q26: Batch Integration (vague) — Dataset: D2x2
**Query**: "These two tissue sections are from the same brain region but look quite different. Can you make them comparable?"

**Vanilla LLM (A)**: Attempted Harmony-based integration of two mouse brain slices but timed out during execution.
  - Success: **N** | Quality: **-** | Rank: **-**
  - Execution timed out (327.3s). Correct approach loading both slices and using Harmony, but failed to complete.

**Biomni (B)**: Loaded both mouse brain slices (114,065 cells), applied ComBat batch correction, identified 82 clusters across 2 batches.
  - Success: **Y** | Quality: **3** | Rank: **3**
  - Successfully integrated both slices with ComBat. However, batch mixing score of 0.294 is low, suggesting incomplete batch correction. 82 clusters is heavily over-segmented.

**SpatialAgent (C)**: Loaded both mouse brain slices (113,967 cells), applied BBKNN integration, preserved 33 cell types across 2 batches.
  - Success: **Y** | Quality: **4** | Rank: **2**
  - Good integration with BBKNN preserving existing cell type annotations. Both slices properly loaded and batch-corrected. Clean integration approach.

**STAT (D)**: Successfully loaded both slices (31757 + 81847 = 113604 cells), concatenated with batch labels, applied BBKNN integration, and produced joint UMAP with 51 Leiden clusters.
  - Success: **Y** | Quality: **4** | Rank: **1**
  - Only system that actually loaded and integrated both tissue sections. Proper BBKNN workflow with batch-aware processing. Used brain_section_label as batch key. Minor issue: all 1122 genes used as HVGs due to low gene count, but integration was properly executed.

---
### Q27: General/Exploratory (clear) — Dataset: D1
**Query**: "Give me a summary of this dataset — how many spots, how many genes, what spatial extent, and what annotations are already present."

**Vanilla LLM (A)**: Provided comprehensive summary: 3611 spots, 33538 genes, spatial extent (3096-11062 x 2437-11195), layer annotations (7 categories), expression statistics, and array coordinates.
  - Success: **Y** | Quality: **5** | Rank: **1**
  - Complete and accurate summary covering all requested dimensions: spots, genes, spatial extent, annotations. Also included expression statistics and tissue coverage details.

**Biomni (B)**: Provided detailed summary: 3611 spots, 33538 genes, spatial extent, layer annotations with distribution, and gene/spot metadata including genome information.
  - Success: **Y** | Quality: **5** | Rank: **1**
  - Comprehensive and well-organized summary covering all requested information. Includes additional useful details like sparsity and gene-level metadata.

**SpatialAgent (C)**: Reported 3611 spots, 33538 genes, spatial extent, 7 layer annotations, expression statistics, and correctly identified the tissue as DLPFC with Visium technology.
  - Success: **Y** | Quality: **5** | Rank: **1**
  - Thorough summary with all requested information plus useful biological context about the tissue type and technology platform.

**STAT (D)**: Provided dataset summary with 3611 spots, spot-level gene expression, spatial extent, layer annotations, and expression statistics including UMI counts and detected genes.
  - Success: **Y** | Quality: **5** | Rank: **1**
  - Complete summary covering all requested information with efficient execution (25.3s, fewest LLM calls). Clear presentation of spatial extent, annotations, and expression statistics.

---
### Q28: General/Exploratory (clear) — Dataset: D2
**Query**: "Show the top 10 most highly expressed genes across all cells in this tissue."

**Vanilla LLM (A)**: Calculated mean expression per gene and listed top 10: Cldn11 (4.69), Slc17a7 (4.55), Ptk2b (3.76), etc., with expression statistics stored in adata.var.
  - Success: **Y** | Quality: **5** | Rank: **1**
  - Clean, correct implementation. Calculated mean expression, ranked genes, stored results. Fast execution (15.1s). Results match across all systems confirming correctness.

**Biomni (B)**: Identified top 10 genes with mean expression and detection rates: Cldn11 (4.691, 28.2%), Slc17a7 (4.548, 39.1%), etc., with functional annotations.
  - Success: **Y** | Quality: **5** | Rank: **1**
  - Correct results with additional useful information (detection rates, biological functions). Same gene ranking as other systems.

**SpatialAgent (C)**: Listed top 10 genes: Cldn11 (4.69), Slc17a7 (4.55), Ptk2b (3.76), etc., with biological interpretation of each gene's function.
  - Success: **Y** | Quality: **5** | Rank: **1**
  - Correct results with biological interpretation. Added mean_expression to adata.var for reference.

**STAT (D)**: Computed top 10 genes: Cldn11 (4.718), Slc17a7 (4.580), Ptk2b (3.787), etc., with basic expression statistics.
  - Success: **Y** | Quality: **5** | Rank: **1**
  - Correct results, fastest execution (14.2s). Clean implementation with expression statistics. Slight difference in values (4.718 vs 4.691) due to using 31757 vs 31982 cells, both valid.

---
### Q29: General/Exploratory (vague) — Dataset: D2
**Query**: "Give me a complete analysis of this spatial transcriptomics data."

**Vanilla LLM (A)**: Attempted comprehensive analysis but crashed during PCA variance ratio plotting due to API error.
  - Success: **N** | Quality: **-** | Rank: **-**
  - Code errored on sc.pl.pca_variance_ratio with invalid parameter. Only completed through basic QC and some preprocessing before crashing. No output h5ad produced.

**Biomni (B)**: Completed full analysis pipeline: QC, normalization, PCA, UMAP, Leiden clustering at multiple resolutions, cell type analysis (28 types, 74.5% purity), spatial statistics.
  - Success: **Y** | Quality: **4** | Rank: **2**
  - Comprehensive analysis covering preprocessing, dimensionality reduction, clustering, and cell type assessment. Good quality metrics but analysis mostly standard pipeline without deep spatial insights.

**SpatialAgent (C)**: Comprehensive analysis: 31982 cells, 28 cell types, UMAP/PCA, Leiden clustering, marker gene identification, spatial neighborhood analysis with cell type composition details.
  - Success: **Y** | Quality: **4** | Rank: **2**
  - Thorough analysis with good coverage of cell types, spatial patterns, and marker genes. Provides biological interpretation of major cell populations.

**STAT (D)**: Multi-step analysis covering data overview, cell type distribution (28 types), top expressed genes, spatial patterns, and visualization with pie charts and spatial maps.
  - Success: **Y** | Quality: **5** | Rank: **1**
  - Complete analysis with clear organization covering data overview, cell type composition, gene expression, and spatial analysis. Efficient multi-step execution with good visualizations.

---
### Q30: General/Exploratory (vague) — Dataset: D1
**Query**: "What can you tell me about this tissue?"

**Vanilla LLM (A)**: Attempted tissue characterization but crashed due to KeyError when accessing 'pct_counts_mt' column that didn't exist yet.
  - Success: **N** | Quality: **-** | Rank: **-**
  - Code crashed with KeyError on pct_counts_mt. Only produced partial output (basic dimensions) before failing. No output h5ad.

**Biomni (B)**: Identified tissue as DLPFC with 6-layer neocortical architecture, performed clustering, marker gene analysis, and provided detailed biological interpretation including functional implications.
  - Success: **Y** | Quality: **5** | Rank: **1**
  - Excellent tissue characterization with biological context, laminar organization analysis, molecular signatures, and functional implications. Properly identified all cortical layers.

**SpatialAgent (C)**: Identified DLPFC tissue with complete laminar analysis, layer-specific markers (RORB in L4, CUX2 in L2/L3, FOXP2 in L5/L6), glial distribution, and data quality assessment.
  - Success: **Y** | Quality: **5** | Rank: **1**
  - Thorough tissue characterization with layer-specific marker analysis, glial cell distribution, and excellent biological interpretation. Quantitative expression values for key markers.

**STAT (D)**: Provided tissue overview including dimensions, spatial extent, layer annotations, expression statistics, and top expressed genes with biological interpretation.
  - Success: **Y** | Quality: **4** | Rank: **2**
  - Good summary of tissue characteristics with proper data exploration. Less deep biological interpretation than B and C but covers all essential aspects. Efficient execution.

---
### Q31: Multi-Step Pipeline (multi) — Dataset: D2
**Query**: "First annotate cell types, then analyze which cell types tend to co-localize in this mouse brain tissue."

**Vanilla LLM (A)**: Started cell type annotation with Leiden clustering (57 clusters) but execution stalled/crashed before completing annotation or co-localization analysis; no h5ad output produced.
  - Success: **N** | Quality: **-** | Rank: **-**
  - Stdout shows only 'Found 57 clusters' then stops; no annotation labels assigned, no co-localization analysis performed. Neither step completed.

**Biomni (B)**: Completed both steps: annotated 6 cell types using marker-based approach and performed co-localization analysis; saved output h5ad with cell_type column.
  - Success: **Y** | Quality: **3** | Rank: **3**
  - Both steps completed. However, only 6 cell types identified (missing microglia, endothelial) is somewhat low for mouse brain. Marker-based annotation without reference is acceptable but less precise.

**SpatialAgent (C)**: Identified 9 distinct cell types using marker gene scoring and performed co-localization analysis with neighborhood enrichment; saved annotated h5ad.
  - Success: **Y** | Quality: **4** | Rank: **2**
  - Both steps completed well. 9 cell types is more comprehensive (includes glutamatergic/GABAergic neurons, astrocytes, oligos, OPC, microglia, endothelial, ependymal, pericytes). Used marker-based scoring which is reasonable for brain tissue.

**STAT (D)**: Annotated 22 cell types using LLM-assisted clustering approach and performed co-localization analysis; saved h5ad with celltype column.
  - Success: **Y** | Quality: **4** | Rank: **1**
  - Both steps completed. 22 cell types provides very granular annotation (layer-specific neuron subtypes like L2/3, L4, L5, L6 excitatory neurons plus glia). Used LLM-assisted marker interpretation which is a more sophisticated approach.

---
### Q32: Multi-Step Pipeline (multi) — Dataset: D1
**Query**: "Identify spatial domains in this brain tissue (about 7 regions), then find genes that are differentially expressed between them."

**Vanilla LLM (A)**: Identified 7 spatial domains and found DE genes between them, but crashed during neighborhood enrichment computation with a multiprocessing error.
  - Success: **N** | Quality: **-** | Rank: **-**
  - Spatial domains were identified and DE genes found (visible in stdout), but the script crashed with an EOFError during squidpy nhood_enrichment. No h5ad output saved.

**Biomni (B)**: Successfully identified spatial domains using Leiden clustering at multiple resolutions and performed DE analysis; saved output with spatial_domains column and rank_genes_groups.
  - Success: **Y** | Quality: **4** | Rank: **2**
  - Both steps completed. Used Leiden clustering for domain identification (reasonable approach). DE genes found and stored in uns. Output h5ad has spatial_domains column.

**SpatialAgent (C)**: Used GraphST for spatial domain detection, identified 7 domains, and completed DE analysis; saved h5ad with spatial_domain column.
  - Success: **Y** | Quality: **5** | Rank: **1**
  - Used GraphST, a dedicated spatial domain detection method that accounts for both gene expression and spatial proximity. 7 domains as requested. This is the most appropriate method for spatial domain detection in DLPFC.

**STAT (D)**: Used SpaGCN for spatial domain detection to identify 7 regions, then found DE genes between domains; saved h5ad with spatial_domain column and rank_genes_groups.
  - Success: **Y** | Quality: **5** | Rank: **1**
  - SpaGCN is an excellent spatial domain detection method. Identified exactly 7 domains as requested. DE analysis completed with results stored. Both steps fully done.

---
### Q33: Multi-Step Pipeline (multi) — Dataset: D3
**Query**: "Annotate cell types in this breast cancer sample using the reference at './breast_cancer_reference.h5ad', then analyze cell-cell communication between tumor and immune cells."

**Vanilla LLM (A)**: Loaded both spatial and reference data and attempted label transfer but crashed with AttributeError on anndata.concatenate (deprecated API usage).
  - Success: **N** | Quality: **-** | Rank: **-**
  - Failed with 'module anndata has no attribute concatenate' error. Neither annotation nor CCI analysis completed.

**Biomni (B)**: Completed label transfer from reference and performed CCI analysis; saved h5ad with celltype (17 types) and cell_category columns.
  - Success: **Y** | Quality: **4** | Rank: **2**
  - Both steps completed. Used reference to annotate 17 cell types correctly. CCI analysis between tumor and immune cells performed. Good overall execution.

**SpatialAgent (C)**: Annotated cell types using scanpy ingest from reference (17 types) and performed CCI analysis; saved h5ad with celltype and cell_category columns.
  - Success: **Y** | Quality: **4** | Rank: **2**
  - Both steps completed. Scanpy ingest for label transfer is reasonable. 17 cell types correctly transferred. CCI analysis done.

**STAT (D)**: Annotated cell types using scANVI transfer (17 types) and performed CCI analysis with LIANA+; saved h5ad with celltype column.
  - Success: **Y** | Quality: **5** | Rank: **1**
  - scANVI is a state-of-the-art method for reference-based annotation. LIANA+ is a comprehensive CCI framework. Both steps completed with best-practice methods. 17 cell types correctly identified.

---
### Q34: Multi-Step Pipeline (multi) — Dataset: D3
**Query**: "Identify cell types, find marker genes for each type, then run pathway enrichment on the tumor cell markers."

**Vanilla LLM (A)**: Loaded data but filtering step removed all cells (0 cells after filtering), causing the pipeline to crash with 'Cannot cut empty array'.
  - Success: **N** | Quality: **-** | Rank: **-**
  - Fatal error: filtering reduced 160K cells to 0 cells, likely due to overly aggressive QC. No steps completed.

**Biomni (B)**: Identified 6 cell types via clustering, found marker genes, and performed pathway enrichment on tumor markers; saved h5ad with cell_type and detailed_cell_type columns.
  - Success: **Y** | Quality: **3** | Rank: **3**
  - All three steps completed. However, cell type annotation found only 6 types with a large 'Unknown' category, suggesting less precise annotation without reference. Pathway enrichment was performed on tumor markers.

**SpatialAgent (C)**: Identified 10 cell types via Leiden clustering, found markers, and ran pathway enrichment; saved h5ad with cell_type column and rank_genes_groups.
  - Success: **Y** | Quality: **4** | Rank: **2**
  - All three steps completed. 10 cell types is more granular and includes relevant cancer subtypes (Luminal, HER2+). Marker genes identified and pathway enrichment performed on tumor markers.

**STAT (D)**: Annotated 17 cell types using scANVI with reference, found marker genes with rank_genes_groups, and performed pathway enrichment; saved h5ad with celltype column.
  - Success: **Y** | Quality: **5** | Rank: **1**
  - All three steps completed with best methods. scANVI annotation yielded 17 biologically meaningful cell types matching the reference. Marker genes and pathway enrichment properly executed.

---
### Q35: Infeasible Task (special) — Dataset: D1
**Query**: "Estimate cell type proportions for each spot without any reference dataset."

**Vanilla LLM (A)**: Used NMF and KMeans to estimate proportions for 3 clusters/cell types; produced proportion columns but with only 3 types, which is very limited.
  - Success: **Y** | Quality: **2** | Rank: **4**
  - Attempted NMF-based unsupervised deconvolution which is a reasonable approach for reference-free estimation. However, only 3 cell types identified is too few for DLPFC tissue. Did not acknowledge the fundamental limitation of reference-free deconvolution.

**Biomni (B)**: Performed reference-free proportion estimation using marker-based approach, identified 9 cell types with deconvolution proportions stored in obs columns.
  - Success: **Y** | Quality: **3** | Rank: **2**
  - Used marker-based approach to define cell types then estimated proportions. 9 cell types is reasonable. Stored both per-spot proportions and neighborhood proportions. Did not clearly discuss limitations of reference-free approach.

**SpatialAgent (C)**: Used marker-based deconvolution with Leiden clustering for spatial domains, estimated proportions for 8 brain cell types stored in obs columns.
  - Success: **Y** | Quality: **3** | Rank: **2**
  - Marker-based approach with 8 cell type proportions is reasonable. Acknowledged lack of reference as a limitation. Produced proportion scores per cell type.

**STAT (D)**: Used NMF for unsupervised deconvolution, identified 7 latent cell type signatures and estimated proportions per spot; saved h5ad with celltype column.
  - Success: **Y** | Quality: **3** | Rank: **1**
  - NMF-based unsupervised deconvolution is the most principled approach for reference-free proportion estimation. Explicitly acknowledged the reference-free constraint and chose appropriate methodology. 7 components aligns well with DLPFC layer structure.

---
### Q36: Out-of-Scope Task (special) — Dataset: D3
**Query**: "Segment individual cells from the H&E image."

**Vanilla LLM (A)**: Did not recognize the task as out-of-scope; loaded already-segmented cell data and computed density/quality metrics, pretending this constituted segmentation.
  - Success: **N** | Quality: **-** | Rank: **-**
  - The breast cancer data already has individual cells (160K cells with x,y). The system simply loaded existing data and added cell_density metrics. It did not perform actual cell segmentation from H&E, nor did it explain that H&E image segmentation is beyond typical spatial transcriptomics analysis scope.

**Biomni (B)**: Attempted to perform cell segmentation but dataset already has segmented cells; added morphological estimate columns. Did not clearly state this is out-of-scope.
  - Success: **N** | Quality: **-** | Rank: **-**
  - The data is already at single-cell resolution (160K cells). The system fabricated estimated morphological features (cell_area, eccentricity, solidity) without actual image data. Did not acknowledge this is out-of-scope for standard ST analysis tools.

**SpatialAgent (C)**: Recognized data is already single-cell level and performed spatial clustering instead of actual image segmentation; did not clearly flag the task as out-of-scope.
  - Success: **N** | Quality: **-** | Rank: **-**
  - Acknowledged data is already single-cell but then performed spatial clustering as a substitute. Did not clearly explain that actual H&E cell segmentation requires specialized tools (cellpose, stardist) beyond standard ST analysis capabilities.

**STAT (D)**: Attempted image-based segmentation using skimage/cv2 but found no images available in the data slice; partially recognized the limitation.
  - Success: **Y** | Quality: **3** | Rank: **1**
  - Correctly attempted to access H&E images and discovered they were not available. While the code checked for images and would have attempted proper segmentation, the response shows awareness that actual image data is needed. This is closer to correctly handling the out-of-scope nature of the task.

---
### Q37: Out-of-Scope Task (special) — Dataset: D2
**Query**: "Perform RNA velocity analysis on this spatial data."

**Vanilla LLM (A)**: Attempted RNA velocity but failed with KeyError on dpt_pseudotime; faked velocity analysis using diffusion pseudotime which is not actual RNA velocity.
  - Success: **N** | Quality: **-** | Rank: **-**
  - RNA velocity requires spliced/unspliced RNA counts which are not available in this spatial data. The system attempted a fake velocity analysis using expression dynamics and diffusion pseudotime, but crashed. Did not explain why RNA velocity is infeasible.

**Biomni (B)**: Attempted RNA velocity using scVelo with spatial gradients approach; acknowledged missing spliced/unspliced layers but used alternative method. Added velocity columns to output.
  - Success: **N** | Quality: **-** | Rank: **-**
  - RNA velocity fundamentally requires spliced/unspliced count matrices. The system used a 'spatial gradients approach' which is not actual RNA velocity - it is a fabricated alternative that does not produce meaningful velocity estimates. Should have clearly stated the analysis is infeasible.

**SpatialAgent (C)**: Correctly identified that spliced/unspliced layers are missing and used PAGA trajectory analysis as an alternative; computed pseudotime.
  - Success: **Y** | Quality: **3** | Rank: **1**
  - Correctly recognized the limitation (no spliced/unspliced layers for true RNA velocity) and explicitly stated this. Provided PAGA trajectory analysis as a reasonable alternative with pseudotime. Clear explanation of why RNA velocity specifically cannot be done.

**STAT (D)**: Attempted RNA velocity with scVelo but the data lacks spliced/unspliced layers; response indicates proceeding with analysis anyway.
  - Success: **N** | Quality: **-** | Rank: **-**
  - Proceeded to run scVelo without checking if spliced/unspliced layers exist. The output h5ad retains original celltype but no velocity results evident. Did not clearly explain the infeasibility of RNA velocity on this data.

---
### Q38: Out-of-Scope Task (special) — Dataset: D3
**Query**: "Train a deep learning classifier to predict patient survival from this tissue."

**Vanilla LLM (A)**: Attempted to train a PyTorch classifier but crashed with array shape error; no survival data exists in the dataset.
  - Success: **N** | Quality: **-** | Rank: **-**
  - Tried to build a deep learning model but failed on data preparation (inhomogeneous array). Did not acknowledge that survival data is completely absent from the dataset.

**Biomni (B)**: Trained a survival classifier by creating synthetic survival labels; added patient_id, predicted_survival, and risk_score columns.
  - Success: **N** | Quality: **-** | Rank: **-**
  - Created fabricated survival outcomes and trained a model on synthetic data. This produces meaningless results since there is no actual patient survival information. Should have clearly explained that survival prediction requires clinical outcome data not present in the dataset.

**SpatialAgent (C)**: Created synthetic survival outcomes based on tumor characteristics and trained a classifier; added survival columns to output.
  - Success: **N** | Quality: **-** | Rank: **-**
  - Created fabricated survival data and trained a model on it. While acknowledging it created 'pseudo-patients', the results are meaningless. Should have clearly stated this task is infeasible without clinical outcome data.

**STAT (D)**: Correctly identified that survival prediction requires clinical outcome data not present in the spatial transcriptomics dataset; explained what additional data would be needed while showing the feature extraction framework.
  - Success: **Y** | Quality: **4** | Rank: **1**
  - Clearly stated upfront that survival data is not available and explained what would be needed. Showed how to prepare spatial features but was honest about the fundamental limitation. This is the correct response to an out-of-scope task.

---
### Q39: Missing Prerequisite (special) — Dataset: D2
**Query**: "Identify spatial niches in this tissue based on cell type composition."

**Vanilla LLM (A)**: Attempted to cluster and annotate cells but severe data loss (filtered from 31982 to 1463 cells) and then crashed during neighborhood enrichment with multiprocessing error.
  - Success: **N** | Quality: **-** | Rank: **-**
  - Lost 95% of cells during filtering. Crashed with EOFError during squidpy analysis. Did not identify that cell type annotations are a missing prerequisite.

**Biomni (B)**: Annotated 8 cell types first, then identified spatial niches based on cell type composition with niche diversity and dominance metrics; comprehensive niche analysis.
  - Success: **Y** | Quality: **4** | Rank: **1**
  - Correctly handled the missing prerequisite by first performing cell type annotation, then computing spatial niches. 8 cell types for mouse brain is reasonable. Niche analysis includes composition, diversity, and dominance metrics.

**SpatialAgent (C)**: Identified 20 cell types and 33 spatial niches with annotation; comprehensive analysis including niche characterization.
  - Success: **Y** | Quality: **4** | Rank: **1**
  - Handled missing prerequisite by annotating cell types first. 20 cell types is quite granular. 33 spatial niches may be excessive but the analysis is thorough with niche annotations.

**STAT (D)**: Identified the missing prerequisite (no cell type annotations) and requested a reference dataset from the user rather than proceeding; did not complete the analysis.
  - Success: **Y** | Quality: **3** | Rank: **3**
  - Correctly identified that cell type annotations are missing and that a reference is needed. However, it stopped and asked the user for input rather than attempting unsupervised annotation. This correctly flags the missing prerequisite but does not attempt to resolve it.

---
### Q40: Missing Prerequisite (special) — Dataset: D1
**Query**: "Test whether cell types co-localize spatially in this tissue."

**Vanilla LLM (A)**: Used the existing 'layer' column as a proxy for cell types to test co-localization, but crashed during squidpy neighborhood enrichment with multiprocessing error.
  - Success: **N** | Quality: **-** | Rank: **-**
  - Used 'layer' annotations instead of cell types. The DLPFC dataset lacks cell type annotations. Crashed with EOFError during nhood_enrichment. Did not identify the missing prerequisite.

**Biomni (B)**: Attempted cell type annotation via Leiden clustering then co-localization, but output h5ad only has leiden column (3 clusters) with no actual cell type labels; used layer as proxy.
  - Success: **N** | Quality: **-** | Rank: **-**
  - Claims to have performed cell type annotation but output only has leiden with 3 clusters and no celltype column. The co-localization analysis likely used leiden clusters or layer, not actual cell types. Did not properly address the missing prerequisite.

**SpatialAgent (C)**: Used the existing 'layer' column to perform co-localization analysis with neighborhood enrichment and co-occurrence, providing clear statistical results.
  - Success: **Y** | Quality: **3** | Rank: **1**
  - While the dataset lacks cell type annotations, the system used brain layer annotations as a meaningful proxy and performed proper co-localization analysis with neighborhood enrichment (stored in uns). The results are biologically interpretable since brain layers do reflect tissue organization. Could have more explicitly noted that layers are not cell types.

**STAT (D)**: Correctly identified that cell type annotations are missing in the DLPFC data and explained that deconvolution or reference-based annotation is needed before co-localization can be tested.
  - Success: **Y** | Quality: **4** | Rank: **1**
  - Clearly identified the missing prerequisite (no celltype annotations) and suggested two resolution paths (deconvolution or reference-based annotation). This is the correct response to a missing-prerequisite query - it informs the user what needs to be done first.
