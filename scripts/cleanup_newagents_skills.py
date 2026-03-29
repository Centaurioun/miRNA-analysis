from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
import csv
import shutil
import re

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "NewAgents-Skills"
AGENTS = BASE / "Agents"
SKILLS = BASE / "Skills"
QUAR = BASE / "To-Be-Deleted"
REPORTS = BASE / "_cleanup_reports"

RUN_ID = datetime.now().strftime("%Y%m%d_%H%M%S")


@dataclass
class ItemRecord:
    source: Path
    item_type: str
    size_bytes: int
    mtime_iso: str


@dataclass
class MovePlan:
    source: Path
    destination: Path
    action: str  # keep, normalize, quarantine
    category: str
    rationale: str


def ensure_paths() -> None:
    AGENTS.mkdir(parents=True, exist_ok=True)
    SKILLS.mkdir(parents=True, exist_ok=True)
    QUAR.mkdir(parents=True, exist_ok=True)
    REPORTS.mkdir(parents=True, exist_ok=True)


def dir_size(path: Path) -> int:
    if path.is_file():
        return path.stat().st_size
    total = 0
    for p in path.rglob("*"):
        if p.is_file():
            try:
                total += p.stat().st_size
            except OSError:
                pass
    return total


def mtime_iso(path: Path) -> str:
    return datetime.fromtimestamp(path.stat().st_mtime).isoformat(timespec="seconds")


def inventory_items() -> list[ItemRecord]:
    records: list[ItemRecord] = []
    for root in (AGENTS, SKILLS):
        for category in sorted([p for p in root.iterdir() if p.is_dir()]):
            for item in sorted([p for p in category.iterdir()]):
                if not item.exists():
                    continue
                records.append(
                    ItemRecord(
                        source=item,
                        item_type="dir" if item.is_dir() else "file",
                        size_bytes=dir_size(item),
                        mtime_iso=mtime_iso(item),
                    )
                )
    return records


def sanitize_name(name: str) -> str:
    return re.sub(r"[^A-Za-z0-9._-]+", "-", name).strip("-") or "item"


def unique_destination(dest: Path) -> Path:
    if not dest.exists():
        return dest
    i = 1
    while True:
        candidate = dest.with_name(f"{dest.name}__dup{i}")
        if not candidate.exists():
            return candidate
        i += 1


def normalize_agent_target(category: str, name: str) -> tuple[str, str, str]:
    n = name.lower()

    if category == "Orchestration-Planning":
        return "Agents/Orchestration-Planning", "keep", "Already canonical keep category"
    if category == "Research-Scientific":
        return "Agents/Research-Scientific", "keep", "Already canonical keep category"
    if category == "Data-Analysis-Modeling":
        return "Agents/Data-Analysis", "normalize", "Category normalization rule: Data-Analysis-Modeling -> Data-Analysis"

    # selective keeps from Quality-Review-Testing
    if category == "Quality-Review-Testing":
        if "biostat" in n:
            return "Agents/Statistics", "normalize", "Biostat reviewer mapped to Statistics"
        if "data-qa" in n or "dataqa" in n:
            return "Agents/Data-Processing-Cleaning", "normalize", "QA mapped to Data-Processing-Cleaning"
        if "leakage" in n or "interpretation" in n:
            return "Agents/Data-Analysis", "normalize", "Model/interpretation quality mapped to Data-Analysis"

    return f"To-Be-Deleted/Agents/{category}", "quarantine", "Not in canonical keep categories"


def normalize_skill_target(category: str, name: str) -> tuple[str, str, str]:
    n = name.lower()

    if category == "Research-Literature":
        return "Skills/Research-Literature", "keep", "Already canonical keep category"
    if category == "Data-Processing-Cleaning":
        return "Skills/Data-Processing-Cleaning", "keep", "Already canonical keep category"
    if category == "Visualization-Reporting":
        return "Skills/Data-Visualization", "normalize", "Category normalization rule: Visualization-Reporting -> Data-Visualization"
    if category == "Statistical-Modeling":
        # place all in Statistics to satisfy keep categories
        return "Skills/Statistics", "normalize", "Category normalization rule: Statistical-Modeling -> Statistics"

    if category == "Biomedical-Bioinformatics":
        # retain a small defensible shortlist by direct relevance
        if any(k in n for k in [
            "statistical-modeling",
            "multiple-testing",
            "model-validation",
            "survival-analysis",
            "small-rna-seq-differential-mirna",
            "scientific-critical-thinking",
            "peer-review",
            "chart-visualization",
            "data-analysis",
            "statistical-analysis",
        ]):
            if "visual" in n or "chart" in n:
                return "Skills/Data-Visualization", "normalize", "High relevance shortlist item mapped to Data-Visualization"
            if any(k in n for k in ["literature", "citation", "pubmed", "research"]):
                return "Skills/Research-Literature", "normalize", "High relevance shortlist item mapped to Research-Literature"
            if any(k in n for k in ["multiple-testing", "statistical", "survival", "model-validation"]):
                return "Skills/Statistics", "normalize", "High relevance shortlist item mapped to Statistics"
            return "Skills/Data-Analysis", "normalize", "High relevance shortlist item mapped to Data-Analysis"

        return "To-Be-Deleted/Skills/Biomedical-Bioinformatics", "quarantine", "Outside canonical keep categories for this cleanup phase"

    return f"To-Be-Deleted/Skills/{category}", "quarantine", "Not in canonical keep categories"


def build_move_plan(records: list[ItemRecord]) -> list[MovePlan]:
    plans: list[MovePlan] = []
    for rec in records:
        rel = rec.source.relative_to(BASE)
        parts = rel.parts
        if len(parts) < 3:
            continue
        top, category, name = parts[0], parts[1], parts[2]

        if top == "Agents":
            target_rel, action, rationale = normalize_agent_target(category, name)
        else:
            target_rel, action, rationale = normalize_skill_target(category, name)

        dest = BASE / target_rel / sanitize_name(name)
        plans.append(MovePlan(source=rec.source, destination=dest, action=action, category=target_rel, rationale=rationale))
    return plans


def write_csv(path: Path, rows: list[dict], fieldnames: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        for r in rows:
            w.writerow(r)


def execute_moves(plans: list[MovePlan]) -> tuple[list[dict], list[dict], list[dict]]:
    executed: list[dict] = []
    rollback: list[dict] = []
    retained: list[dict] = []

    for plan in plans:
        src = plan.source
        if not src.exists():
            continue

        # keep in place
        if plan.action == "keep" and src.parent == plan.destination.parent:
            retained.append(
                {
                    "path": str(src.relative_to(BASE)),
                    "category": plan.category,
                    "reason": plan.rationale,
                }
            )
            continue

        plan.destination.parent.mkdir(parents=True, exist_ok=True)
        dest = unique_destination(plan.destination)
        shutil.move(str(src), str(dest))

        executed.append(
            {
                "source": str(src.relative_to(BASE)),
                "destination": str(dest.relative_to(BASE)),
                "action": plan.action,
                "category": plan.category,
                "rationale": plan.rationale,
                "collision_resolved": "yes" if dest.name != plan.destination.name else "no",
            }
        )
        rollback.append(
            {
                "destination": str(dest.relative_to(BASE)),
                "original_source": str(src.relative_to(BASE)),
            }
        )

    return executed, rollback, retained


def main() -> None:
    ensure_paths()

    # preflight inventory
    records = inventory_items()
    pre_rows = [
        {
            "path": str(r.source.relative_to(BASE)),
            "type": r.item_type,
            "size_bytes": r.size_bytes,
            "last_modified": r.mtime_iso,
        }
        for r in records
    ]
    pre_file = REPORTS / f"inventory_manifest_{RUN_ID}.csv"
    write_csv(pre_file, pre_rows, ["path", "type", "size_bytes", "last_modified"])

    # dry run plan
    plans = build_move_plan(records)
    dry_rows = [
        {
            "source": str(p.source.relative_to(BASE)),
            "destination": str(p.destination.relative_to(BASE)),
            "action": p.action,
            "category": p.category,
            "rationale": p.rationale,
        }
        for p in plans
    ]
    dry_file = REPORTS / f"dry_run_move_plan_{RUN_ID}.csv"
    write_csv(dry_file, dry_rows, ["source", "destination", "action", "category", "rationale"])

    # execute
    executed, rollback, retained = execute_moves(plans)

    executed_file = REPORTS / f"executed_moves_{RUN_ID}.csv"
    rollback_file = REPORTS / f"rollback_map_{RUN_ID}.csv"
    retained_file = REPORTS / f"retained_items_{RUN_ID}.csv"

    write_csv(executed_file, executed, ["source", "destination", "action", "category", "rationale", "collision_resolved"])
    write_csv(rollback_file, rollback, ["destination", "original_source"])
    write_csv(retained_file, retained, ["path", "category", "reason"])

    # post validation summary
    keep_exists = all((BASE / c).exists() for c in [
        "Agents/Research-Scientific",
        "Agents/Orchestration-Planning",
        "Skills/Research-Literature",
        "Skills/Data-Processing-Cleaning",
        "Skills/Statistics",
        "Skills/Data-Visualization",
        "Skills/Data-Analysis",
    ])

    summary_file = REPORTS / f"summary_{RUN_ID}.txt"
    summary_file.write_text(
        "\n".join(
            [
                f"run_id={RUN_ID}",
                f"inventory_count={len(pre_rows)}",
                f"planned_moves={len(dry_rows)}",
                f"executed_moves={len(executed)}",
                f"retained={len(retained)}",
                f"rollback_entries={len(rollback)}",
                f"keep_paths_exist={keep_exists}",
                f"reports_dir={REPORTS}",
                f"inventory_manifest={pre_file.name}",
                f"dry_run_plan={dry_file.name}",
                f"executed_moves_file={executed_file.name}",
                f"rollback_map_file={rollback_file.name}",
                f"retained_items_file={retained_file.name}",
            ]
        ),
        encoding="utf-8",
    )

    print(f"Cleanup run complete: {RUN_ID}")
    print(f"Inventory items: {len(pre_rows)}")
    print(f"Executed moves: {len(executed)}")
    print(f"Rollback entries: {len(rollback)}")
    print(f"Summary: {summary_file}")


if __name__ == "__main__":
    main()
