# miRNA qPCR Reanalysis — Consolidated Analytical Report

## Executive summary

This report consolidates the completed notebook-native reanalysis of the salivary miRNA qPCR periodontal dataset (`n=108`; balanced groups: `S=36`, `G=36`, `P=36`). The analytical workflow was executed end-to-end with explicit logs for assumptions, discrepancies, transformations, and results.

Key high-level findings:

- Strong task-level discrimination exists for fixed tasks (`S vs G`, `G vs P`, `S vs P`) under leakage-safe nested CV.
- Reference-gene behavior (`mean_GAPDH`) is **not stable across groups**, and is strongly associated with demographic/clinical variables; this materially affects interpretation of normalization-dependent claims.
- Broader/global Ct proxies alone achieved high to near-perfect discrimination for some tasks, indicating that strong classification performance is not automatically evidence of disease-specific marker biology.
- Single-marker and small-panel results are informative but panel search outputs remain exploratory by design.

---

## Analysis order and rationale

The report follows a dependency-aware order so each section provides prerequisites for the next:

1. **Data integrity and transformation readiness first** to establish trustworthy inputs and explicit derived-variable definitions.
2. **Descriptive/inferential group comparisons second** to identify where differences exist before predictive modeling.
3. **Reference-gene and clinical association audits third** to challenge normalization assumptions and test broader explanatory pathways.
4. **Leakage-safe classification analyses fourth** to quantify discrimination with robust validation controls.
5. **Model-family comparisons and confounding/global checks fifth** to evaluate whether biomarker claims persist after broader alternatives.
6. **Robustness and sensitivity analyses sixth** to stress-test strong internal performance.
7. **Results registry and completion mapping last** to tie claims to outputs and document implementation completeness.

This sequence ensures a coherent narrative from data reliability → statistical signal → mechanistic caution → validated prediction → robustness-informed interpretation.

---

## Detailed analyses

### 1) Data loading, validation, discrepancy handling, and transformation registry

**Purpose**
To verify schema integrity, confirm fixed-group/task feasibility, and produce explicit, auditable derived variables required by the workflow.

**Method overview**
- Loaded `miRNA-qPCR-analysis-results.csv` and validated shape, missingness, duplicates, and category levels.
- Confirmed fixed groups (`S`, `G`, `P`) are present exactly.
- Created discrepancy log for unavailable requested global variables and generated explicit proxies:
  - `global_mean_ct_all7_proxy`
  - `global_mean_ct_miRNA_only_proxy`
- Computed `dct_*` and `abd_*` variables from `mean_*` and `mean_GAPDH`.

**Results**

| Metric | Value |
|---|---:|
| Rows | 108 |
| Columns | 15 |
| Missing values | 0 across all columns |
| Duplicate rows | 0 |
| Group counts | S: 36, G: 36, P: 36 |

| Discrepancy | Status | Resolution |
|---|---|---|
| `global_mean_ct_all7` | Not in CSV | Used `global_mean_ct_all7_proxy` (documented) |
| `global_mean_ct_miRNA_only` | Not in CSV | Used `global_mean_ct_miRNA_only_proxy` (documented) |

**Figures (filename only)**
- `eda_miRNA_ct_boxplots.png`

**Interpretation and key takeaways**
Data quality is structurally strong (no missingness or duplicates), and transformations are fully auditable. The main caveat is that broader/global Ct variables are proxy-derived due to absent original fields.

**Insights/observations**
- Balanced group sizes reduce class-imbalance artifacts in pairwise tasks.
- Proxy use is a methodological limitation, but was implemented transparently and tracked.

---

### 2) Baseline and miRNA group-comparison inferential analyses

**Purpose**
To quantify whether marker and derived-variable distributions differ across fixed pairwise tasks before model fitting.

**Method overview**
- Task-wise pairwise tests for `S vs G`, `G vs P`, `S vs P`.
- Primary nonparametric test: Mann–Whitney U (`mw_p`, FDR-adjusted `mw_q_fdr`).
- Secondary Welch t-test provided as sensitivity.

**Results**

**Representative significant findings (FDR-adjusted):**

| Task | Variable | Median diff (Group2 - Group1) | mw_p | mw_q_fdr | FDR significant |
|---|---|---:|---:|---:|---|
| S vs G | `mean_mir146b` | -0.1033 | 0.0109 | 0.0272 | Yes |
| S vs G | `dct_mir146b` | -0.5000 | 0.00012 | 0.00148 | Yes |
| G vs P | `mean_mir203` | -6.7967 | 2.28e-07 | 3.79e-07 | Yes |
| G vs P | `mean_GAPDH` | -5.2950 | 7.24e-10 | 1.09e-08 | Yes |
| S vs P | `mean_mir203` | -6.7800 | 3.04e-13 | 5.08e-13 | Yes |
| S vs P | `global_mean_ct_all7_proxy` | -6.3533 | 3.05e-13 | 5.08e-13 | Yes |

**Figures (filename only)**
- `eda_miRNA_ct_boxplots.png`

**Interpretation and key takeaways**
Large contrasts are most pronounced in tasks involving `P`. Significant effects in both biomarker and broader/global proxy variables suggest strong separation but not necessarily marker-specific etiology.

**Insights/observations**
- `S vs G` is the hardest discrimination task in both univariate and multivariate contexts.
- `S vs P` exhibits extremely strong separability requiring cautious interpretation (possible broader process effects).

---

### 3) Reference-gene and normalization audit (`mean_GAPDH`)

**Purpose**
To test whether reference-gene behavior is stable enough to support straightforward normalization claims.

**Method overview**
- Compared `mean_GAPDH` across groups (Kruskal–Wallis + one-way ANOVA).
- Tested Spearman associations with age and clinical variables.

**Results**

| Group | GAPDH mean | GAPDH SD | Median | Min | Max |
|---|---:|---:|---:|---:|---:|
| G | 35.9052 | 2.0178 | 36.7417 | 31.0600 | 37.7300 |
| P | 31.3879 | 0.3731 | 31.4467 | 30.4767 | 32.1133 |
| S | 36.4922 | 0.4691 | 36.6800 | 35.5800 | 37.0600 |

| Test | p-value |
|---|---:|
| Kruskal–Wallis (GROUP effect on GAPDH) | 6.55e-14 |
| One-way ANOVA (GROUP effect on GAPDH) | 1.25e-35 |

| Covariate | Spearman r with GAPDH | p-value |
|---|---:|---:|
| AGE | -0.5409 | 1.51e-09 |
| plaque_index | -0.5233 | 6.20e-09 |
| gingival_index | -0.4722 | 2.47e-07 |
| pocket_depth | -0.6187 | 9.64e-13 |
| bleeding_on_probing | -0.5660 | 1.74e-10 |
| number_of_missing_teeth | -0.3265 | 5.63e-04 |

**Figures (filename only)**
- `gapdh_group_distribution.png`

**Interpretation and key takeaways**
Reference-gene behavior is strongly group- and covariate-associated, so normalization choices can materially shift interpretation. GAPDH is not behaving as a flat nuisance factor in this dataset.

**Insights/observations**
- This directly supports caution against interpreting normalized contrasts as purely disease-specific.
- It also explains why broader/global summaries can compete with biomarker-specific models.

---

### 4) Clinical correlation analyses (marker-clinical relationships)

**Purpose**
To quantify alignment between miRNA-derived features and periodontal clinical burden.

**Method overview**
- Spearman correlations (`marker` × `clinical variable`) with FDR correction.
- Age-adjusted linear models for clinical predictors as sensitivity analysis.

**Results**

**Top Spearman (FDR-adjusted) examples:**

| Marker | Clinical variable | Spearman r | q (FDR) | Significant |
|---|---|---:|---:|---|
| abd_mir203 | bleeding_on_probing | 0.7083 | 2.17e-16 | Yes |
| abd_mir155 | bleeding_on_probing | 0.7059 | 2.17e-16 | Yes |
| abd_mir146b | bleeding_on_probing | 0.6664 | 2.64e-14 | Yes |
| abd_mir381p | plaque_index | 0.6530 | 8.02e-14 | Yes |
| abd_mir146a | pocket_depth | 0.4991 | 4.80e-08 | Yes |
| abd_mir146a | number_of_missing_teeth | 0.0948 | 0.3289 | No |

**Age-adjusted model examples:**

| Marker | Clinical variable | Beta (adj AGE) | p | q (FDR) | Significant |
|---|---|---:|---:|---:|---|
| abd_mir203 | plaque_index | 0.7811 | 3.30e-11 | 3.30e-10 | Yes |
| abd_mir223 | plaque_index | 0.8239 | 1.90e-10 | 9.21e-10 | Yes |
| abd_mir381p | pocket_depth | 0.5914 | 2.21e-08 | 3.69e-08 | Yes |
| abd_mir146a | number_of_missing_teeth | -0.0695 | 0.3486 | 0.4183 | No |

**Figures (filename only)**
- `clinical_correlation_heatmap.png`

**Interpretation and key takeaways**
Marker-derived features are strongly aligned with multiple clinical severity indices; however, this coherence does not by itself disambiguate causal direction or specificity versus broader inflammatory biology.

**Insights/observations**
- Bleeding/plaque/gingival metrics are consistently high-signal across many markers.
- Missing-teeth associations are weaker and less consistent.

---

### 5) Leakage-safe fixed pairwise classification (core predictive analysis)

**Purpose**
To quantify discriminative performance for fixed tasks under explicit leakage controls.

**Method overview**
- Fixed tasks: `S vs G`, `G vs P`, `S vs P`.
- Nested CV with fold-contained preprocessing/selection/tuning.
- Model families: single marker, small exploratory panel, demographic-only, biomarker+demographic, broader/global-only, combined.
- OOF-based performance summaries.

**Results**

**Best AUC by task (all model families):**

| Task | Best model family | Best model label | AUC | Accuracy | Sensitivity | Specificity |
|---|---|---|---:|---:|---:|---:|
| S vs G | single_marker | abd_mir146b | 0.7616 | 0.6667 | 0.6944 | 0.6389 |
| G vs P | combined_model | ABD+Proxy+Demo_select7 | 0.9977 | 0.9583 | 1.0000 | 0.9167 |
| S vs P | broader_global_only / combined_model | global proxies / combined | 1.0000 | 1.0000 / 0.9861 | 1.0000 / 0.9722 | 1.0000 |

**Figures (filename only)**
- `model_family_auc_comparison.png`

**Interpretation and key takeaways**
Predictive signal is strongest when periodontitis is one class. However, near-perfect internal performance—especially where broader/global-only models perform equivalently—requires high interpretive caution.

**Insights/observations**
- `S vs G` remains the limiting clinical boundary.
- Performance parity between broader/global-only and combined models in `S vs P` suggests strong shared/global signal.

---

### 6) Single-marker versus exploratory panel comparison

**Purpose**
To test whether small marker panels improve over single-marker performance and to label search-based results appropriately.

**Method overview**
- Compared single-marker models to constrained pairwise panels formed from top univariate candidates.
- Labeled panel search as exploratory.

**Results**

| Task | Family | Max AUC | Median AUC | Mean AUC | Models tested |
|---|---|---:|---:|---:|---:|
| S vs G | single_marker | 0.7616 | 0.7284 | 0.7137 | 6 |
| S vs G | small_panel_exploratory | 0.7423 | 0.7407 | 0.7410 | 3 |
| G vs P | single_marker | 0.8410 | 0.8121 | 0.7982 | 6 |
| G vs P | small_panel_exploratory | 0.8480 | 0.8434 | 0.8387 | 3 |
| S vs P | single_marker | 0.9923 | 0.9456 | 0.9501 | 6 |
| S vs P | small_panel_exploratory | 1.0000 | 0.9931 | 0.9943 | 3 |

**Figures (filename only)**
- `model_family_auc_comparison.png`

**Interpretation and key takeaways**
Panels can improve or stabilize AUC in some tasks, but because combinations were searched, these gains are exploratory until externally validated.

**Insights/observations**
- The largest panel benefit appears in harder boundaries (`S vs G`, `G vs P`) but remains modest.
- In `S vs P`, both markers and broader/global signal are already extremely strong.

---

### 7) Confounding/covariate adjustment and broader/global structure checks

**Purpose**
To determine whether biomarker performance persists beyond demographic and global-signal alternatives.

**Method overview**
- Contrasted demographic-only, biomarker+demographic, broader/global-only, and combined families by task.

**Results**

| Task | Demographic-only AUC | Biomarker+demographic AUC | Broader/global-only AUC | Combined AUC |
|---|---:|---:|---:|---:|
| S vs G | 0.6231 | 0.7307 | 0.5965 | 0.7323 |
| G vs P | 0.9742 | 0.9660 | 0.8534 | 0.9977 |
| S vs P | 0.8005 | 0.9938 | 1.0000 | 1.0000 |

**Figures (filename only)**
- `broader_global_proxy_distributions.png`
- `model_family_auc_comparison.png`

**Interpretation and key takeaways**
Broader/global and demographic pathways explain substantial discrimination in some contrasts, particularly severe separation contexts, reducing confidence in strictly marker-specific explanations.

**Insights/observations**
- Very strong demographic-only performance in `G vs P` indicates age/sex structure is nontrivial.
- In `S vs P`, broader/global-only can match top combined performance.

---

### 8) Robustness and sensitivity analyses

**Purpose**
To stress-test high internal performance and quantify uncertainty.

**Method overview**
- Bootstrap CIs for best single-marker AUC per task (`n_boot=300`).
- Permutation-style null check for representative strong model (`Task3`, combined).

**Results**

| Task | Marker | Bootstrap median AUC | 95% CI low | 95% CI high |
|---|---|---:|---:|---:|
| S vs G | abd_mir146b | 0.7628 | 0.6722 | 0.8705 |
| G vs P | abd_mir203 | 0.8511 | 0.7279 | 0.9473 |
| S vs P | abd_mir203 | 0.9969 | 0.9860 | 1.0000 |

| Task | Model | Observed AUC | Permutations | Permutation p-value |
|---|---|---:|---:|---:|
| S vs P | combined_model | 1.0000 | 50 | 0.0196 |

**Figures (filename only)**
- `exploratory_pca_multiclass.png`
- `exploratory_pca_variance.csv` (table artifact)

**Interpretation and key takeaways**
Strong findings remain statistically unusual under permutation for the representative task/model, but this does not eliminate risks of dataset-specific structure or over-optimism without external validation.

**Insights/observations**
- Uncertainty is widest where class boundaries are weaker (`S vs G`).
- Near-perfect `S vs P` still demands conservative narrative framing.

---

### 9) Results registry and completion mapping

**Purpose**
To make claims auditable and verify directive-level completion.

**Method overview**
- Generated `results_registry.csv` from top model outputs.
- Generated `completion_map.csv` against workflow directives.

**Results**

| Result_ID | Claim summary | Inference label |
|---|---|---|
| R1 | Task1_S_vs_G single_marker AUC=0.762, Accuracy=0.667 | Exploratory |
| R3 | Task2_G_vs_P combined_model AUC=0.998, Accuracy=0.958 | Stronger internal inference |
| R5 | Task3_S_vs_P small_panel_exploratory AUC=1.000, Accuracy=1.000 | Exploratory |
| R6 | Task3_S_vs_P broader_global_only AUC=1.000, Accuracy=1.000 | Stronger internal inference |

| Completion item | Status |
|---|---|
| Fixed pairwise leakage-safe classification | Completed |
| Reference-gene audit | Completed |
| Clinical correlations | Completed |
| Robustness and sensitivity analyses | Completed (bounded permutation count for runtime) |
| Final synthesis + confidence/caution split | Completed |

**Figures (filename only)**
- (Registry/completion are table-first sections)

**Interpretation and key takeaways**
The final output is traceable and implementation-complete relative to declared directives, with explicit caveat tracking for exploratory and proxy-dependent components.

**Insights/observations**
- The completion map enables rapid audit and reproducibility review.
- Registry labels help prevent overclaiming in downstream communication.

---

## Cross-analysis insights

1. **Signal strength is task-dependent.** The largest contrast is consistently `S vs P`; `S vs G` remains substantially harder.
2. **Broader/global signal is consequential.** Proxy global Ct variables can rival combined models in severe-separation tasks.
3. **Reference-gene variability is non-negligible.** GAPDH has strong group and covariate associations, which limits simplistic normalization narratives.
4. **Clinical alignment is strong but not necessarily specific.** Many markers correlate robustly with clinical burden; this supports biological relevance but not exclusivity.
5. **Leakage-safe design matters.** OOF nested-CV estimates provide stronger internal validity than in-sample or prefiltered pipelines.
6. **Exploratory outputs are clearly delineated.** Panel-search improvements are useful but remain exploratory pending external replication.

---

## Overall findings and conclusions

This reanalysis provides strong internal evidence of discriminative structure across periodontal states, especially when periodontitis is one class. However, the same analyses show that global signal and covariate structure can explain a substantial portion of separation, and reference-gene behavior is not neutral.

Therefore:

- **Confidently supported:** reproducible internal discrimination and robust marker-clinical associations within this dataset.
- **Supported cautiously:** disease-specific biomarker claims beyond broader/global effects, panel superiority after search, and any translational threshold claims without external validation.

In summary, the dataset is highly informative for internal stratification patterns but should be interpreted conservatively for specificity and external generalization.
