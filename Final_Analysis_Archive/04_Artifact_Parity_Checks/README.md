# 04 Artifact Parity Checks

**Purpose.** Parity, QA, and reproducibility confirmation artifacts.

**Provenance.** Derived from closeout checks, artifact inventories, completion maps, and final decision logs.

## Contents

- CSV files: 19
- Markdown files: 0
- Log files: 0

## Data dictionary

| File | Columns |
| --- | --- |
| `outputs__completion_map.csv` | Directive, Section, Status |
| `outputs__miRNA-ipynb-analysis-results-reports-29-03-2026__analysis_results__03_statistical_hardening__multiplicity_family_registry.csv` | Family_ID, Section, Family_Definition, Members, Primary_Test, Sensitivity_Test, Correction |
| `outputs__miRNA-ipynb-analysis-results-reports-29-03-2026__analysis_results__05_audit_ledgers__completion_map.csv` | Directive, Section, Status |
| `outputs__miRNA-ipynb-analysis-results-reports-29-03-2026__analysis_results__05_audit_ledgers__model_comparison_family_registry.csv` | Family_ID, Section, Family_Definition, Members, Primary_Metric, Correction_or_Ceiling |
| `outputs__miRNA-ipynb-analysis-results-reports-29-03-2026__analysis_results__05_audit_ledgers__p2_reproducibility_artifact_check.csv` | Artifact, Exists_now, Path |
| `outputs__miRNA-ipynb-analysis-results-reports-29-03-2026__analysis_results__05_audit_ledgers__results_registry.csv` | Result_ID, Claim summary, Notebook section, Source output, Analysis type, Exploratory or stronger inference, Key_Caveat, Rank_Eligible, Missingness_status, Complete_case_fraction_min, Claim_ceiling_from_missingness |
| `outputs__miRNA-ipynb-analysis-results-reports-29-03-2026__data_and_inputs__miRNA-qPCR-analysis-results.csv` | GROUP, SEX, AGE, plaque_index, gingival_index, pocket_depth, bleeding_on_probing, number_of_missing_teeth, mean_mir146a, mean_mir146b, mean_mir155, mean_mir203, mean_mir223, mean_mir381p, mean_GAPDH |
| `outputs__model_comparison_family_registry.csv` | Family_ID, Section, Family_Definition, Members, Primary_Metric, Correction_or_Ceiling |
| `outputs__multiplicity_family_registry.csv` | Family_ID, Section, Family_Definition, Members, Primary_Test, Sensitivity_Test, Correction |
| `outputs__p2_reproducibility_artifact_check.csv` | Artifact, Exists_now, Path |
| `outputs__results_registry.csv` | Result_ID, Claim summary, Notebook section, Source output, Analysis type, Exploratory or stronger inference, Key_Caveat, Rank_Eligible, Missingness_status, Complete_case_fraction_min, Claim_ceiling_from_missingness |
| `outputs__session-statistical-review__p2_tolerance_summary.csv` | Comparison, Rows_compared, Median_abs_diff, Max_abs_diff, Tolerance_rule, Within_tolerance |
| `outputs__session-statistical-review__q02_multiplicity_family_registry.csv` | Family_ID, Section, Family_Definition, Members, Primary_Test, Correction |
| `outputs__session-statistical-review__q09_claim_classification.csv` | Category, Claim, Disposition |
| `outputs__session-statistical-review__q09_closeout_summary.csv` | Question, Answer |
| `outputs__session-statistical-review__q09_pending_checks.csv` | Pending_Check, Completed, Evidence_Object |
| `outputs__session-statistical-review__q09_revision_checklist.csv` | Notebook_Section, Action, Reason, Evidence_Anchors |
| `outputs__session-statistical-review__qa_gate_results_reproduced.csv` | QA_Gate, Pass |
| `outputs__session-statistical-review__transformation_registry_reproduced.csv` | Derived_Variable, Formula, Rationale |
