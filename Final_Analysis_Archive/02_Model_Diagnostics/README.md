# 02 Model Diagnostics

**Purpose.** Model diagnostics, validation summaries, and robustness checks.

**Provenance.** Derived from nested-CV, bootstrap, permutation, calibration, and clinical association result files.

## Contents

- CSV files: 72
- Markdown files: 0
- Log files: 0

## Data dictionary

| File | Columns |
| --- | --- |
| `outputs__bootstrap_auc_best_single_markers.csv` | Task, Marker, AUC_boot_median, AUC_boot_ci95_low, AUC_boot_ci95_high, Boot_n |
| `outputs__bootstrap_auc_prespecified_families.csv` | Task, Model_Family, Model_Label, AUC_oof_boot_median, AUC_oof_boot_ci95_low, AUC_oof_boot_ci95_high, Boot_n, Interpretation |
| `outputs__calibration_oof_diagnostics.csv` | Task, Model_Family, Model_Label, AUC_oof, Brier_oof, ECE10_oof, Calibration_note |
| `outputs__clinical_adjusted_ols_diagnostics.csv` | Marker, Clinical_Variable, N, Beta_clinical_adj_age, Beta_ci95_low, Beta_ci95_high, P_clinical_adj_age, Shapiro_resid_p, BreuschPagan_p, Max_CooksD, Frac_CooksD_gt_4_over_n, Max_VIF_nonconst, Age_quad_delta_AIC, Clinical_quad_delta_AIC, Assumption_flag, Inference_tier, P_q_fdr |
| `outputs__clinical_correlations_age_adjusted.csv` | Marker, Clinical_Variable, Beta_clinical_adj_age, P_clinical_adj_age, N, P_q_fdr, Reject_fdr05 |
| `outputs__clinical_correlations_spearman.csv` | Marker, Clinical_Variable, Spearman_r, Spearman_p, Spearman_q_fdr, Reject_fdr05 |
| `outputs__confounding_and_broader_comparisons.csv` | AUC, Accuracy, Sensitivity, Specificity, PPV, NPV, TN, FP, FN, TP, Task, Model_Family, Model_Label, n, Model_Validity, Claim_Ceiling |
| `outputs__exploratory_pca_variance.csv` | Component, Explained_Variance_Ratio |
| `outputs__gapdh_assumption_evidence.csv` | Group, N, Shapiro_p, Levene_p_all_groups, ANOVA_eta_sq |
| `outputs__gapdh_audit_tests.csv` | Metric, Value |
| `outputs__gapdh_covariate_associations.csv` | Covariate, N_effective, Spearman_r, Spearman_p, Spearman_r_ci95_low, Spearman_r_ci95_high, Spearman_q_fdr |
| `outputs__gapdh_group_summary.csv` | GROUP, mean, std, median, min, max |
| `outputs__miRNA-ipynb-analysis-results-reports-29-03-2026__analysis_results__01_data_qa_and_provenance__gapdh_assumption_evidence.csv` | Group, N, Shapiro_p, Levene_p_all_groups, ANOVA_eta_sq |
| `outputs__miRNA-ipynb-analysis-results-reports-29-03-2026__analysis_results__01_data_qa_and_provenance__gapdh_audit_tests.csv` | Metric, Value |
| `outputs__miRNA-ipynb-analysis-results-reports-29-03-2026__analysis_results__01_data_qa_and_provenance__gapdh_covariate_associations.csv` | Covariate, N_effective, Spearman_r, Spearman_p, Spearman_r_ci95_low, Spearman_r_ci95_high, Spearman_q_fdr |
| `outputs__miRNA-ipynb-analysis-results-reports-29-03-2026__analysis_results__01_data_qa_and_provenance__gapdh_group_summary.csv` | GROUP, mean, std, median, min, max |
| `outputs__miRNA-ipynb-analysis-results-reports-29-03-2026__analysis_results__01_data_qa_and_provenance__missingness_listwise_impact.csv` | Analysis_family, Rows_total, Rows_complete_case, Complete_case_fraction, Dropped_rows, Listwise_deletion_impact, Handling_rule |
| `outputs__miRNA-ipynb-analysis-results-reports-29-03-2026__analysis_results__02_leakage_remediation__calibration_oof_diagnostics.csv` | Task, Model_Family, Model_Label, AUC_oof, Brier_oof, ECE10_oof, Calibration_note |
| `outputs__miRNA-ipynb-analysis-results-reports-29-03-2026__analysis_results__02_leakage_remediation__searched_panel_fold_selection_log.csv` | Fold, Selected_Panel, InnerCV_BestAUC, Candidate_Count, Task |
| `outputs__miRNA-ipynb-analysis-results-reports-29-03-2026__analysis_results__02_leakage_remediation__searched_panel_selection_stability.csv` | Task, Unique_Selected_Panels, Most_Frequent_Panel, Most_Frequent_Count, Most_Frequent_Proportion, Selection_Entropy_bits, Interpretation |
| `outputs__miRNA-ipynb-analysis-results-reports-29-03-2026__analysis_results__02_leakage_remediation__single_vs_panel_summary.csv` | Task, Model_Family, max, median, mean, count |
| `outputs__miRNA-ipynb-analysis-results-reports-29-03-2026__analysis_results__02_leakage_remediation__task_model_performance_nestedcv.csv` | AUC, Accuracy, Sensitivity, Specificity, PPV, NPV, TN, FP, FN, TP, Task, Model_Family, Model_Label, n, Model_Validity, Claim_Ceiling |
| `outputs__miRNA-ipynb-analysis-results-reports-29-03-2026__analysis_results__02_leakage_remediation__threshold_sensitivity_oof.csv` | Task, Model_Family, Model_Label, Threshold, AUC, Accuracy, Sensitivity, Specificity, PPV, NPV, TN, FP, FN, TP |
| `outputs__miRNA-ipynb-analysis-results-reports-29-03-2026__analysis_results__03_statistical_hardening__bootstrap_auc_best_single_markers.csv` | Task, Marker, AUC_boot_median, AUC_boot_ci95_low, AUC_boot_ci95_high, Boot_n |
| `outputs__miRNA-ipynb-analysis-results-reports-29-03-2026__analysis_results__03_statistical_hardening__bootstrap_auc_prespecified_families.csv` | Task, Model_Family, Model_Label, AUC_oof_boot_median, AUC_oof_boot_ci95_low, AUC_oof_boot_ci95_high, Boot_n, Interpretation |
| `outputs__miRNA-ipynb-analysis-results-reports-29-03-2026__analysis_results__03_statistical_hardening__permutation_check_combined_all_tasks.csv` | Task, Model, Observed_AUC, Permutation_n, Perm_AUC_Mean, Perm_AUC_SD, Permutation_p_value |
| `outputs__miRNA-ipynb-analysis-results-reports-29-03-2026__analysis_results__03_statistical_hardening__permutation_check_task3_combined.csv` | Task, Model, Observed_AUC, Permutation_n, Permutation_p_value |
| `outputs__miRNA-ipynb-analysis-results-reports-29-03-2026__analysis_results__03_statistical_hardening__taskwise_assumption_effects_ci.csv` | Task, Variable, n1, n2, Shapiro_p_group1, Shapiro_p_group2, Levene_p, Primary_inference_path, Sensitivity_inference_path, Cliffs_delta, Cliffs_delta_boot_median, Cliffs_delta_ci95_low, Cliffs_delta_ci95_high, MedianDiff_boot_median_g2_minus_g1, MedianDiff_ci95_low, MedianDiff_ci95_high, Sample_size_fragility |
| `outputs__miRNA-ipynb-analysis-results-reports-29-03-2026__analysis_results__03_statistical_hardening__taskwise_inferential_tests.csv` | Task, Group1, Group2, Variable, n1, n2, median_diff_g2_minus_g1, mw_p, welch_p, mw_q_fdr, mw_reject_fdr05 |
| `outputs__miRNA-ipynb-analysis-results-reports-29-03-2026__analysis_results__04_clinical_and_eda__clinical_adjusted_ols_diagnostics.csv` | Marker, Clinical_Variable, N, Beta_clinical_adj_age, Beta_ci95_low, Beta_ci95_high, P_clinical_adj_age, Shapiro_resid_p, BreuschPagan_p, Max_CooksD, Frac_CooksD_gt_4_over_n, Max_VIF_nonconst, Age_quad_delta_AIC, Clinical_quad_delta_AIC, Assumption_flag, Inference_tier, P_q_fdr |
| `outputs__miRNA-ipynb-analysis-results-reports-29-03-2026__analysis_results__04_clinical_and_eda__clinical_correlations_age_adjusted.csv` | Marker, Clinical_Variable, Beta_clinical_adj_age, P_clinical_adj_age, N, P_q_fdr, Reject_fdr05 |
| `outputs__miRNA-ipynb-analysis-results-reports-29-03-2026__analysis_results__04_clinical_and_eda__clinical_correlations_spearman.csv` | Marker, Clinical_Variable, Spearman_r, Spearman_p, Spearman_q_fdr, Reject_fdr05 |
| `outputs__miRNA-ipynb-analysis-results-reports-29-03-2026__analysis_results__04_clinical_and_eda__confounding_and_broader_comparisons.csv` | AUC, Accuracy, Sensitivity, Specificity, PPV, NPV, TN, FP, FN, TP, Task, Model_Family, Model_Label, n, Model_Validity, Claim_Ceiling |
| `outputs__miRNA-ipynb-analysis-results-reports-29-03-2026__analysis_results__04_clinical_and_eda__exploratory_pca_variance.csv` | Component, Explained_Variance_Ratio |
| `outputs__miRNA-ipynb-analysis-results-reports-29-03-2026__analysis_results__04_clinical_and_eda__summary_by_group.csv` | , mean_mir146a, mean_mir146a, mean_mir146a, mean_mir146b, mean_mir146b, mean_mir146b, mean_mir155, mean_mir155, mean_mir155, mean_mir203, mean_mir203, mean_mir203, mean_mir223, mean_mir223, mean_mir223, mean_mir381p, mean_mir381p, mean_mir381p, mean_GAPDH, mean_GAPDH, mean_GAPDH, global_mean_ct_all7_proxy, global_mean_ct_all7_proxy, global_mean_ct_all7_proxy, global_mean_ct_miRNA_only_proxy, global_mean_ct_miRNA_only_proxy, global_mean_ct_miRNA_only_proxy |
| `outputs__missingness_listwise_impact.csv` | Analysis_family, Rows_total, Rows_complete_case, Complete_case_fraction, Dropped_rows, Listwise_deletion_impact, Handling_rule |
| `outputs__permutation_check_combined_all_tasks.csv` | Task, Model, Observed_AUC, Permutation_n, Perm_AUC_Mean, Perm_AUC_SD, Permutation_p_value |
| `outputs__permutation_check_task3_combined.csv` | Task, Model, Observed_AUC, Permutation_n, Permutation_p_value |
| `outputs__searched_panel_fold_selection_log.csv` | Fold, Selected_Panel, InnerCV_BestAUC, Candidate_Count, Task |
| `outputs__searched_panel_selection_stability.csv` | Task, Unique_Selected_Panels, Most_Frequent_Panel, Most_Frequent_Count, Most_Frequent_Proportion, Selection_Entropy_bits, Interpretation |
| `outputs__session-statistical-review__p1_listwise_deletion_impact.csv` | Analysis_family, Rows_total, Rows_complete_case, Dropped_rows, Complete_case_fraction, Listwise_deletion_impact, Handling_rule |
| `outputs__session-statistical-review__q01_foundation_summary.csv` | Metric, Value |
| `outputs__session-statistical-review__q01_task3_permutation_recomputed.csv` | task, model, observed_auc, perm_mean_auc, perm_sd_auc, perm_p_value, n_permutations |
| `outputs__session-statistical-review__q01_taskwise_inferential_tests_recomputed.csv` | task, group_a, group_b, marker, n_group_a, n_group_b, mw_u, mw_p, mean_diff_group_b_minus_group_a, cliffs_delta, cliffs_delta_ci95_low, cliffs_delta_ci95_high, median_diff_group_b_minus_group_a, median_diff_ci95_low, median_diff_ci95_high, mw_q_fdr |
| `outputs__session-statistical-review__q02_gapdh_correlations.csv` | variable, rho, p_value |
| `outputs__session-statistical-review__q02_gapdh_correlations_fdr_ci.csv` | variable, rho, p_value, q_fdr_bh, rho_ci95_low, rho_ci95_high |
| `outputs__session-statistical-review__q02_gapdh_diagnostics.csv` | Model, Shapiro_P, BreuschPagan_P, Max_VIF |
| `outputs__session-statistical-review__q02_gapdh_model_summary.csv` | model, r_squared, adj_r_squared, f_pvalue |
| `outputs__session-statistical-review__q02_gapdh_task_auc.csv` | task, group_a, group_b, gapdh_auc, gapdh_mean_diff_group_b_minus_group_a |
| `outputs__session-statistical-review__q03_normalized_increment_bootstrap.csv` | delta_median, delta_mean, ci_low, ci_high, n_boot_valid, task, comparison |
| `outputs__session-statistical-review__q03_normalized_increment_bootstrap_hardened.csv` | delta_median, delta_mean, ci_low, ci_high, n_boot_valid, task, comparison, family, ci_crosses_zero, evidence_tier, note |
| `outputs__session-statistical-review__q03_normalized_increment_performance.csv` | task, model_name, n_features, features, auc, accuracy, sensitivity, specificity, ppv, f1, tn, tp, fn, fp |
| `outputs__session-statistical-review__q03_q05_q06_multiplicity_registry.csv` | Family_ID, Section, Family_Definition, Correction |
| `outputs__session-statistical-review__q05_raw_increment_bootstrap.csv` | delta_median, delta_mean, ci_low, ci_high, n_boot_valid, task, comparison |
| `outputs__session-statistical-review__q05_raw_increment_bootstrap_hardened.csv` | delta_median, delta_mean, ci_low, ci_high, n_boot_valid, task, comparison, family, ci_crosses_zero, evidence_tier, note |
| `outputs__session-statistical-review__q05_raw_increment_performance.csv` | task, model_name, n_features, features, auc, accuracy, sensitivity, specificity, ppv, f1, tn, tp, fn, fp |
| `outputs__session-statistical-review__q06_control_ablation_bootstrap.csv` | delta_median, delta_mean, ci_low, ci_high, n_boot_valid, task, comparison |
| `outputs__session-statistical-review__q06_control_ablation_bootstrap_hardened.csv` | delta_median, delta_mean, ci_low, ci_high, n_boot_valid, task, comparison, family, ci_crosses_zero, evidence_tier, note |
| `outputs__session-statistical-review__q06_control_ablation_performance.csv` | task, model_name, n_features, features, auc, accuracy, sensitivity, specificity, ppv, f1, tn, tp, fn, fp |
| `outputs__session-statistical-review__q07_task2_ablation_stability.csv` | ablation, median_delta_auc, mean_delta_auc, positive_fraction, most_harmful_fraction |
| `outputs__session-statistical-review__q07_task2_coefficient_stability.csv` | feature, median_coef, sign_consistency, abs_median_coef |
| `outputs__session-statistical-review__q07_task2_control_correlations.csv` | , AGE, mean_GAPDH, global_mean_ct_all7_proxy, global_mean_ct_miRNA_only_proxy |
| `outputs__session-statistical-review__q07_task2_vif.csv` | variable, VIF |
| `outputs__session-statistical-review__q08_adjusted_models_diagnostics_ci.csv` | family, marker, clinical_variable, n, beta, beta_ci95_low, beta_ci95_high, p, shapiro_resid_p, breusch_pagan_p, frac_cook_gt_4_over_n, max_vif_numeric, reset_p, assumption_flag, inference_tier, q_fdr_bh |
| `outputs__session-statistical-review__q08_clinical_correlation_reassessment.csv` | family, marker, clinical_variable, beta_adj_std, p_adj, partial_r2, rho_unadj, rho_unadj_p, adj_r2_model, n, q_adj_fdr, classification |
| `outputs__session-statistical-review__q08_clinical_group_r2.csv` | clinical_variable, r2_group_only, r2_group_plus_age |
| `outputs__single_vs_panel_summary.csv` | Task, Model_Family, max, median, mean, count |
| `outputs__summary_by_group.csv` | , mean_mir146a, mean_mir146a, mean_mir146a, mean_mir146b, mean_mir146b, mean_mir146b, mean_mir155, mean_mir155, mean_mir155, mean_mir203, mean_mir203, mean_mir203, mean_mir223, mean_mir223, mean_mir223, mean_mir381p, mean_mir381p, mean_mir381p, mean_GAPDH, mean_GAPDH, mean_GAPDH, global_mean_ct_all7_proxy, global_mean_ct_all7_proxy, global_mean_ct_all7_proxy, global_mean_ct_miRNA_only_proxy, global_mean_ct_miRNA_only_proxy, global_mean_ct_miRNA_only_proxy |
| `outputs__task_model_performance_nestedcv.csv` | AUC, Accuracy, Sensitivity, Specificity, PPV, NPV, TN, FP, FN, TP, Task, Model_Family, Model_Label, n, Model_Validity, Claim_Ceiling |
| `outputs__taskwise_assumption_effects_ci.csv` | Task, Variable, n1, n2, Shapiro_p_group1, Shapiro_p_group2, Levene_p, Primary_inference_path, Sensitivity_inference_path, Cliffs_delta, Cliffs_delta_boot_median, Cliffs_delta_ci95_low, Cliffs_delta_ci95_high, MedianDiff_boot_median_g2_minus_g1, MedianDiff_ci95_low, MedianDiff_ci95_high, Sample_size_fragility |
| `outputs__taskwise_inferential_tests.csv` | Task, Group1, Group2, Variable, n1, n2, median_diff_g2_minus_g1, mw_p, welch_p, mw_q_fdr, mw_reject_fdr05 |
| `outputs__threshold_sensitivity_oof.csv` | Task, Model_Family, Model_Label, Threshold, AUC, Accuracy, Sensitivity, Specificity, PPV, NPV, TN, FP, FN, TP |
