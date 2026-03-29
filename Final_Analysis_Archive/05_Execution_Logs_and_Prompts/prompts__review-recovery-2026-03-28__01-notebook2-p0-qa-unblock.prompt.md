@miRNA Reanalysis Coordinator

Objective:
Resolve P0 blockers in `output/jupyter-notebook/2026-03-28-session-statistical-review-reproduction.ipynb` related to QA/provenance dependency and incomplete rerun closeout.

Scope:
- Notebook: `output/jupyter-notebook/2026-03-28-session-statistical-review-reproduction.ipynb`
- Governing specs: `miRNA-qPCR-reanalysis.md`, `AGENTS.md`
- Fixed groups/tasks must remain unchanged.

Execution requirements:
- Edit this notebook directly (not read-only).
- Keep all computations notebook-visible.
- Do not rely on hidden/off-notebook preprocessing.
- Apply strict evidence/provenance discipline.

Subagent sequence:
1. `Spec Mapper` (strict) — map missing required artifacts for this notebook.
2. `Data QA Auditor` (strict) — identify all high/moderate unresolved QA/provenance defects.
3. `Biostatistics Reviewer` (strict) — ensure no statistical acceptance depends on unresolved QA defects.
4. Coordinator synthesis — generate and implement notebook edits.

Must-fix targets from prior report:
- Remove/replace core dependence on upstream exported artifacts for required adjudication evidence.
- Correct derivation/provenance mapping inconsistencies.
- Enforce strict group coding assertions for S/G/P.
- Add/complete notebook-visible rerun closeout where prior status said “needs repeat analysis”.
- Ensure required evidence is anchored to this notebook outputs.

Required notebook additions/updates:
- A clear provenance section with file/variable origin and transformation trace.
- Explicit QA gates (coding/range/missingness/duplication assertions).
- A rerun-closeout section showing completion status of all previously pending checks.
- Updated discrepancy entries for any unresolved constraints.

Required output in chat:
A) What was changed (cell-level summary)
B) Remaining blockers (if any) with blocking level
C) Evidence anchors (section names + cell numbers)
D) Readiness decision for this notebook: ready / conditional / blocked

Required file output (mandatory):
- Create/update: `outputs/review-recovery-2026-03-28/01-notebook2-p0-qa-unblock-results.md`
- The file must include sections:
	1. Objective
	2. Changes applied (cell-level)
	3. Specialist summaries
	4. Remaining blockers
	5. Deferred Issues (if any)
	6. Readiness decision

Deferred Issues policy (mandatory):
- If any issue is not fully resolved, add it under `Deferred Issues` with:
	- `Issue_ID`
	- `Blocking level`
	- `Why deferred`
	- `What evidence/action unblocks it`
	- `Owner agent`
	- `Target prompt step` (e.g., 02/03/04/06)
- If none remain, write `Deferred Issues: none` explicitly.

Acceptance criteria:
- No unresolved high QA/provenance blocker remains.
- Rerun-closeout no longer indicates pending repeat analysis.
- All key adjudication claims are supported by this notebook’s own visible outputs.
