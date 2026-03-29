# Review Team Handoff Vocabulary

This file defines shared wording and enum-style values for the review team:

- `Data QA Auditor`
- `Modeling Leakage Auditor`
- `Interpretation Reviewer`
- `Spec Mapper`
- (and downstream coordinator synthesis)

Use these terms to reduce cross-agent ambiguity.

## 1) Shared status language

Use these values consistently:

- `completed`
- `partial`
- `blocked`

Interpretation:
- `completed`: enough visible evidence for deterministic disposition.
- `partial`: some evidence is missing, but actionable remediation is possible.
- `blocked`: required evidence is missing such that reliable adjudication cannot proceed.

## 2) Shared triage axis

Use these values for blocking-style gates:

- `none`
- `low`
- `moderate`
- `high`
- `critical`

Calibration:
- `none`: documentation/format cleanup only.
- `low`: limited local risk; interpretation possible with caveat.
- `moderate`: substantive defect requiring notebook correction.
- `high`: major defect likely to invalidate key downstream claims.
- `critical`: core integrity failure; downstream use should halt.

## 3) Shared dependency state tokens

For dependency fields (e.g., `QA dependency`, `Statistics dependency`, `Leakage dependency`), use:

- `resolved`
- `open`
- `blocked`
- `none`

## 4) Shared cross-review handoff tokens

For handoff fields (e.g., `Cross-review handoff`), use these canonical tokens:

- `none`
- `data-qa-auditor`
- `modeling-leakage-auditor`
- `interpretation-reviewer`
- `spec-mapper`
- `biostatistics-reviewer`
- `miRNA-reanalysis-coordinator`

If multiple handoffs apply, use comma-separated canonical tokens.

## 5) Shared claim-ceiling phrasing pattern

When unresolved defects remain, use this pattern:

- `Claim ceiling impact`: `Until <defect> is resolved, limit interpretation to <ceiling>.`
- `Maximum defensible wording`: concise ceiling sentence with no causal overreach.

## 6) Evidence location format

Prefer this format for anchor clarity:

- `<file path> :: <section/cell/output anchor>`

Examples:
- `miRNA_qpcr_reanalysis.ipynb :: Section 12 correlation heatmap output`
- `miRNA_qpcr_reanalysis.ipynb :: Task 2 CV metrics table`

## 7) Machine-readable output contract

When an agent supports `output_mode = yaml|both`, emit:

- root key: `records`
- value: list of mappings
- mapping keys: exact required output field names for that agent

No field omissions; use `none` when a field has no issue.

## 8) Optional completeness checker

Use `scripts/validate_agent_review_records.py` to verify required fields are present for each agent's machine-readable output.
