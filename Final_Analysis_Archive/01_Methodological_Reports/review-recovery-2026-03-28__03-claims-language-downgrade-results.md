# 03-claims-language-downgrade-results

## 1. Objective

Fix unsupported biological/clinical claim language in:
- `miRNA_qpcr_reanalysis.ipynb`
- `output/jupyter-notebook/2026-03-28-session-statistical-review-reproduction.ipynb`

Edits were limited to markdown interpretation/synthesis cells; results and computations were preserved.

## 2. Claim-by-claim wording changes

### Notebook A — `miRNA_qpcr_reanalysis.ipynb`

1) **Robustness checkpoint overstatement**
- **Location:** Section 17–18 checkpoint, **Cell 36**
- **Old:** “Effects that remain strong under permutation and broad bootstrap intervals are more credible.”
- **New:** “For the tested models, permutation/bootstrap checks were directionally reassuring, but remain internal and non-confirmatory.”

2) **Final synthesis attribution overreach**
- **Location:** Section 19–20 final synthesis, **Cell 37**
- **Old:** “Effects that remain strong in combined/adjusted models and pass robustness checks have stronger internal support, but still require external validation.”
- **New:** “Some combined/adjusted models retain strong internal discrimination, but robustness depth is limited and biological attribution remains unresolved.”

3) **Directionality certainty softening**
- **Location:** Section 19–20 support split, **Cell 37**
- **Old:** “Directional contrasts for some miRNA-derived features within this dataset.”
- **New:** “Some miRNA-derived variables show within-dataset directional contrasts, sensitive to representation/normalization choices.”

### Notebook B — `output/jupyter-notebook/2026-03-28-session-statistical-review-reproduction.ipynb`

4) **Task3 perfect-performance wording hardening**
- **Location:** q04 revised interpretation, **Cell 17**
- **Old:** “…structure variables alone achieved perfect internal discrimination…”
- **New:** “…structure variables alone achieved perfect internal discrimination in this internal evaluation…”
- **Added caveat:** internal-only scope and non-biomarker-specific framing retained.

5) **Causal phrasing in Task2 reconciliation**
- **Location:** q05/q06 reconciliation note, **Cell 22**
- **Old:** “…driven by age plus redundant reference/global structure…”
- **New:** “…more consistent with age plus shared reference/global structure… This remains associational and non-causal.”

6) **Closeout certainty flattening**
- **Location:** Rerun closeout, **Cell 29**
- **Old:** procedural completion bullets without cross-review dependency qualifier.
- **New:** added explicit qualifier: notebook rerun checks resolved locally, but final interpretation ceilings still depend on cross-review dependency resolution and artifact consistency.

7) **Bottom-line absolute resolution wording**
- **Location:** Bottom Line, **Cell 30**
- **Old:** “The prior closeout blocker (`needs repeat analysis`) is now resolved…”
- **New:** “The prior closeout blocker … is addressed in this notebook … final resolved status should be asserted only when closeout artifacts are internally consistent across the review bundle.”

## 3. Post-edit claim labels/actions

| Claim area | Label after edit | Action taken |
|---|---|---|
| Internal discrimination in fixed tasks | tentative (internal-only) | Retained with explicit non-generalization caveats |
| Searched panel/best panel language | exploratory | Retained only as hypothesis-generating framing |
| Robustness wording from limited checks | tentative | Downgraded to model-specific, non-confirmatory language |
| Disease-specific biology from classifier performance | unsupported as a class | Explicitly framed as unresolved/not established |
| Clinical actionability/threshold utility | unsupported as a class | Explicitly left out pending external calibration/validation |
| “Blocker resolved” procedural language | exploratory/tentative | Made conditional on cross-artifact consistency |

## 4. Remaining no-go claim classes

The following remain disallowed in final synthesis text:
1. Causal/mechanistic verbs from observational/ablation evidence (e.g., “driven by”, “causes”, “determines”).
2. Disease-specific biological claims inferred from discrimination metrics alone.
3. Clinical utility or threshold-actionability claims from default-threshold internal CV only.
4. External generalization claims without independent validation.
5. “Best panel” superiority claims as confirmatory evidence.

## 5. Deferred Issues (if any)

Deferred Issues: none

## 6. Acceptance check

- ✅ Unsupported biological/clinical claims were removed or reframed in markdown interpretation/synthesis cells only.
- ✅ Final synthesis language is aligned to strict evidence ceilings (internal/tentative/exploratory tiers).
- ✅ No computational results were changed; only wording/caveat language was edited.
- ✅ Cross-notebook closeout certainty wording now includes dependency/consistency guardrails.
