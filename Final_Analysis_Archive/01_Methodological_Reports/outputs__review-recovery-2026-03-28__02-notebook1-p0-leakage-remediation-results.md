# 02-notebook1-p0-leakage-remediation-results

## 1. Objective

Resolve P0 leakage risks in `miRNA_qpcr_reanalysis.ipynb` for searched marker/panel workflows, enforce fold-contained search/tuning logic, and align interpretation ceilings with leakage-safe evidence.

## 2. Leakage defects and fixes

### Defect A (P0): full-data pre-ranking before searched panel evaluation
- **Where found:** Section 13–16 classification helper (**Cell 24**).
- **Problem:** marker ranking (`roc_auc_score` across all samples) was used to define top markers before CV panel evaluation.
- **Why leakage:** searched feature space depended on full labels outside outer folds.
- **Fix applied:** replaced searched-panel path with **outer-fold-contained panel search**:
  - candidate ranking performed on outer-train only,
  - inner CV selects pair + hyperparameter,
  - outer-test predictions stored as OOF.

### Defect B: downstream summaries could include leakage-tainted searched-panel rankings
- **Where found:** single-vs-panel summary and registry logic (**Cells 27 and 40**).
- **Fix applied:** updated claim-tier logic and registry wording to keep searched-panel claims exploratory and non-confirmatory; rank-eligible top rows now exclude searched-panel family.

### Defect C: interpretation overstatement risks
- **Where found:** Section checkpoint and final synthesis language (**Cells 30 and 37**).
- **Fix applied:** replaced robust/absolute language with tentative/exploratory claim ceilings; explicit caution that discrimination does not establish disease-specific biology or external validity.

### Additional hardening
- **Cell 23:** added explicit leakage-safety method note.
- **Cell 33:** bootstrap uncertainty now uses OOF probabilities for best single-marker per task (still labeled exploratory due within-dataset ranking).
- **Cell 25:** added fold-selection log export: `searched_panel_fold_selection_log.csv`.

## 3. Metrics recomputed/replaced

### Recomputed/replaced code paths
- `task_model_performance_nestedcv.csv` generation logic replaced to use fold-contained searched-panel OOF pipeline (**Cell 25**).
- `single_vs_panel_summary.csv` now derives from remediated model results (**Cell 27**, via rerun).
- `results_registry.csv` claim-tier logic updated and “stronger” labeling removed (**Cell 40**, via rerun).
- New artifact: `searched_panel_fold_selection_log.csv` with per-fold selected panel and inner-CV score (**Cell 25**, via rerun).

### Execution status
- Notebook cells were edited successfully; **runtime rerun is pending** (see Deferred Issues) because this session does not have notebook cell execution capability.

## 4. Updated metric validity and claim ceilings

### Validity status (post-edit design)
- **Searched panels:** Exploratory, fold-contained nested search design implemented; valid as internal exploratory estimates after rerun.
- **Non-searched families:** Tentative internal inference; OOF nested-CV estimates remain internal-only.
- **Biological specificity claims from classifier performance:** Unsupported without orthogonal validation.

### Updated claim ceiling wording
- Searched panels: “Exploratory panel search identified candidate combinations with internal discrimination; results are selection-affected and hypothesis-generating, not confirmatory.”
- Non-searched families: “Nested-CV OOF results indicate internal discrimination in this dataset; external validity and disease specificity are not established.”

## 5. Deferred Issues (if any)

- **Issue_ID:** DI-02-NB-RERUN
- **Blocking level:** moderate
- **Why deferred:** Notebook execution/rerun is not available in this session, so refreshed numeric outputs/plots cannot be produced here.
- **What evidence/action unblocks it:** Run notebook from fresh kernel through Cells 24–40 and verify regenerated artifacts in `outputs/`.
- **Owner agent:** miRNA Reanalysis Coordinator
- **Target prompt step:** 03/04/06

## 6. Acceptance check

- **Leakage risk for searched panel paths reduced to none/low with evidence:** **Design-level PASS** (fold-contained searched-panel nested CV implemented in Cell 24).
- **Previously contaminated metric replaced by leakage-safe rerun output:** **PENDING RERUN** (logic replaced; numeric outputs require execution).
- **Predictive language consistent with updated metric validity:** **PASS** (checkpoint/final synthesis/registry wording downgraded to tentative/exploratory ceilings).
