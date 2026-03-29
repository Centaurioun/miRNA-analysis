# Session Statistical Review Reproduction

## 1. Executive summary

This delivery package documents the statistical review session performed on the salivary miRNA periodontal qPCR analysis workflow. The final notebook for this session is:

- `session_statistical_review_reproduction_2026-03-28.ipynb`

The purpose of the session was not to rerun the entire biological workflow blindly, but to stress-test the notebook’s strongest statistical conclusions and determine which claims were secure, which needed wording changes, and which required additional or repeated analysis.

Main outcomes:

- The notebook’s screening and leakage-safe classification framework is broadly defensible.
- The strongest limitation is severe instability of `mean_GAPDH` across groups and across severity-linked clinical variables.
- The strongest internal classification results for `Task2_G_vs_P` and `Task3_S_vs_P` remain real as within-dataset separation findings, but they are not securely interpretable as uniquely biomarker-specific.
- The current clinical-correlation claims do not remain convincing after stronger adjustment for `GROUP`, `AGE`, `mean_GAPDH`, and broader/global Ct structure.
- The final closeout judgment from this session is:
  - the notebook is usable after targeted revision
  - the statistical review is not fully complete until the stronger-adjusted clinical-correlation section is rerun inside the main notebook

## 2. Context and objectives

### Project context

This repository contains a notebook-centered reanalysis of a salivary miRNA periodontal qPCR dataset with fixed groups and tasks:

- `S` = Healthy
- `G` = Gingivitis
- `P` = Periodontitis

Pairwise tasks:

- `Task1` = `S` vs `G`
- `Task2` = `G` vs `P`
- `Task3` = `S` vs `P`

The main project notebook remains:

- `miRNA_qpcr_reanalysis.ipynb`

This session-specific notebook is a separate audit/reproduction artifact focused on validating the statistical interpretation layer.

### Session objectives

The statistical review session addressed these questions:

1. Is the notebook’s univariate inferential framework acceptable for screening?
2. Does instability in `mean_GAPDH` materially threaten normalization-dependent claims?
3. Do normalized biomarker models add anything once explicit GAPDH/global structure is included?
4. Do raw `mean_miR*` Ct features add anything once the full control block is included?
5. What is actually driving the strongest `Task2` and `Task3` discrimination?
6. Do the notebook’s clinical-correlation claims survive stronger adjustment?
7. What is the final claim-by-claim statistical adjudication for the notebook?

### Why these questions mattered

These questions mattered because the original notebook contained very strong internal discrimination results and multiple normalization-dependent interpretations. In a qPCR setting, strong results are only useful if the reference signal is stable enough and if separation is not being driven mostly by broader/global structure, demographics, or denominator behavior.

## 3. Data and methodology

### Data sources used

The session notebook used:

- `miRNA-qPCR-analysis-results.csv`
- `miRNA-qPCR-reanalysis.md`
- existing exported notebook outputs under `outputs/`
- saved session review outputs under `outputs/session-statistical-review/`

Key exported files referenced by the session notebook included:

- `taskwise_inferential_tests.csv`
- `gapdh_audit_tests.csv`
- `gapdh_group_summary.csv`
- `gapdh_covariate_associations.csv`
- `clinical_correlations_spearman.csv`
- `clinical_correlations_age_adjusted.csv`
- `task_model_performance_nestedcv.csv`
- `confounding_and_broader_comparisons.csv`
- `permutation_check_task3_combined.csv`
- `results_registry.csv`

### Preprocessing and derived variables

The session notebook transparently rebuilt the same core derived variables used during the review:

- `dct_mir* = mean_miR* - mean_GAPDH`
- `abd_mir* = -1 * dct_mir*`
- `global_mean_ct_all7_proxy`
- `global_mean_ct_miRNA_only_proxy`

For the stronger clinical-correlation reassessment, it also used a leave-one-out broader/global miRNA Ct proxy for each tested marker to reduce direct self-inclusion and avoid the most obvious collinearity problem.

### Analyses performed

The notebook is organized into `q01` through `q09`, which reproduce the session analyses in sequence:

1. `q01` foundational master audit
2. `q02` GAPDH/reference-gene stress test
3. `q03` normalized biomarker incremental-value analysis
4. `q04` revised Task2/Task3 interpretation text
5. `q05` raw `mean_miR*` incremental-value analysis
6. `q06` control-block ablation for `Task2` and `Task3`
7. `q07` Task2 control-block stability analysis
8. `q08` stronger clinical-correlation reassessment
9. `q09` final closeout adjudication and revision checklist

### Why these methods were selected

- **Mann-Whitney and Welch testing context**: retained because the original notebook used them appropriately for screening in balanced pairwise comparisons.
- **OLS regression**: used for GAPDH modeling and the stronger clinical-correlation reassessment because the outcomes under review there were continuous.
- **Leakage-safe nested logistic regression**: used for the discrimination analyses because the session’s core question was not just association but out-of-fold discriminative value under defensible validation.
- **Bootstrap AUC-difference summaries**: used to evaluate whether model differences were materially meaningful rather than relying only on point estimates.
- **Ablation analysis**: used to determine which components of the control block mattered most once raw and normalized biomarker increment had already been tested.
- **Repeated resampling stability analysis**: used in `q07` because collinearity inside the Task2 control block made single-model interpretation too brittle.

### How the analyses were executed

The notebook was structured as an auditable, top-to-bottom review artifact. Each major section includes:

- a heading stating the analytical purpose
- visible code
- saved output tables
- explanatory markdown for interpretation

The notebook writes reproduced review outputs to:

- `outputs/session-statistical-review/`

## 4. Results and interpretation

### q01. Master audit

Key finding:

- The notebook is directionally credible but not fully confirmed as originally framed.

Interpretation:

- The screening framework is acceptable.
- The main problems are not basic inferential syntax or obvious leakage errors.
- The main problems are interpretation-layer problems, especially normalization dependence and over-attribution of strong separation to biomarker-specific signal.

### q02. GAPDH/reference-gene stress test

Key result:

- `mean_GAPDH` is severely unstable across groups and strongly linked to severity-related structure.

Important reproduced outputs:

- `group_only R² = 0.783644`
- `clinical_only R² = 0.710823`
- GAPDH task AUCs:
  - `Task1 = 0.545139`
  - `Task2 = 0.922454`
  - `Task3 = 1.000000`

Interpretation:

- GAPDH is not acting like a neutral housekeeping denominator in this dataset.
- This materially weakens the interpretability of `dct_*` and `abd_*` variables as clean marker-specific abundance proxies.

### q03. Normalized biomarker increment over explicit GAPDH/global structure

Key result:

- The normalized biomarker block does not provide meaningful incremental value once explicit GAPDH/global structure is included.

Important reproduced outputs:

- `Task2 structure_only AUC = 0.962963`
- `Task2 biomarker_plus_structure AUC = 0.904321`
- `Task2 delta median = -0.057841`
- `Task3 structure_only AUC = 1.000000`
- `Task3 biomarker_plus_structure AUC = 1.000000`

Interpretation:

- The strongest normalized biomarker claims for `Task2` and `Task3` should be downgraded.
- Especially for `Task3`, the perfect internal discrimination is already fully captured by structure-only variables.

### q05. Raw mean_miR* increment over the full control block

Key result:

- Raw `mean_miR*` features also do not provide meaningfully useful incremental value over the full control block.

Important reproduced outputs:

- `Task2 control_only AUC = 0.998457`
- `Task2 raw_mirna_plus_control AUC = 1.000000`
- `Task2 delta median = 0.000777`

Interpretation:

- Even when bypassing the normalized `abd_*` representation, the session still does not recover convincing incremental biomarker-block value.
- The gain is numerically positive in the rebuilt notebook but too small to change the conclusion.

### q06 and q07. What is actually driving Task2?

Key result:

- `q06` in the rebuilt notebook suggests that removing the broader/global proxy block can reduce performance.
- `q07` provides the more stable interpretation:
  - `AGE` is the most stable unique contributor
  - the proxy family is not the uniquely dominant driver
  - `mean_GAPDH` plus the proxy block behave like a redundant structure-related signal

Important reproduced outputs from `q07`:

- `AGE most_harmful_fraction = 0.96`
- `mean_GAPDH most_harmful_fraction = 0.04`

Interpretation:

- The correct closeout reading is not “Task2 is explained only by proxy structure.”
- The safer interpretation is:
  - Task2 reflects strong within-dataset discrimination driven by age plus redundant reference/global structure
  - it should not be framed as a uniquely biomarker-specific panel effect

### q08. Stronger clinical-correlation reassessment

Key result:

- The original clinical-correlation claims do not survive stronger adjustment.

Important reproduced outputs:

- all `abd_*` associations were classified as `mostly_group_or_structure_driven`
- all raw `mean_miR*` associations were classified as `mostly_group_or_structure_driven`

Interpretation:

- The earlier clinical-correlation section in the main notebook is too strong as currently written.
- These associations appear to be driven mainly by group structure, reference behavior, and broader/global Ct structure rather than robust marker-specific clinical relationships.

### q09. Final closeout adjudication

The notebook’s final claim classification in this session was:

- **Confirmed**
  - screening framework
  - leakage-safe classification setup
  - GAPDH instability as a real issue

- **Confirmed but must be worded cautiously**
  - `Task1`
  - `Task2`
  - `Task3`

- **Requires wording revision**
  - normalization-dependent biomarker attribution
  - Task2/Task3 biomarker-specific framing
  - final synthesis

- **Requires repeat analysis**
  - clinical correlations
  - Task3 permutation robustness, only if a formal p-value is still desired

- **Should be removed**
  - claims that normalized biomarker models add meaningful value over explicit GAPDH/global structure for Task2/Task3
  - claims that age-adjusted `abd_*`/`dct_*` clinical correlations are robust independent marker-specific findings

## 5. Visual and tabular evidence

This session notebook is table-heavy rather than figure-heavy. The most important evidence is presented as structured output tables saved from the notebook.

Most important tables:

- `q02_gapdh_model_summary.csv`
  - shows how much of GAPDH variance is explained by group structure and clinical variables

- `q02_gapdh_task_auc.csv`
  - shows that GAPDH alone already separates Task2 strongly and Task3 perfectly

- `q03_normalized_increment_performance.csv`
  - shows that normalized biomarker models do not outperform the structure-aware baseline

- `q05_raw_increment_performance.csv`
  - shows that raw miRNA features also do not add meaningfully useful gain over the control block

- `q06_control_ablation_performance.csv`
  - shows how performance changes under component removal in the control block

- `q07_task2_ablation_stability.csv`
  - provides the strongest evidence for the final Task2 control-block interpretation

- `q08_clinical_correlation_reassessment.csv`
  - shows that stronger adjustment collapses the earlier clinical-correlation claims

- `q09_claim_classification.csv`
  - gives the final claim-by-claim statistical disposition

- `q09_revision_checklist.csv`
  - gives the exact notebook revision actions implied by the session review

## 6. Limitations, assumptions, and risks

### Important assumptions

- The raw CSV is the source of truth for rederived variables.
- The notebook’s broader/global Ct proxies are acceptable stand-ins for unavailable original requested global Ct variables.
- The leave-one-out broader/global proxy used in the stronger clinical reassessment is a defensible anti-collinearity adjustment choice.

### Main limitations

- This is a review and reproduction notebook, not the main biological analysis notebook.
- Some nested-CV results in the rebuilt notebook are not numerically identical to the live-session values.
- The largest numeric drift occurs in `q06`, where the rebuilt ablation makes the proxy block look somewhat more helpful than it did during the live session.

### How that limitation was handled

- The notebook explicitly includes a reconciliation note in the `q05/q06` area.
- The final Task2 interpretation is anchored more heavily to `q07`, which is the stronger and more stable resampling-based analysis.

### Remaining risk

- The visible main notebook still contains a clinical-correlation section that does not reflect the stronger-adjustment closeout review.

## 7. Conclusions and next steps

### Final conclusions

- The session supports retaining the notebook’s core within-dataset separation findings.
- The session does not support strong biomarker-specific attribution for the strongest Task2/Task3 results.
- The session does not support the current strength of the notebook’s clinical-correlation claims.
- The notebook’s strongest secure result is:
  - strong within-dataset separation exists
  - but interpretation must remain cautious because reference behavior and broader/global structure explain much of the strongest signal

### Recommended next steps

Highest-priority remaining analysis:

- rerun the clinical-correlation section inside the main notebook with:
  - outcome = each clinical variable
  - predictor = each marker
  - covariates = `GROUP`, `AGE`, `mean_GAPDH`, and a leave-one-out broader/global miRNA Ct proxy
  - BH-FDR across tested marker-clinical pairs

Follow-up revision work after that:

- revise Section 11 of the main notebook to state clearly that GAPDH is not a neutral denominator here
- revise Section 13 and Section 14 to downgrade biomarker-specific language for Task2 and especially Task3
- revise the final synthesis and confidence/caution split so it matches the completed review

## Delivery validation

- Final notebook delivered in repository root: yes
- Matching report with same base name: yes
- Notebook and report describe the same analysis artifact: yes
- Notebook execution status: executed successfully
- Important limitation noted explicitly: yes
