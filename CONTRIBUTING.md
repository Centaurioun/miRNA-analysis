# Contributing

Thanks for contributing to `miRNA-analysis`.

## Before you start

Read these files first:

1. `AGENTS.md`
2. `miRNA-qPCR-reanalysis.md`
3. `README.md`

## Project rules (must follow)

- Keep all observable computations inside notebook cells.
- Do not add hidden preprocessing scripts for core analysis.
- Preserve fixed groups exactly (`S`, `G`, `P`).
- Preserve fixed tasks exactly (`S vs G`, `G vs P`, `S vs P`).
- Keep modeling and feature-selection logic leakage-safe.
- Label exploratory analyses explicitly.
- Save major artifacts in `outputs/`.

## Development workflow

- Make focused, reviewable changes.
- Document assumptions and discrepancies in the notebook when needed.
- Keep interpretation language calibrated to evidence.

## Pull requests

Use the repository PR template and ensure all checklist items are completed.

## Issues

Use the issue templates for bug reports and feature requests.
