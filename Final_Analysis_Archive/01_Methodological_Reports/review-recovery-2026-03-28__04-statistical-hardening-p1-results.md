# 04-statistical-hardening-p1-results

## 1. Objective

Execute P1 statistical hardening in:
- `miRNA_qpcr_reanalysis.ipynb`
- `output/jupyter-notebook/2026-03-28-session-statistical-review-reproduction.ipynb`

Scope was limited to notebook-visible diagnostics/reporting additions, preserving existing computations and conclusions ceilings.

## 2. Diagnostics and multiplicity changes

### A. `miRNA_qpcr_reanalysis.ipynb`

1. **Section 9-10 hardening (after Cell 17)**
   - Added **multiplicity family registry** (`F1`-`F3`) with explicit family definitions and BH-FDR strategy.
   - Added **assumption-evidence + effect-size/CI table** per task-variable:
     - Shapiro p-values per group
     - Levene p-values
     - Cliff's delta with bootstrap 95% CI
     - Median difference bootstrap 95% CI
     - sample-size fragility flag
   - Outputs:
     - `outputs/multiplicity_family_registry.csv`
     - `outputs/taskwise_assumption_effects_ci.csv`

2. **Section 11 GAPDH hardening (after Cell 20)**
   - Added ANOVA/Kruskal assumption-evidence table:
     - per-group Shapiro p-values
     - Levene p-value
     - ANOVA eta-squared effect size
   - Added interpretation note: Kruskal primary if assumptions weak; ANOVA sensitivity only.
   - Output:
     - `outputs/gapdh_assumption_evidence.csv`

3. **Section 12 adjusted-model hardening (after Cell 22)**
   - Added OLS diagnostics and uncertainty table across adjusted marker-clinical models:
     - coefficient CI95
     - residual normality (Shapiro)
     - heteroskedasticity (Breusch-Pagan)
     - influence (Cook's D fraction)
     - inference tier (`tentative_adjusted` vs `exploratory_adjusted`)
   - Added explicit **listwise-deletion impact table** by analysis family.
   - Outputs:
     - `outputs/clinical_adjusted_ols_diagnostics.csv`
     - `outputs/missingness_listwise_impact.csv`

4. **Final synthesis guardrail (Cell 37)**
   - Added explicit non-significant phrasing policy:
     - “insufficient statistical evidence” ≠ “no effect”
     - no equivalence/non-inferiority framework run.

### B. `2026-03-28-session-statistical-review-reproduction.ipynb`

1. **Data QA / attrition tie-in (after Cell 7)**
   - Added notebook-visible listwise deletion impact table by analysis family.
   - Output:
     - `outputs/session-statistical-review/p1_listwise_deletion_impact.csv`

2. **q02 multiplicity + CI hardening (after Cell 14)**
   - Added q02 family registry (`Q02-F1`) and BH-FDR across GAPDH correlation family.
   - Added Fisher-transformed 95% CI for Spearman rho.
   - Outputs:
     - `outputs/session-statistical-review/q02_multiplicity_family_registry.csv`
     - `outputs/session-statistical-review/q02_gapdh_correlations_fdr_ci.csv`

3. **q08 adjusted-model diagnostics (after Cell 26)**
   - Added model diagnostics and CI table:
     - beta CI95, Shapiro residual p, Breusch-Pagan p, Cook's D burden
     - assumption flag and inference tier
     - family-level BH-FDR by raw/abd families
   - Output:
     - `outputs/session-statistical-review/q08_adjusted_models_diagnostics_ci.csv`

4. **q09 interpretation policy guardrail (after Cell 29)**
   - Added explicit statement that non-significant findings are not interpreted as evidence of absence.

## 3. Adequacy status by section

### `miRNA_qpcr_reanalysis.ipynb`
- **Section 9-10 inferential tests:** Adequate (strict) after explicit assumption/CI/effect-size and family registry.
- **Section 11 GAPDH audit:** Adequate with caveat (ANOVA treated as sensitivity where assumptions weak).
- **Section 12 clinical correlations/adjusted models:** Adequate (strict) after diagnostics + CI + inference-tiering.
- **Sections 13-16 classification interpretation path:** Adequate with caveat (internal-only discrimination remains).
- **Section 19-20 synthesis wording:** Adequate after non-significant interpretation guardrail.

### `2026-03-28-session-statistical-review-reproduction.ipynb`
- **Data loading/QA + attrition visibility:** Adequate after listwise-deletion impact table.
- **q02 GAPDH stress test:** Adequate (strict) after explicit family correction + CI.
- **q03/q05/q06 model-comparison uncertainty:** Adequate with caveat (internal CV evidence retained as tentative).
- **q08 stronger-adjusted reassessment:** Adequate (strict) after diagnostics + CI + family-level FDR.
- **q09 adjudication wording:** Adequate after non-significant phrasing guardrail.

## 4. Remaining statistical caveats

1. Evidence remains **internal** to this dataset (no external replication).
2. Proxy global-structure variables remain a structural limitation and must stay caveated.
3. Small-sample fragility remains possible for some contrasts despite robust methods.
4. Associations remain non-causal; diagnostics improve fit transparency, not causal identification.

## 5. Deferred Issues (if any)

Deferred Issues: none

## 6. Acceptance check

- ✅ No major method-appropriateness gap remains in core claim paths.
- ✅ Multiplicity families and correction strategies are explicit and auditable.
- ✅ Effect sizes and uncertainty intervals are now visible in notebook outputs.
- ✅ Missing-data/listwise implications are explicitly reported.
- ✅ Non-significant findings are constrained to non-overreaching language.
