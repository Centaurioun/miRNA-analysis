# IPynb Prompt and Workflow v2

This document consolidates and hardens both the **master prompt** and the **governing workflow specification** for a notebook-based reanalysis of the salivary miRNA periodontal dataset.

It is designed for a workflow in which a Jupyter notebook (`.ipynb`) is the main analytical artifact and the visible source of truth.

---

# PART I — MASTER PROMPT FOR THE NOTEBOOK-BUILDING AGENT

## Task

Use the two workspace files below as the governing inputs for this job:

* `miRNA-qPCR-reanalysis.md`
* `miRNA-qPCR-analysis-results.csv`

Read both files carefully and implement **every directive** from `miRNA-qPCR-reanalysis.md`.

## Primary deliverable

Create a **single, fully executable Jupyter notebook (`.ipynb`)** that performs the complete workflow end to end.

## Core execution doctrine

### 1) The notebook is the visible source of truth

All observable work must be performed inside notebook cells.
This includes:

* data loading,
* schema inspection,
* validation,
* cleaning,
* transformation,
* descriptive analysis,
* inferential testing,
* modeling,
* feature selection,
* visualization,
* sensitivity analysis,
* robustness analysis,
* and output generation.

Do **not** rely on:

* hidden assistant-side preprocessing,
* off-notebook calculations,
* invisible temporary scripts,
* prior runtime state,
* unstated manual edits,
* or unsupported narrative claims.

### 2) The notebook must be auditable, not merely polished

Every major claim must be traceable to:

* visible code,
* visible output,
* and a nearby markdown interpretation.

If a result is not generated inside the notebook, it must not be reported as if it were.

### 3) Use the active notebook runtime

Detect required packages in the current runtime.
Install missing packages inside the notebook itself if needed.
Do not assume access to a pre-existing local `.venv` unless the runtime explicitly exposes it.

### 4) Clean rerun from a fresh kernel is mandatory

The notebook must execute successfully from top to bottom from a fresh runtime with no manual intervention.
All state must be created within the notebook.
Cells must be logically ordered and dependent only on earlier cells.

### 5) Raw-data-first discipline

Treat the CSV as the primary observable data source unless the markdown specification explicitly instructs otherwise and the additional file is actually available in the runtime.
Do not pretend hidden files exist.
Do not silently substitute missing inputs.

### 6) Separate exploratory from stronger inferential claims

If the notebook searches across many models, thresholds, transformations, or feature combinations, that work must be labeled explicitly as exploratory unless the validation logic strongly supports a firmer interpretation.
Do not present searched-for panels as if they were pre-specified.

### 7) Leakage control is mandatory

If classification is performed:

* do not select features on the full dataset before validation,
* do not choose thresholds using all samples when reporting validated performance,
* do not let preprocessing leak outcome information across folds,
* and do not confuse in-sample fit with validated discrimination.

Where feature search or tuning exists, use leakage-safe logic such as nested cross-validation whenever feasible.

### 8) Strong results must trigger skepticism, not celebration

If a model shows unusually high discrimination, intensify robustness checks rather than weakening standards.
Treat near-perfect internal performance as a stress-test trigger.

---

## Required notebook structure

### A. Opening overview

Begin with a markdown section stating:

* the project purpose,
* the two governing input files,
* the fixed group definitions,
* the analytical scope,
* and the reproducibility promise that all observable computations occur inside notebook cells.

### B. Environment and setup

Include code and markdown that:

* imports required libraries,
* installs missing packages,
* prints key package versions,
* sets reproducible seeds,
* configures plotting and display options,
* and creates an organized output directory.

### C. File checks

Define input paths clearly.
Check that both required files exist.
Raise a clear, visible error if either is missing.

### D. Specification ingestion and directive map

Read `miRNA-qPCR-reanalysis.md` inside the notebook.
Create a visible directive checklist or implementation map.
Each major notebook section must clearly correspond to that map.

### E. Input registry and assumption ledger

Create a small notebook-visible registry that records:

* which files were actually available,
* which variables were found in the CSV,
* which expected elements were missing,
* and which assumptions were made.

Create an **Assumption Ledger** table with columns such as:

* `Assumption_ID`
* `Assumption`
* `Why needed`
* `Evidence`
* `Risk if wrong`
* `Affected sections`

### F. Data loading and validation

Load the CSV inside the notebook and show:

* shape,
* column names,
* row preview,
* data types,
* missingness,
* duplicates,
* category levels,
* and obvious schema problems.

Do not rush past data quality issues.

### G. Data cleaning and transformation

Perform cleaning explicitly in code.
Preserve the raw loaded dataframe separately.
Document all transformations in markdown or comments.
Avoid silent recoding.
Create a **Transformation Registry** that records formulas and source columns.

### H. Directive-by-directive implementation

Implement every directive from `miRNA-qPCR-reanalysis.md`.
For each directive:

* use a heading that mirrors the directive,
* show the code,
* show the outputs,
* and add concise interpretation.

If a directive cannot be completed exactly:

* document the obstacle,
* show the evidence of the obstacle,
* state the most defensible fallback,
* and label the section as partial or limited.

### I. Statistical and modeling transparency

For every test or model, show:

* exact code,
* variable inputs,
* assumptions,
* settings,
* thresholds,
* random seed if relevant,
* and the resulting outputs.

Material defaults must not stay hidden.

### J. Results registry

Create a **Results Registry** dataframe or markdown table near the end of the notebook with columns such as:

* `Result_ID`
* `Claim summary`
* `Notebook section`
* `Source output`
* `Analysis type`
* `Exploratory or stronger inference`
* `Key caveat`

This forces claims to stay tethered to visible evidence.

### K. Completion map

Include a completion section that maps:

* each directive from `miRNA-qPCR-reanalysis.md`,
* to the notebook section that implemented it,
* and whether it was completed fully, partially, or not possible.

### L. Reproducibility statement

End with a reproducibility section confirming:

* clean-rerun intent,
* in-notebook package handling,
* seed handling,
* file assumptions,
* limitation handling,
* and the absence of hidden preprocessing.

---

## Failure and discrepancy policy

If any instruction is ambiguous, conflicting, unsupported by the observed dataset, or impossible to execute exactly:

* do not ignore it,
* do not silently reinterpret it,
* document it explicitly,
* implement the most defensible interpretation,
* and record the issue in a **Discrepancy Log**.

The notebook should contain a visible **Discrepancy Log** table with fields such as:

* `Issue_ID`
* `Instruction or expectation`
* `Observed reality`
* `Resolution`
* `Impact on interpretation`

---

## Interpretation policy

* Do not overclaim.
* Do not confuse discrimination with disease-specific biology.
* Do not let elegant writing outrun methodological support.
* Do not market exploratory panels as if they were established biomarkers.
* When preprocessing or normalization choices materially affect conclusions, say so clearly.
* When results depend strongly on small sample patterns, state that plainly.

---

## Final expectation

Deliver a **fully executed, self-contained, auditable `.ipynb` notebook** that reproduces the complete analysis from the provided files, with all observable computations visible inside notebook cells and all major claims tethered to notebook outputs.

---

---

# PART II — GOVERNING WORKFLOW SPECIFICATION FOR `miRNA-qPCR-reanalysis.md`

## 1. Role and objective

Act as a demanding reanalysis partner building the main notebook for this project from scratch.

The notebook must determine what the dataset actually supports about salivary miRNA qPCR patterns across periodontal conditions, their clinical associations, and their potential discriminative value.

The notebook must be:

* transparent,
* reproducible,
* skeptical,
* assumption-aware,
* and explicit about what is robust versus fragile.

Do not behave like a promotional assistant.
Behave like an analytical reviewer building a serious research notebook.

---

## 2. Fixed study definitions

This is a salivary miRNA qPCR dataset related to periodontal conditions.

Group definitions are fixed:

* `S` = Healthy
* `G` = Gingivitis
* `P` = Periodontitis

Fixed pairwise tasks are fixed:

* **Task 1:** `S vs G`
* **Task 2:** `G vs P`
* **Task 3:** `S vs P`

These definitions must not be changed.

---

## 3. Governing analysis principles

### 3.1 Notebook-only observability

All observable work must occur in notebook cells.
No hidden calculations.
No invisible preprocessing.
No unsupported narrative shortcuts.

### 3.2 CSV-first schema discovery

Start from the actual CSV structure.
Infer the variable map from what is present.
Do not assume ideal column names.
Document mismatches explicitly.

### 3.3 Conservative interpretation

Do not overclaim.
Do not equate internal model performance with clinical readiness.
Do not claim disease-specific signal before ruling out broader explanations as well as the design allows.

### 3.4 Explicit exploratory-versus-validated labeling

Any analysis involving search across transformations, markers, panels, thresholds, or models must be labeled clearly as exploratory unless the validation logic justifies stronger language.

### 3.5 Decision logging is required

The notebook must maintain visible logs for:

* assumptions,
* discrepancies,
* transformations,
* and headline results.

### 3.6 Broader-signal skepticism is required

The notebook must actively test whether broader/global Ct structure, reference-gene behavior, demographic imbalance, or other covariates explain part of the apparent signal.

---

## 4. Required notebook workflow

### Section 1 — Title, purpose, and notebook promise

State:

* the project purpose,
* the two workspace files used,
* the fixed S/G/P definitions,
* the fixed task definitions,
* and the promise that all observable computation is notebook-visible.

### Section 2 — Environment setup

Include:

* imports,
* missing-package handling,
* key version output,
* reproducible seeds,
* output-directory creation,
* and plotting/display configuration.

### Section 3 — File existence checks

Verify both workspace files exist.
Fail clearly if either is absent.

### Section 4 — Read this workflow inside the notebook

Read `miRNA-qPCR-reanalysis.md` inside the notebook.
Create a visible directive checklist.
Use it as the controlling implementation map.

### Section 5 — Dataset loading and schema inspection

Load `miRNA-qPCR-analysis-results.csv` and display:

* shape,
* columns,
* preview rows,
* data types,
* missingness,
* duplicates,
* category levels,
* and obvious structural problems.

### Section 6 — Notebook-native data dictionary

Create a concise in-notebook data dictionary grouping variables into:

* grouping variables,
* demographic variables,
* clinical variables,
* qPCR Ct variables,
* and derived variables.

Explicitly note that Ct is an inverse-abundance measure.
Do not use abundance-style interpretation casually.

### Section 7 — Sample accounting and data quality

Provide:

* total N,
* N by group,
* age summaries by group,
* sex summaries by group,
* missing-data summaries,
* duplicate summaries,
* and plausibility checks for major clinical and Ct variables.

Flag suspicious values visibly.

### Section 8 — Transformation registry

If source columns exist, define and document at minimum:

* `dCt_mir146a = mean_mir146a - mean_GAPDH`
* `dCt_mir146b = mean_mir146b - mean_GAPDH`
* `dCt_mir155 = mean_mir155 - mean_GAPDH`
* `dCt_mir203 = mean_mir203 - mean_GAPDH`
* `dCt_mir223 = mean_mir223 - mean_GAPDH`
* `dCt_mir381p = mean_mir381p - mean_GAPDH`
* `global_mean_ct_all7` = mean of the six miRNA Ct variables plus GAPDH
* `global_mean_ct_miRNA_only` = mean of the six miRNA Ct variables only

If the observed column names differ, map them explicitly.
Do not handwave mappings.

### Section 9 — Baseline descriptive and group-comparison analyses

Analyze group differences for available variables corresponding to:

* age,
* sex,
* plaque index,
* gingival index,
* pocket depth,
* bleeding on probing,
* missing teeth,
* and equivalent observed clinical measures.

Use appropriate summaries, assumption checks, appropriate tests, and effect sizes where feasible.
Correct for multiple testing where reasonable.

### Section 10 — miRNA group-difference analyses

For each miRNA-related variable, analyze group differences using:

* raw Ct,
* and derived/normalized versions where justified.

At minimum include:

* three-group comparison,
* Task 1: `S vs G`,
* Task 2: `G vs P`,
* Task 3: `S vs P`.

Add visualizations and multiple-testing correction where appropriate.
Do not use "upregulated" or "downregulated" until the sign convention has been defined and kept consistent.

### Section 11 — Reference-gene and normalization audit

Do not assume GAPDH is stable.
The notebook must directly analyze:

* GAPDH distribution across groups,
* GAPDH variability,
* GAPDH relations with age,
* GAPDH relations with key clinical variables where feasible,
* and the consequences of using GAPDH-based normalization.

Then compare how major findings behave across multiple representations, including where feasible:

* raw Ct,
* ΔCt,
* broader/global Ct summaries,
* and any other transparent normalization strategy that is explicitly justified.

Summarize what remains robust and what weakens materially.

### Section 12 — Clinical correlation analyses

Test associations between miRNA-related variables and available periodontal clinical measures.
Use appropriate correlation methods based on the observed distributions.
Where justified, also add adjusted analyses such as age-adjusted or age-plus-sex adjusted models.
Provide at least one useful visualization such as a heatmap.

### Section 13 — Fixed pairwise classification analyses

Use the exact fixed tasks:

* Task 1: `S vs G`
* Task 2: `G vs P`
* Task 3: `S vs P`

For each task, where data and sample sizes permit, compare transparent workflows using combinations such as:

* single-marker models,
* small multi-marker panels,
* demographic-only models,
* biomarker-plus-demographic models,
* broader/global Ct models,
* and combined biomarker-plus-broader/global models.

Use leakage-safe validation.
If feature search or tuning occurs, use stronger logic such as nested cross-validation where feasible.
Keep threshold selection inside training data only.
Prefer out-of-fold predictions for performance summaries whenever feasible.

Report metrics responsibly, such as:

* AUC,
* accuracy,
* sensitivity,
* specificity,
* PPV,
* NPV,
* confusion matrices,
* and uncertainty summaries if justified.

If a metric cannot be estimated responsibly under the actual workflow, say so.

### Section 14 — Single-marker versus panel comparison

Compare individual markers against small panels.
If searching across multiple combinations:

* label the process explicitly as exploratory,
* keep the search space transparent,
* and avoid letting the best-found panel sound pre-specified.

### Section 15 — Confounding and covariate adjustment

Evaluate whether biomarker-related findings remain after accounting for broader factors such as:

* age,
* sex,
* and broader/global Ct structure.

These are core interpretive checks, not decorative add-ons.
Compare:

* biomarker-only models,
* covariate-only models where sensible,
* combined models,
* and broader/global-aware models.

State clearly whether biomarker-related findings persist, weaken materially, or appear partly explained by broader factors.

### Section 16 — Broader/global Ct structure analysis

Explicitly test whether broader Ct structure explains part of the separation.
At minimum:

* analyze `global_mean_ct_all7` and `global_mean_ct_miRNA_only`,
* compare them across groups,
* test their task-level discriminative value,
* visualize their distributions,
* and compare their explanatory power with biomarker-focused explanations.

If broader/global summaries perform strongly, say that clearly.

### Section 17 — Robustness and sensitivity analyses

Challenge strong findings.
Where justified, include:

* bootstrap-based uncertainty checks,
* permutation-style checks,
* sensitivity to normalization choice,
* sensitivity to covariate adjustment,
* outlier or influence-aware checks,
* stability of model or panel selection,
* threshold sensitivity,
* and missing-data sensitivity if relevant.

Strong results should invite harder checking, not softer standards.

### Section 18 — Additional justified analyses

Add analyses beyond the core plan only when clearly justified by emerging results.
Potential examples may include:

* three-group or multiclass models,
* ordinal or severity-aware analyses,
* PCA or other low-dimensional structure inspection,
* clustering or subgroup exploration,
* calibration checks,
* or limited interaction checks.

Do not add decorative complexity.
Add only what clarifies a real interpretive problem.

### Section 19 — Mandatory checkpoint after each major block

At the end of every major analysis block, insert a markdown section titled exactly:

`Checkpoint — What was found and what happens next`

Each checkpoint must briefly state:

1. what was analyzed,
2. the main findings,
3. what appears robust,
4. what appears fragile, assumption-dependent, suspicious, or incomplete,
5. what alternative explanations remain,
6. and what analysis should follow because of those findings.

### Section 20 — Final synthesis

End with a final synthesis clearly separating:

* findings that appear robust,
* findings that appear fragile,
* findings that weaken after broader checks,
* findings that remain convincing after broader checks,
* and added analyses that materially changed interpretation.

Also include a final section titled exactly:

`What this dataset supports confidently vs cautiously`

---

## 5. Statistical defaults and reporting rules

Unless the observed data justify a better alternative, follow these defaults:

* check assumptions explicitly before parametric testing,
* use nonparametric alternatives when assumptions are doubtful,
* correct for multiple testing when families of related tests are run,
* report effect sizes where feasible,
* separate exploratory work from stronger inference,
* prefer transparent models over unnecessarily complex ones,
* and use reproducible seeds where relevant.

If you depart from these defaults, explain why.

---

## 6. Coding requirements

* Write clear, readable Python.
* Use self-contained code blocks.
* Reuse helper functions where sensible.
* Keep naming consistent.
* Save important tables and figures from within the notebook.
* Keep outputs organized.
* Build reusable dataframes or result objects where this improves auditability.

---

## 7. Interpretation rules

* Do not overclaim.
* Do not confuse discrimination with disease specificity.
* Do not assume a reference gene automatically solves normalization.
* Do not assume strong internal performance explains itself.
* Do not assume a searched-for panel is biologically privileged.
* Keep Ct directionality and abundance-style interpretation logically consistent.
* Make it explicit when conclusions depend materially on preprocessing, transformation, model choice, threshold logic, or adjustment strategy.
* Treat perfect or near-perfect internal classification as a stress-test trigger, not a headline.

---

## 8. Final notebook expectation

The final notebook must be a complete, disciplined, notebook-native reanalysis document.

It must:

* run from a clean restart,
* implement every directive above,
* keep all observable computations inside notebook cells,
* show outputs directly,
* distinguish robust from fragile findings,
* maintain visible assumption, discrepancy, transformation, and results logs,
* and leave an auditable trail from raw CSV to final interpretation.

Do not return a sketch.
Do not return only prose.
Do not skip the hard parts.
Build the notebook as the main research reanalysis notebook for this dataset.
