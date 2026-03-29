@miRNA Reanalysis Coordinator

Objective:
Execute fresh-kernel regeneration and final closure confirmation for all remaining Step-07 deferred issues.

Primary goal:
Convert current `conditional` state to final closure readiness by replacing placeholder/provisional artifacts with execution-derived outputs and proving source↔artifact parity.

Inputs to read first (mandatory):
- `outputs/review-recovery-2026-03-28/06-full-reaudit-strict-results.md`
- `outputs/review-recovery-2026-03-28/07-deferred-issues-closure-results.md`
- `outputs/review-recovery-2026-03-28/07-deferred-issues-closure-results-chat-logs.md`

Target deferred issues to close:
- `DI-07-001` (searched-panel fold-selection log placeholder content)
- `DI-07-002` (P1/P2 artifacts present but not fully regenerated from fresh-kernel execution)

Scope:
- `miRNA_qpcr_reanalysis.ipynb`
- `output/jupyter-notebook/2026-03-28-session-statistical-review-reproduction.ipynb`

Execution settings:
- `review_mode = strict`
- `output_mode = both`
- `read_only = false` for regeneration + closure edits

Mandatory execution sequence:
1. Build a closure checklist from Step-07 deferred issues with explicit pass/fail criteria.
2. Restart kernels and run each notebook top-to-bottom from a fresh kernel (no manual hidden state).
3. Regenerate all closeout-critical artifacts from notebook execution (overwrite placeholder/provisional files).
4. Run strict parity checks between notebook conclusions and persisted artifacts.
5. Run strict mini-audit on deferred lanes only:
   - Spec Mapper
   - Data QA Auditor + Biostatistics Reviewer (parallel)
   - Modeling Leakage Auditor
   - Interpretation Reviewer
6. Produce final closure decision and remaining risk statement.

Fresh-kernel regeneration requirements (mandatory):
- No hidden preprocessing or off-notebook scripts for analytic outputs.
- All regenerated outputs must be traceable to visible notebook cells.
- If any notebook cell fails, stop closure escalation and classify status as blocked with exact error evidence.

Mandatory artifact parity checks:

Notebook 1 (`miRNA_qpcr_reanalysis.ipynb`):
- `outputs/searched_panel_fold_selection_log.csv`
  - Must contain real fold-level rows (no placeholder/NA-only rows).
  - Must align with current searched-panel code path and task IDs.
- `outputs/results_registry.csv`
  - Must remain aligned with strict claim ceilings.
  - Must not reintroduce searched-panel superiority as confirmatory evidence.

Notebook 2 (`2026-03-28-session-statistical-review-reproduction.ipynb`):
- `outputs/session-statistical-review/q09_closeout_summary.csv`
  - Must match q09 closeout markdown conclusions.
- `outputs/session-statistical-review/q09_pending_checks.csv`
  - Must logically support final decision status.

Bundle-level P1/P2 artifact checks:
- Ensure regenerated (not placeholder) values for:
  - `outputs/multiplicity_family_registry.csv`
  - `outputs/taskwise_assumption_effects_ci.csv`
  - `outputs/gapdh_assumption_evidence.csv`
  - `outputs/clinical_adjusted_ols_diagnostics.csv`
  - `outputs/missingness_listwise_impact.csv`
  - `outputs/p2_reproducibility_artifact_check.csv`
  - `outputs/session-statistical-review/p1_listwise_deletion_impact.csv`
  - `outputs/session-statistical-review/q02_multiplicity_family_registry.csv`
  - `outputs/session-statistical-review/q02_gapdh_correlations_fdr_ci.csv`
  - `outputs/session-statistical-review/q08_adjusted_models_diagnostics_ci.csv`
  - `outputs/session-statistical-review/p2_tolerance_summary.csv`

Required output in chat:
A) Fresh-kernel execution summary (per notebook)
B) Artifact regeneration summary (created/updated files)
C) Source↔artifact parity matrix (pass/fail per critical file)
D) Deferred-issues closure matrix (open -> closed/partial/blocked)
E) Final readiness + claim-class Go/No-Go

Required file output (mandatory):
- Create/update: `outputs/review-recovery-2026-03-28/08-fresh-kernel-regeneration-and-closure-confirmation-results.md`
- Required sections (exact order):
  1. Objective
  2. Fresh-kernel execution summary
  3. Regenerated artifacts
  4. Source↔artifact parity matrix
  5. Deferred-issues closure matrix
  6. Remaining blockers
  7. Final readiness + Go/No-Go
  8. Deferred Issues (if any)

Deferred Issues policy (mandatory):
- If anything remains unresolved, include rows with:
  - `Issue_ID`
  - `Blocking level`
  - `Why deferred`
  - `Maximum defensible wording for now`
  - `What evidence/action unblocks it`
  - `Owner agent`
  - `Proposed next prompt/action`
- If none remain, write `Deferred Issues: none` explicitly.

Acceptance criteria:
- `DI-07-001` is closed (real fold-level searched-panel provenance log).
- `DI-07-002` is closed (P1/P2 artifacts regenerated from fresh-kernel runs).
- No unresolved high/critical deferred issue remains.
- Final readiness is at least conditional for both notebooks, with no contradiction between notebook conclusions and persisted artifacts.
