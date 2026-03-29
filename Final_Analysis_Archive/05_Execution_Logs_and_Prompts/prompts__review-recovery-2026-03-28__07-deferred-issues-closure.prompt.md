@miRNA Reanalysis Coordinator

Objective:
Close all deferred issues from Steps 01-06 by forcing source↔artifact parity and producing a final closure matrix.

Inputs to read first (mandatory):
- `outputs/review-recovery-2026-03-28/01-notebook2-p0-qa-unblock-results.md`
- `outputs/review-recovery-2026-03-28/02-notebook1-p0-leakage-remediation-results.md`
- `outputs/review-recovery-2026-03-28/03-claims-language-downgrade-results.md`
- `outputs/review-recovery-2026-03-28/04-statistical-hardening-p1-results.md`
- `outputs/review-recovery-2026-03-28/05-reproducibility-polish-p2-results.md`
- `outputs/review-recovery-2026-03-28/06-full-reaudit-strict-results.md`
- `outputs/review-recovery-2026-03-28/01-06-results-all-chat-logs.md`

Target deferred issues to close (minimum):
- DI-06-001 / P0-RPT-001 (Notebook 2 closeout artifact mismatch)
- DI-06-002 / P0-LEAK-002 (Notebook 1 registry/provenance mismatch)
- DI-06-003 (bundle synchronization parity)

Scope:
- `miRNA_qpcr_reanalysis.ipynb`
- `output/jupyter-notebook/2026-03-28-session-statistical-review-reproduction.ipynb`

Execution settings:
- `review_mode = strict`
- `output_mode = both`
- `read_only = false` for closure edits + rerun evidence

Required process (mandatory order):
1. Build a unified Deferred-Issues Register from steps 01-06.
2. For each deferred issue, define explicit closure criteria and required evidence artifacts.
3. Execute notebook updates/reruns needed to satisfy closure criteria.
4. Verify source↔artifact parity for closeout-critical files.
5. Re-run strict read-only mini-audit (Spec Mapper -> Data QA + Biostat -> Leakage -> Interpretation) focused only on previously deferred lanes.
6. Produce final closure decision.

Mandatory parity checks:
- Notebook 2:
  - `q09_closeout_summary.csv` must no longer conflict with q09 closeout markdown conclusions.
  - `q09_pending_checks.csv` and closeout decision must be logically aligned.
- Notebook 1:
  - `results_registry.csv` must align with current strict claim ceilings.
  - searched-panel/perfect-performance rows must not exceed allowed ceilings.
  - `searched_panel_fold_selection_log.csv` must exist and be referenced where required.
- Bundle-level:
  - P1/P2 artifacts used in conclusions must exist and match current source logic.

Required output in chat:
A) Deferred-Issues closure matrix (open -> closed/partial/blocked)
B) Exact edits/reruns performed
C) Parity verification results (pass/fail by artifact)
D) Remaining blockers (if any)
E) Updated readiness + Go/No-Go by claim class

Required file output (mandatory):
- Create/update: `outputs/review-recovery-2026-03-28/07-deferred-issues-closure-results.md`
- Required sections:
  1. Objective
  2. Deferred-Issues closure matrix
  3. Edits/reruns performed
  4. Source↔artifact parity checks
  5. Remaining blockers
  6. Final readiness + Go/No-Go
  7. Deferred Issues (if any)

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
- No unresolved P0 blocker remains.
- Source↔artifact parity passes for all closeout-critical files.
- Final readiness is at least conditional for both notebooks.
- Claim-class Go/No-Go is internally consistent with verified evidence.
