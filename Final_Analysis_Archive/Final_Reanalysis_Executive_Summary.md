# Final Reanalysis Executive Summary

## KPI dashboard

| Metric | Value |
| --- | --- |
| Final decision | ready |
| Confirmation from reviewer closeout | yes, with caveated wording |
| Missingness / attrition gate | True |
| Most harmful age fraction under q07 | 0.96 |
| Task2 delta median (q03) | -0.0578414351851852 |
| Task3 delta median (q03) | 0.0 |
| Task2 delta median (q05) | 0.0007770007770007137 |
| Task3 delta median (q05) | 0.0 |

## Best internal classifiers by task

| Task         | Best model family   | Model label                                               |      AUC |   Accuracy |   Sensitivity |   Specificity |
|:-------------|:--------------------|:----------------------------------------------------------|---------:|-----------:|--------------:|--------------:|
| Task1_S_vs_G | single_marker       | abd_mir146b                                               | 0.761574 |   0.666667 |      0.694444 |      0.638889 |
| Task2_G_vs_P | combined_model      | ABD+Proxy+Demo_select7                                    | 0.997685 |   0.958333 |      1        |      0.916667 |
| Task3_S_vs_P | broader_global_only | global_mean_ct_all7_proxy+global_mean_ct_miRNA_only_proxy | 1        |   1        |      1        |      1        |

## Initial problem state

The dataset began with a leakage concern: apparent discrimination was vulnerable to reference-gene instability, broader Ct structure, and selection-affected model search. The analysis therefore hardened the workflow with nested cross-validation, explicit FDR control, permutation checks, and repeated robustness/attrition checks.

## Methodological interventions

- Nested CV with in-fold tuning and OOF summaries for the main classifiers.
- Benjamini-Hochberg FDR control for family-wise inferential reporting.
- Listwise deletion accounting and explicit attrition ceilings.
- Structure-control comparisons to test whether broad Ct patterns outperformed biomarker-specific panels.

## Artifact traceability

- [Model diagnostics](02_Model_Diagnostics/outputs__task_model_performance_nestedcv.csv)
- [Assumption ledger](03_Assumption_Ledgers/outputs__assumption_ledger.csv)
- [Parity checks](04_Artifact_Parity_Checks/outputs__session-statistical-review__q09_closeout_summary.csv)
- [Prompts and logs](05_Execution_Logs_and_Prompts/prompts__review-recovery-2026-03-28__README.md)

## Final scientific conclusions

| Category                  | Claim                                         | Disposition                                                                                                              |
|:--------------------------|:----------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------|
| confirmed                 | Univariate inferential framework              | Notebook-native taskwise Mann-Whitney + within-task FDR completed from raw CSV for fixed tasks.                          |
| confirmed                 | Leakage-safe classification setup             | Nested CV with in-fold tuning and OOF predictions used for q03/q05/q06 summaries.                                        |
| confirmed                 | GAPDH instability                             | Reference-gene instability remains material under q02 stress testing.                                                    |
| confirmed but cautious    | Task1_S_vs_G                                  | Signal is exploratory and should remain cautiously worded.                                                               |
| confirmed but cautious    | Task2_G_vs_P                                  | Strong within-dataset separation persists; q03/q05 indicate limited incremental biomarker value over structure controls. |
| confirmed but cautious    | Task3_S_vs_P                                  | Very strong separation remains, with structure-related controls sufficient for high internal discrimination.             |
| requires wording revision | Normalization-dependent biomarker attribution | dCt/abd markers remain reference-sensitive and should not be framed as reference-secure proof.                           |
| requires wording revision | Clinical-correlation robustness framing       | q08 stronger-adjusted reassessment completed; robust independent marker-specific claims should be removed.               |
| optional sensitivity      | Task3 permutation robustness                  | Permutation check is now reproduced in q01; further permutations are optional only.                                      |
| should be removed         | Incremental normalized biomarker value claim  | q03 delta medians do not support meaningful incremental gain over structure-only controls.                               |
| should be removed         | Robust independent clinical-correlation claim | q08 classifications are predominantly group/structure-driven under stronger adjustment.                                  |

### Interpretation

Task 1 remains exploratory and cautiously worded. Task 2 retains strong internal separation, but the archived q03/q05 delta medians indicate limited incremental biomarker value over structure controls. Task 3 shows very strong internal discrimination, yet the broader-global and combined models indicate that apparent performance is not automatically equivalent to disease-specific biological signal. The safest conclusion is that the dataset supports strong internal classification patterns under the archived leakage-safe workflow, with interpretation constrained by structure-related signal and selection sensitivity.

## Reproducibility note

This archive is a copied, collision-safe snapshot. The source files remain untouched. All copied artifacts are discoverable through the manifest and the audit log, and every folder contains a local README with a data dictionary for its CSV files.
