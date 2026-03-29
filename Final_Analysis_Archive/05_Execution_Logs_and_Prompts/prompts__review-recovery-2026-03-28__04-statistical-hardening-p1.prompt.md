@miRNA Reanalysis Coordinator

Objective:
Execute P1 statistical hardening in both notebooks.

Scope:
- `miRNA_qpcr_reanalysis.ipynb`
- `output/jupyter-notebook/2026-03-28-session-statistical-review-reproduction.ipynb`

Execution requirements:
- Add/strengthen diagnostics and reporting where currently partial.
- Keep all checks notebook-visible.

Subagent sequence:
1. `Biostatistics Reviewer` (strict)
2. `Data QA Auditor` (strict) for missing-data/attrition risk tie-in
3. Coordinator applies edits.

Hardening checklist:
- Parametric-family assumption evidence visible or robust alternative justified.
- Multiplicity family definitions explicit for related test sets.
- Family-level correction strategy explicit and consistently reported.
- Effect sizes + uncertainty intervals presented with interpretation.
- Non-significant findings phrased correctly (no “no effect” overreach).
- Missing-data/listwise-deletion implications explicitly evaluated where relevant.

Required output in chat:
A) What diagnostics/multiplicity additions were made
B) Which sections now meet adequacy criteria
C) Remaining statistical caveats
D) Evidence anchors (section names + cell numbers)

Required file output (mandatory):
- Create/update: `outputs/review-recovery-2026-03-28/04-statistical-hardening-p1-results.md`
- The file must include sections:
	1. Objective
	2. Diagnostics and multiplicity changes
	3. Adequacy status by section
	4. Remaining statistical caveats
	5. Deferred Issues (if any)
	6. Acceptance check

Deferred Issues policy (mandatory):
- For unresolved statistical gaps, add `Deferred Issues` rows with:
	- `Issue_ID`
	- `Blocking level`
	- `Why deferred`
	- `What evidence/action unblocks it`
	- `Owner agent`
	- `Target prompt step` (e.g., 05/06)
- If none remain, write `Deferred Issues: none` explicitly.

Acceptance criteria:
- No major method-appropriateness gap remains in core claim paths.
- Multiplicity and uncertainty reporting are explicit and auditable.
