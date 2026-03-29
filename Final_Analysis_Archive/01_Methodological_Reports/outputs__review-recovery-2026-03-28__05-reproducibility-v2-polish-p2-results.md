# 05-reproducibility-v2-polish-p2-results

## 1. Objective

Apply P2 reproducibility/robustness polish across both notebooks with emphasis on:
- fresh-kernel rerun guidance,
- tolerance evidence visibility,
- explicit internal-vs-external validation boundaries,
- clear reporting without hidden preprocessing.

## 2. Reproducibility improvements

### Notebook 1: `miRNA_qpcr_reanalysis.ipynb`

1. **Reproducibility statement strengthened (Section “Reproducibility statement (P2 polish)”, Cell 48).**
   - Added explicit rerun-observation rule:
     - interpretive claims are treated as rerun-verified only when analysis cells and checklist outputs are visibly regenerated in the current notebook state.
   - Preserved explicit internal-only boundary and external-validation requirement.

2. **Notebook-visible artifact checklist retained and referenced (Results/closeout block, Cell 47).**
   - `outputs/p2_reproducibility_artifact_check.csv` remains the visible parity snapshot.
   - Current file shows required artifacts present in the parity snapshot.

### Notebook 2: `output/jupyter-notebook/2026-03-28-session-statistical-review-reproduction.ipynb`

1. **Rerun closeout narrative clarified (Section “Rerun Closeout Status (P2 polish)”, Cell 35).**
   - Added explicit statement that `ready` is valid when closeout tables are regenerated in the current fresh-kernel run.

2. **Tolerance summary retained as explicit P2 evidence (Tolerance block, Cell 34).**
   - `outputs/session-statistical-review/p2_tolerance_summary.csv` confirms available tolerance comparisons:
     - q01 taskwise comparison within tolerance,
     - q02 Kruskal GAPDH p-value within tolerance.

3. **Closeout evidence remains explicit and auditable.**
   - `outputs/session-statistical-review/q09_pending_checks.csv`: all pending checks complete.
   - `outputs/session-statistical-review/q09_closeout_summary.csv`: final decision = `ready` (with caveated wording).

## 3. Remaining intrinsic limitations

1. **Internal validation scope only.**
   - Both notebooks remain internal-evidence artifacts; no external cohort verification is present.

2. **No external calibration/transport validation.**
   - Threshold and calibration conclusions are internal/descriptive and should not be interpreted as clinical operating-point readiness.

3. **Attribution limits remain.**
   - High discrimination does not establish disease-specific mechanism under current observational design.

4. **Reproducibility is state-sensitive.**
   - Claims should always be tied to visibly regenerated outputs in the active notebook run state.

## 4. Deferred Issues (if any)

| Issue_ID | Blocking level | Why deferred | What evidence/action unblocks it | Owner agent | Target prompt step |
|---|---|---|---|---|---|
| P2V2-DI-001 | moderate | External validation is out of scope for current notebooks/dataset. | Independent cohort replication with frozen preprocessing and preregistered acceptance criteria. | miRNA Reanalysis Coordinator | 06 |
| P2V2-DI-002 | low | Clinical-actionability/transport calibration cannot be established from internal rerun evidence alone. | External transport + calibration drift evaluation with predefined clinical thresholds. | Biostatistics Reviewer + Coordinator | 06 |

## 5. Acceptance check

- ✅ Notebook narrative clearly separates reproducible-now (internal) vs external-validation-needed claims.
- ✅ Internal-only performance conclusions are explicit with no ambiguity.
- ✅ P2 tolerance and closeout evidence are notebook-visible and artifact-backed.
- ✅ No hidden preprocessing was introduced.
