# miRNA Review Recovery Prompt Pack (2026-03-28)

This folder contains copy/paste prompts to resolve the blockers reported in:

- `Analysi-Review-Report-miRNA_qpcr-28-03-2026.md`

## What the report means in plain English

Your review team found:

1. **Notebook 1 (`miRNA_qpcr_reanalysis.ipynb`) is conditional**
   - Main hard issue: **material leakage risk** in searched marker/panel paths.
   - Also hard issue: **over-strong biological/clinical wording** not fully supported.

2. **Notebook 2 (`output/jupyter-notebook/2026-03-28-session-statistical-review-reproduction.ipynb`) is blocked**
   - Main hard issue: **QA/provenance dependency blocker** (key adjudication still depends on upstream artifacts / incomplete rerun closeout).

## Priority order (must follow)

- **P0 first**
  1. Unblock Notebook 2 QA/provenance
  2. Fix Notebook 1 leakage in searched workflows
  3. Downgrade unsupported biological/clinical claims

- **P1 second**
  4. Add assumption diagnostics, multiplicity families, uncertainty hardening

- **P2 third (optional but recommended)**
  5. Reproducibility tolerance and external-validation roadmap polish

- **Final**
  6. Strict full re-audit of both notebooks

## Files in this folder

1. `01-notebook2-p0-qa-unblock.prompt.md`
2. `02-notebook1-p0-leakage-remediation.prompt.md`
3. `03-claims-language-downgrade.prompt.md`
4. `04-statistical-hardening-p1.prompt.md`
5. `05-reproducibility-polish-p2.prompt.md`
6. `06-full-reaudit-strict.prompt.md`
7. `07-deferred-issues-closure.prompt.md`
8. `08-fresh-kernel-regeneration-and-closure-confirmation.prompt.md`

## Mandatory run artifacts

Each prompt now requires writing a step-specific markdown results file under:

- `outputs/review-recovery-2026-03-28/`

Expected files:

1. `01-notebook2-p0-qa-unblock-results.md`
2. `02-notebook1-p0-leakage-remediation-results.md`
3. `03-claims-language-downgrade-results.md`
4. `04-statistical-hardening-p1-results.md`
5. `05-reproducibility-polish-p2-results.md`
6. `06-full-reaudit-strict-results.md`
7. `07-deferred-issues-closure-results.md`
8. `08-fresh-kernel-regeneration-and-closure-confirmation-results.md`

Each results file must include a `Deferred Issues` section.
If nothing is deferred, it must still state: `Deferred Issues: none`.

## How to use

Open each file in order and paste the full prompt into your main UI agent (recommended: `miRNA Reanalysis Coordinator`).

If Step 06 still reports deferred issues or any P0 blocker, run Step 07 immediately.

If Step 07 still reports deferred issues (especially placeholder/provisional artifacts), run Step 08 to force fresh-kernel regeneration and parity confirmation.

Do not skip order. Later prompts assume outputs from earlier ones.

## Completion definition

You are done when:

- Notebook 2 no longer has high QA/provenance blockers.
- Notebook 1 searched workflows are leakage-safe and rerun with updated OOF metrics.
- Biological/clinical claims are capped to defensible wording.
- Final strict re-audit returns no P0 blockers.

## Why this matters

The per-step markdown artifacts create a durable audit trail and make unresolved items explicit instead of getting lost in chat history.
