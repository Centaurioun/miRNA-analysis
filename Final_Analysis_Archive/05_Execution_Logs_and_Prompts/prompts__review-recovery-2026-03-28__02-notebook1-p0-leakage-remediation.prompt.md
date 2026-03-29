@miRNA Reanalysis Coordinator

Objective:
Resolve P0 leakage issues in `miRNA_qpcr_reanalysis.ipynb`, especially searched marker/panel paths.

Scope:
- Notebook: `miRNA_qpcr_reanalysis.ipynb`
- Focus sections: classification, panel search/comparison, robustness blocks.

Execution requirements:
- Edit notebook directly.
- Keep all computations notebook-visible.
- Enforce leakage-safe logic for any search/tuning/threshold/calibration path.

Subagent sequence:
1. `Modeling Leakage Auditor` (strict, output_mode=both)
2. `Biostatistics Reviewer` (strict, output_mode=both)
3. `Interpretation Reviewer` (strict, output_mode=both)
4. Coordinator applies edits and reruns affected cells.

Mandatory remediation rules:
- No feature/panel selection on full data prior to validation.
- Search/tuning must be fold-contained (nested CV where applicable).
- Threshold/calibration cannot use evaluation outcomes.
- Use out-of-fold predictions for reported performance summaries.
- Distinguish pre-specified vs searched models in labels.

Required notebook edits:
- Refactor searched panel workflow into nested, fold-contained selection.
- Recompute and replace impacted metrics/tables/plots.
- Add explicit leakage-safety method note in markdown.
- Update claim ceilings for searched panels until external validation exists.

Required output in chat:
A) Leakage defects found and exact fixes applied
B) Which metrics were recomputed/replaced
C) Updated metric validity status
D) Updated claim ceiling wording
E) Evidence anchors (section names + cell numbers)

Required file output (mandatory):
- Create/update: `outputs/review-recovery-2026-03-28/02-notebook1-p0-leakage-remediation-results.md`
- The file must include sections:
	1. Objective
	2. Leakage defects and fixes
	3. Metrics recomputed/replaced
	4. Updated metric validity and claim ceilings
	5. Deferred Issues (if any)
	6. Acceptance check

Deferred Issues policy (mandatory):
- If any leakage/statistical/interpretive issue remains unresolved, add it under `Deferred Issues` with:
	- `Issue_ID`
	- `Blocking level`
	- `Why deferred`
	- `What evidence/action unblocks it`
	- `Owner agent`
	- `Target prompt step` (e.g., 03/04/06)
- If none remain, write `Deferred Issues: none` explicitly.

Acceptance criteria:
- Leakage risk for searched panel paths is reduced to none/low with evidence.
- Any previously contaminated metric is replaced by leakage-safe rerun output.
- Predictive language is consistent with updated metric validity.
