#!/usr/bin/env python3
"""Validate required-field completeness for team review-agent records.

Supported agents:
- data-qa-auditor
- modeling-leakage-auditor
- interpretation-reviewer
- spec-mapper

Input formats:
1) YAML/JSON object with `records: [...]`
2) YAML/JSON list of record objects
3) YAML/JSON single record object

Exit code:
- 0: all records contain all required fields with non-empty values
- 1: one or more records are missing required fields or contain empty values
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

REQUIRED_FIELDS: dict[str, list[str]] = {
    "data-qa-auditor": [
        "Issue_ID",
        "Status",
        "Check class",
        "Issue scope",
        "Evidence location",
        "Issue",
        "Evidence",
        "Source columns",
        "Transformation rule",
        "Propagation risk",
        "Blocking level",
        "Impact level",
        "Affected tasks",
        "Downstream breakage if unresolved",
        "Notebook action",
        "Required notebook action",
        "Recompute required",
        "Claim ceiling impact",
        "Cross-review handoff",
        "Log destination",
    ],
    "modeling-leakage-auditor": [
        "Status",
        "Task",
        "Pipeline stage",
        "Evidence location",
        "Observed evidence",
        "Missing evidence",
        "Leakage risk",
        "Blocking level",
        "Severity",
        "Metric validity status",
        "Evidence",
        "Notebook action",
        "Safe redesign template",
        "Fix",
        "Re-run required",
        "Residual risk after fix",
        "Claim ceiling impact",
        "Maximum defensible claim after current audit",
        "Claim downgrade needed",
    ],
    "interpretation-reviewer": [
        "Claim_ID",
        "Status",
        "Claim",
        "Claim type",
        "Label",
        "Primary evidence location",
        "Evidence location",
        "Blocking level",
        "QA dependency",
        "Statistics dependency",
        "Leakage dependency",
        "Unsupported because",
        "Alternative explanations",
        "Claim action",
        "Notebook action",
        "Claim ceiling impact",
        "Maximum defensible wording",
        "What would upgrade this claim",
        "Required caveat text",
        "Interpretive blocker",
    ],
    "spec-mapper": [
        "Directive_ID",
        "Directive summary",
        "Notebook section target",
        "Completion criteria",
        "Dependencies",
        "Status",
        "Blocker evidence",
    ],
}


def _load_data(path: Path) -> Any:
    text = path.read_text(encoding="utf-8")

    try:
        return json.loads(text)
    except json.JSONDecodeError:
        pass

    try:
        import yaml  # type: ignore
    except Exception as exc:
        raise ValueError(
            "Input is not valid JSON, and PyYAML is not available for YAML parsing. "
            "Install PyYAML or provide JSON input."
        ) from exc

    data = yaml.safe_load(text)
    if data is None:
        raise ValueError("Input file parsed to empty content.")
    return data


def _extract_records(data: Any) -> list[dict[str, Any]]:
    if isinstance(data, dict):
        if "records" in data:
            records = data["records"]
        else:
            records = [data]
    elif isinstance(data, list):
        records = data
    else:
        raise ValueError("Input must be a mapping or list of mappings.")

    if not isinstance(records, list):
        raise ValueError("`records` must be a list.")

    normalized: list[dict[str, Any]] = []
    for i, record in enumerate(records, start=1):
        if not isinstance(record, dict):
            raise ValueError(f"Record #{i} is not a mapping/object.")
        normalized.append(record)
    return normalized


def _is_empty(value: Any) -> bool:
    if value is None:
        return True
    if isinstance(value, str):
        return value.strip() == ""
    return False


def validate_records(agent: str, records: list[dict[str, Any]]) -> tuple[bool, list[str]]:
    required = REQUIRED_FIELDS[agent]
    errors: list[str] = []

    for idx, record in enumerate(records, start=1):
        missing = [field for field in required if field not in record]
        empty = [field for field in required if field in record and _is_empty(record[field])]

        if missing or empty:
            parts: list[str] = []
            if missing:
                parts.append(f"missing={missing}")
            if empty:
                parts.append(f"empty={empty}")
            errors.append(f"record#{idx}: " + " ; ".join(parts))

    return (len(errors) == 0, errors)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Validate required-field completeness for team review-agent records."
    )
    parser.add_argument(
        "--agent",
        required=True,
        choices=sorted(REQUIRED_FIELDS.keys()),
        help="Agent schema to validate against.",
    )
    parser.add_argument(
        "--input",
        required=True,
        help="Path to YAML or JSON file containing records.",
    )

    args = parser.parse_args()
    input_path = Path(args.input)

    if not input_path.exists():
        print(f"ERROR: Input file not found: {input_path}")
        return 1

    try:
        data = _load_data(input_path)
        records = _extract_records(data)
    except Exception as exc:
        print(f"ERROR: Failed to load records: {exc}")
        return 1

    ok, errors = validate_records(args.agent, records)
    if ok:
        print(
            f"PASS: {len(records)} record(s) validated for agent `{args.agent}`. "
            f"All required fields are present and non-empty."
        )
        return 0

    print(
        f"FAIL: {len(errors)} record(s) have required-field issues for agent `{args.agent}`:"
    )
    for err in errors:
        print(f"- {err}")
    return 1


if __name__ == "__main__":
    sys.exit(main())
