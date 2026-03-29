@miRNA Reanalysis Coordinator

Objective:
Fix unsupported biological/clinical claim language across both notebooks.

Scope:
- `miRNA_qpcr_reanalysis.ipynb`
- `output/jupyter-notebook/2026-03-28-session-statistical-review-reproduction.ipynb`

Execution requirements:
- Edit markdown interpretation/synthesis cells only where needed.
- Preserve results; adjust wording/caveats/claim ceilings to match evidence.

Subagent sequence:
1. `Interpretation Reviewer` (strict)
2. `Biostatistics Reviewer` (strict)
3. Coordinator applies language edits.

Mandatory language rules:
- No causal wording for observational/correlational evidence.
- No disease-specific biology claim unless alternatives are ruled out.
- No clinical-actionability language beyond current support.
- Use explicit maximum defensible wording where evidence is tentative.

Required output in chat:
A) Claim-by-claim change log (old phrasing -> new phrasing)
B) Claim label after edit (robust/tentative/exploratory/unsupported)
C) Any remaining no-go claim classes
D) Evidence anchors (section names + cell numbers)

Required file output (mandatory):
- Create/update: `outputs/review-recovery-2026-03-28/03-claims-language-downgrade-results.md`
- The file must include sections:
	1. Objective
	2. Claim-by-claim wording changes
	3. Post-edit claim labels/actions
	4. Remaining no-go claim classes
	5. Deferred Issues (if any)
	6. Acceptance check

Deferred Issues policy (mandatory):
- For any unresolved claim, add a `Deferred Issues` row with:
	- `Issue_ID`
	- `Blocking level`
	- `Why deferred`
	- `Maximum defensible wording for now`
	- `What evidence/action unblocks it`
	- `Owner agent`
	- `Target prompt step` (e.g., 04/06)
- If none remain, write `Deferred Issues: none` explicitly.

Acceptance criteria:
- Unsupported biological/clinical claims are removed or reframed.
- Final synthesis text is fully aligned to strict evidence ceilings.
