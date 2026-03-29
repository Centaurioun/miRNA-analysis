# 03-claims-v2-language-downgrade-results

## 1. Objective

Fix unsupported biological/clinical claim language across:
- `miRNA_qpcr_reanalysis.ipynb`
- `output/jupyter-notebook/2026-03-28-session-statistical-review-reproduction.ipynb`

Edits were restricted to markdown interpretation/synthesis cells. No computational cells or numeric outputs were edited.

## 2. Claim-by-claim wording changes

### Notebook A — `miRNA_qpcr_reanalysis.ipynb`

1) **Final synthesis certainty reduction (execution-state aware)**
- **Location:** Section 19–20, **Cell 42**
- **Old:** “Fixed-task discrimination signal is present…”
- **New:** “Prior saved outputs indicate fixed-task discrimination signal…”
- **Reason:** Prevent claiming fully established findings when key downstream model sections are not freshly executed in current notebook state.

2) **Over-broad interpretation-change statement downgraded**
- **Location:** Section 19–20, **Cell 42**
- **Old:** “Analyses that materially changed interpretation: fold-contained searched-panel logic, panel-selection stability reporting, threshold-sensitivity summaries, and all-task permutation checks…”
- **New:** “Interpretation guardrail: Claims in this section should be treated as provisional until Sections 13–18 are freshly re-executed and outputs visibly regenerated.”
- **Reason:** Avoid evidence-traceability overreach.

3) **Biological directionality caveat tightened**
- **Location:** Section 19–20, **Cell 42**
- **Old:** “Some miRNA-derived variables show within-dataset directional contrasts…”
- **New:** “Some miRNA-derived variables show within-dataset contrasts, but sign and biological interpretation remain representation-/normalization-sensitive.”
- **Reason:** Maintain non-causal, normalization-sensitive interpretation ceiling.

### Notebook B — `2026-03-28-session-statistical-review-reproduction.ipynb`

4) **Task2 attribution softened to non-specific incremental framing**
- **Location:** q04 revised interpretation, **Cell 19**
- **Old:** “…does not support attributing that separation primarily to the normalized biomarker panel.”
- **New:** “…should not be interpreted as uniquely biomarker-specific… adding normalized biomarker block did not improve AUC over structure controls.”
- **Reason:** Reduce biomarker-primacy implication.

5) **Task3 near-ceiling phrasing + no superiority claim**
- **Location:** q04 revised interpretation, **Cell 19**
- **Old:** “...extremely strong... uniquely biomarker-specific discrimination... perfect internal discrimination...”
- **New:** “...near-ceiling internal separation... should not be framed as disease-specific biomarker superiority... no incremental gain in bootstrap delta summaries.”
- **Reason:** Prevent superiority/mechanistic overclaim from internal near-perfect discrimination.

6) **q05/q06 reconciliation changed to CI-bounded language**
- **Location:** reconciliation note, **Cell 24**
- **Old:** “...broader/global proxy ablation look somewhat more harmful...”
- **New:** “...larger point estimate... but bootstrap interval includes near-zero effects; not a decisive dominance result.”
- **Reason:** Point estimates alone were over-interpreted.

7) **Task2 contributor wording made explicitly tentative**
- **Location:** reconciliation note, **Cell 24**
- **Old:** “...mean_GAPDH plus proxy block behave like a redundant structure-related signal.”
- **New:** “...are consistent with overlapping structure-related signal.”
- **Reason:** Avoid mechanistic certainty under collinearity.

8) **Bottom-line internal-only caveat strengthened**
- **Location:** Bottom Line, **Cell 35**
- **Old:** “The core evidence for strong within-dataset separation should be preserved.”
- **New:** “Strong **internal** within-dataset separation is supported, with attribution constrained by confounding/structure alternatives.”
- **Reason:** Align with strict evidence ceiling.

## 3. Post-edit claim labels/actions

| Claim area | Label after edit | Action |
|---|---|---|
| Notebook A final synthesis discrimination statement | unsupported -> tentative/provisional | Reframed to prior-output/provisional language with execution guardrail |
| Notebook A interpretation-change omnibus statement | unsupported | Replaced with explicit provisional execution-state guardrail |
| Notebook A directionality sentence | tentative | Added normalization/representation caveat |
| Notebook B Task2 biomarker attribution | tentative | Kept internal discrimination; removed unique biomarker implication |
| Notebook B Task3 near-perfect discrimination | tentative | Converted to near-ceiling internal separability with no superiority claim |
| Notebook B q05/q06 ablation interpretation | tentative | Reframed to CI-bounded, non-decisive wording |
| Notebook B Task2 contributor stability line | tentative | Softened to “consistent with” language |
| Notebook B Bottom Line | tentative | Strengthened internal-only + constrained attribution caveat |

## 4. Remaining no-go claim classes

1. Causal/mechanistic verbs from observational/model-comparison evidence (e.g., “drives,” “causes,” “determines”).
2. Disease-specific biology claims inferred from discrimination alone.
3. Clinical-actionability or operating-threshold utility claims without external transport/calibration validation.
4. Searched-panel superiority claims as confirmatory findings.
5. “No effect” conclusions from non-significance without equivalence/non-inferiority design.

## 5. Deferred Issues (if any)

| Issue_ID | Blocking level | Why deferred | Maximum defensible wording for now | What evidence/action unblocks it | Owner agent | Target prompt step |
|---|---|---|---|---|---|---|
| DI-03V2-001 | moderate | In `miRNA_qpcr_reanalysis.ipynb`, final synthesis currently references interpretation-level conclusions while key model/robustness sections are not freshly executed in current notebook state. | “Prior saved outputs indicate internal discrimination patterns, pending fresh in-notebook rerun visibility for Sections 13–18.” | Fresh-kernel rerun through Sections 13–18 with visible outputs and aligned artifacts (`task_model_performance_nestedcv.csv`, searched-panel provenance, robustness summaries). | Coordinator + Biostatistics Reviewer | 04/06 |

## 6. Acceptance check

- ✅ Unsupported biological/clinical claims were removed or reframed in markdown interpretation/synthesis cells only.
- ✅ No code/result changes were made in this task; edits were language-only.
- ✅ Final synthesis language in both notebooks is aligned to strict internal-evidence ceilings.
- ✅ Remaining unresolved claim risk is explicitly tracked in Deferred Issues.
