@miRNA Reanalysis Coordinator

Objective:
Apply P2 reproducibility/robustness polish after P0/P1 are complete.

Scope:
- Both notebooks

Execution requirements:
- Focus on reproducibility evidence, tolerance checks, and reporting clarity.
- Do not introduce hidden preprocessing.

Recommended additions:
- Explicit rerun reproducibility note (fresh-kernel guidance and observed outcomes).
- Tolerance summary for reproduced metrics where applicable.
- Clear statement of what is internal validation vs external validation need.
- Optional external-validation roadmap section (clearly labeled future work).

Required output in chat:
A) Reproducibility improvements added
B) What remains inherently limited by current dataset/scope
C) Evidence anchors (section names + cell numbers)

Required file output (mandatory):
- Create/update: `outputs/review-recovery-2026-03-28/05-reproducibility-polish-p2-results.md`
- The file must include sections:
	1. Objective
	2. Reproducibility improvements
	3. Remaining intrinsic limitations
	4. Deferred Issues (if any)
	5. Acceptance check

Deferred Issues policy (mandatory):
- For any unresolved reproducibility or external-validation limitation, add `Deferred Issues` rows with:
	- `Issue_ID`
	- `Blocking level`
	- `Why deferred`
	- `What evidence/action unblocks it`
	- `Owner agent`
	- `Target prompt step` (usually 06)
- If none remain, write `Deferred Issues: none` explicitly.

Acceptance criteria:
- Notebook narrative clearly separates what is reproducible now vs what needs external validation.
- No ambiguity about internal-only performance conclusions.
