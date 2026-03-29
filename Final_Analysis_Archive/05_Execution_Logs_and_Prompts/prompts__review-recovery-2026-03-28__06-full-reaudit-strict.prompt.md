@miRNA Reanalysis Coordinator

Run a final strict read-only re-audit of both notebooks after remediation.

Notebooks:
1) miRNA_qpcr_reanalysis.ipynb
2) output/jupyter-notebook/2026-03-28-session-statistical-review-reproduction.ipynb

Governing references:
- miRNA-qPCR-reanalysis.md
- AGENTS.md

Execution settings:
- review_mode = strict
- output_mode = both
- read_only = true

Subagent sequence (mandatory):
1. Spec Mapper
2. Data QA Auditor + Biostatistics Reviewer (parallel)
3. Modeling Leakage Auditor
4. Interpretation Reviewer
5. Coordinator synthesis with strictest-blocker precedence

Required final report sections (exact order):
A) Executive summary
B) Specialist findings by notebook
C) Cross-notebook consistency matrix
D) Blockers, claim ceilings, remediation deltas
E) Final readiness decision

Readiness categories:
- ready
- conditional
- blocked

Go/No-Go required for claim classes:
- statistical
- predictive
- biological
- clinical

Output requirements:
- Use section names + cell numbers only for evidence hooks.
- Provide maximum defensible wording where any cap remains.
- Explicitly list any remaining P0 blockers (should be none if remediation succeeded).

Required file output (mandatory):
- Create/update: `outputs/review-recovery-2026-03-28/06-full-reaudit-strict-results.md`
- The file must include sections (exact order):
	1. Executive summary
	2. Specialist findings by notebook
	3. Cross-notebook consistency matrix
	4. Blockers, claim ceilings, remediation deltas
	5. Final readiness decision
	6. Deferred Issues (if any)

Deferred Issues policy (mandatory):
- If anything remains unresolved after final re-audit, include `Deferred Issues` rows with:
	- `Issue_ID`
	- `Blocking level`
	- `Why deferred`
	- `Maximum defensible wording for now`
	- `What evidence/action unblocks it`
	- `Owner agent`
	- `Proposed next prompt/action`
- If none remain, write `Deferred Issues: none` explicitly.

Acceptance criteria:
- Both notebooks are no worse than conditional.
- No unresolved P0 blocker remains.
- Final claim ceilings and go/no-go are internally consistent with specialist evidence.
