# What is in this archive

This folder is a validated, collision-safe copy of the miRNA-qPCR reanalysis record. It contains the main reports, diagnostics, ledgers, parity checks, prompts, and logs that document how the final result was reached.

## Main workflow phases

1. **Data QA and provenance** — inputs, transformations, assumptions, and discrepancy tracking.
2. **Leakage-safe modeling** — nested cross-validation, in-fold tuning, and out-of-fold summaries.
3. **Statistical hardening** — inferential tests, FDR control, permutation checks, and robustness checks.
4. **Parity and closeout** — reproducibility checks, completion maps, and final confirmation artifacts.
5. **Execution trace** — prompts, chat logs, and recovery notes that show how the archive was assembled.

## Most important result categories

- [`01_Methodological_Reports/`](./01_Methodological_Reports/) — the readable narrative record.
- [`02_Model_Diagnostics/`](./02_Model_Diagnostics/) — performance, calibration, and robustness tables.
- [`03_Assumption_Ledgers/`](./03_Assumption_Ledgers/) — provenance, assumptions, and discrepancy logs.
- [`04_Artifact_Parity_Checks/`](./04_Artifact_Parity_Checks/) — validation and reproducibility evidence.
- [`05_Execution_Logs_and_Prompts/`](./05_Execution_Logs_and_Prompts/) — the operational trail.

## Main takeaway

The archived workflow supports strong internal classification patterns, but the interpretation stays cautious: structure-related signal, reference-gene instability, and selection sensitivity matter, so the safest reading is “useful internal separation with constrained biological claims.”

## If you only read 3 files

- [`Final_Reanalysis_Executive_Summary.md`](./Final_Reanalysis_Executive_Summary.md)
- [`02_Model_Diagnostics/outputs__task_model_performance_nestedcv.csv`](./02_Model_Diagnostics/outputs__task_model_performance_nestedcv.csv)
- [`04_Artifact_Parity_Checks/outputs__session-statistical-review__q09_closeout_summary.csv`](./04_Artifact_Parity_Checks/outputs__session-statistical-review__q09_closeout_summary.csv)

## If you want technical detail

- [`README.md`](./README.md) — the archive layout in one page.
- [`migration_manifest.json`](./migration_manifest.json) — the copied file list and target paths.
- [`organization_audit.log`](./organization_audit.log) — the creation and validation record.