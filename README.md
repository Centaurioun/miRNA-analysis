# miRNA-analysis

Notebook-native reanalysis workspace for salivary miRNA qPCR data across periodontal groups.

## Project scope

This repository is designed around a single auditable notebook workflow.

- **Main deliverable:** `miRNA_qpcr_reanalysis.ipynb`
- **Governing spec:** `miRNA-qPCR-reanalysis.md`
- **Primary data:** `miRNA-qPCR-analysis-results.csv`

Fixed definitions (must remain unchanged):

- `S = Healthy`
- `G = Gingivitis`
- `P = Periodontitis`

Fixed pairwise tasks:

- `Task 1: S vs G`
- `Task 2: G vs P`
- `Task 3: S vs P`

## Repository structure

- `AGENTS.md` — workspace-wide operational constraints.
- `.github/agents/` — coordinator/worker custom agents for this project.
- `.github/prompts/` — reusable orchestration prompt.
- `.github/workflows/repo-sanity.yml` — basic required-file and workflow checks.
- `.github/ISSUE_TEMPLATE/` — bug + feature issue templates.
- `.github/PULL_REQUEST_TEMPLATE.md` — PR checklist aligned to workflow constraints.
- `Final_Analysis_Archive/` — curated archive of the final results and supporting artifacts.
- `Legacy_Results_Archive/` — frozen snapshot of the original messy results and source folders.
- `miRNA_qpcr_reanalysis.ipynb` — notebook scaffold (starter).
- `outputs/` — location for saved tables/figures.

## Setup

1. Create and activate a Python environment.
2. Install dependencies from `requirements.txt`.
3. Open `miRNA_qpcr_reanalysis.ipynb` and run from a fresh kernel.

## Non-negotiable workflow rules

- All observable computations must happen in notebook cells.
- No hidden preprocessing or off-notebook scripts.
- Use leakage-safe logic for feature selection and classification.
- Label exploratory analyses clearly.
- Document ambiguities and limitations explicitly.

See `AGENTS.md` and `miRNA-qPCR-reanalysis.md` for full policy details.

## Contributing

Before opening a PR, make sure:

- Required files are present and unchanged constraints are respected.
- Notebook logic remains reproducible from a clean runtime.
- Major outputs are saved to `outputs/`.
- Interpretation language is evidence-calibrated (robust vs fragile claims).

## Archives

- Use `Final_Analysis_Archive/` for organized review, reporting, and traceability.
- Use `Legacy_Results_Archive/` only for historical comparison against the original messy layout.
- Keep `outputs/` as the live working directory, then curate new results into `Final_Analysis_Archive/` and clean `outputs/` afterward.
