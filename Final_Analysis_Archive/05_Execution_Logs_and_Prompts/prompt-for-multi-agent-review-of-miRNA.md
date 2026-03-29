# Prompt for Multi-Agent Review of miRNA Analysis Notebooks

**Main Agent:** @miRNA Reanalysis Coordinator

Run a READ-ONLY, strict multi-agent audit of these two notebooks:

1) miRNA_qpcr_reanalysis.ipynb
2) output/jupyter-notebook/2026-03-28-session-statistical-review-reproduction.ipynb

Primary objective:
- Determine what claims are defensible, what is fragile, and what is blocked, using the configured review team.
- Do not edit notebooks/files. Review only.

Governing references (must be applied):
- miRNA-qPCR-reanalysis.md
- AGENTS.md
- Fixed groups/tasks (S/G/P; Task1 SvsG, Task2 GvsP, Task3 SvsP)

Global execution settings:
- review_mode = strict
- output_mode = both
- read_only = true

Subagent sequence (mandatory):
1. Spec Mapper
   - Build directive-by-directive coverage map for BOTH notebooks.
   - Return ready/partial/blocked for each directive with blocker evidence.
2. Data QA Auditor + Biostatistics Reviewer (parallel)
   - QA: schema/coding/missingness/duplicates/derivation provenance/recompute risk
   - Biostats: method appropriateness, assumptions, multiplicity, uncertainty, wording ceiling
3. Modeling Leakage Auditor
   - Evaluate leakage risk, metric validity status, rerun requirement, safe redesign template
4. Interpretation Reviewer
   - Classify claims (robust/tentative/exploratory/unsupported), action (retain/reframe/remove), caveat ceilings
5. Coordinator synthesis
   - Resolve conflicts using strictest credible blocker
   - Produce unified remediation and publication-safe claim ceilings

Normalization contract (required for each specialist):
Return and normalize to these shared fields:
- Status
- Evidence location
- Blocking level
- Notebook action
- Claim ceiling impact

If specialist has richer schema:
- Keep all specialist details below normalized fields.
- Do not drop high-resolution evidence.

Missing-field rule:
- If any shared field is missing from a specialist response, mark that specialist result as partial.
- Do not silently fill missing fields by inference.

Readiness gates (must enforce):
- If Data QA has unresolved high/critical on required inputs -> no downstream acceptance.
- If Biostatistics verdict is reject -> statistical acceptance blocked.
- If Leakage risk is material/critical -> predictive claims capped and not accepted.
- If Interpretation label is unsupported -> claim cannot be re-upgraded in synthesis.

Cross-notebook consistency check (mandatory):
- Identify agreements, conflicts, and dependency causes (QA/statistics/leakage/interpretation).
- Apply stricter claim ceiling when notebooks disagree.

Evidence anchoring rules:
- Use notebook section names and cell numbers only (human-visible anchors).
- Do not use hidden/internal cell IDs.

Output format (exact section order):
A) Executive Summary
   - Overall readiness per notebook: ready / conditional / blocked
   - Highest blocker per notebook
   - Confidence statement per notebook

B) Specialist Findings by Notebook
   - One subsection per specialist per notebook
   - Include normalized 5-field summary + key detailed fields

C) Cross-Notebook Consistency Matrix
   - Agreement/conflict table + root-cause dependency lane

D) Blockers, Claim Ceilings, and Remediation Plan
   - P0/P1/P2 prioritized actions
   - Maximum defensible wording for each capped claim family
   - Go/No-Go by claim class: statistical / predictive / biological / clinical

E) Final Readiness Decision
   - What can be reported now
   - What must be fixed first
   - Minimum evidence needed to unblock each blocked area

Behavioral constraints:
- Do not ask for approval during execution.
- If evidence is missing, mark partial/blocked and state the minimum required evidence.
- Do not overclaim; do not convert exploratory findings into confirmatory conclusions.
- Keep final conclusions bounded by the strictest unresolved blocker.