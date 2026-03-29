from __future__ import annotations

from collections import defaultdict
from pathlib import Path
import re
import shutil
import tempfile

ROOT = Path(__file__).resolve().parents[1]
OUT_ROOT = ROOT / "NewAgents-Skills"

EXCLUDE_PARTS = {".git", "NewAgents-Skills"}


def is_excluded(path: Path) -> bool:
    return any(part in EXCLUDE_PARTS for part in path.parts)


def sanitize_name(name: str) -> str:
    s = name.strip().lower()
    s = re.sub(r"\.agent$", "", s)
    s = re.sub(r"\.(md|markdown)$", "", s)
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    return s or "item"


def skill_category(path: Path) -> str:
    t = str(path).lower()
    if any(k in t for k in ["visual", "plot", "figure", "ggplot", "chart", "slides", "infographic"]):
        return "Visualization-Reporting"
    if any(k in t for k in ["stat", "biostat", "model", "regression", "survival", "power", "multiple-testing"]):
        return "Statistical-Modeling"
    if any(k in t for k in ["clean", "transform", "normalization", "preprocess", "qc", "duplicate"]):
        return "Data-Processing-Cleaning"
    if any(k in t for k in ["literature", "pubmed", "research", "citation", "openalex", "search"]):
        return "Research-Literature"
    if any(k in t for k in ["bio-", "omics", "rna", "gwas", "variant", "microbiome", "metabol", "proteom", "tooluniverse", "clinical"]):
        return "Biomedical-Bioinformatics"
    if any(k in t for k in ["workflow", "superpowers", "debugging", "writing-plans", "review", "agent", "mcp", "automation"]):
        return "Workflow-Tooling"
    if any(k in t for k in ["machine-learning", "scikit", "pytorch", "deep", "ai"]):
        return "Machine-Learning-AI"
    return "General"


def agent_category(path: Path) -> str:
    t = str(path).lower()
    if any(k in t for k in ["orchestrator", "coordinator", "planner", "architect", "meta", "workflow"]):
        return "Orchestration-Planning"
    if any(k in t for k in ["qa", "review", "auditor", "validator", "debug", "test"]):
        return "Quality-Review-Testing"
    if any(k in t for k in ["research", "paper", "literature", "scientific"]):
        return "Research-Scientific"
    if any(k in t for k in ["data", "analyst", "biostat", "model", "leakage"]):
        return "Data-Analysis-Modeling"
    if any(k in t for k in ["security", "sec", "compliance", "governance"]):
        return "Security-Governance"
    if any(k in t for k in ["docs", "writer", "documentation", "content"]):
        return "Documentation-Communication"
    return "Domain-Specialist"


def unique_dest(base: Path, used: set[Path]) -> Path:
    candidate = base
    n = 1
    while candidate in used or candidate.exists():
        candidate = base.with_name(f"{base.name}_{n}")
        n += 1
    used.add(candidate)
    return candidate


def discover_items() -> tuple[list[Path], list[Path], list[Path], list[Path]]:
    skill_dirs: set[Path] = set()
    loose_skill_files: list[Path] = []
    agent_files: list[Path] = []
    agent_like_files: list[Path] = []

    for p in ROOT.rglob("*"):
        if is_excluded(p) or not p.is_file():
            continue

        name = p.name
        lower = str(p).lower()

        if name == "SKILL.md":
            skill_dirs.add(p.parent)

        if name.endswith(".md") and re.search(r"(^SKILL.*\.md$|SKILL\.md$|-SKILL\.md$)", name):
            if name != "SKILL.md":
                loose_skill_files.append(p)

        if name.endswith(".agent.md"):
            agent_files.append(p)

        if name.endswith(".md") and not name.endswith(".agent.md"):
            if "/agents/" in lower or "/subagents/" in lower:
                if name.lower() not in {"readme.md", "agents.md"}:
                    agent_like_files.append(p)

    skill_dir_set = set(skill_dirs)
    loose_skill_files = sorted(
        {
            p
            for p in loose_skill_files
            if p.parent not in skill_dir_set and not is_excluded(p)
        }
    )

    agent_file_set = set(agent_files)
    agent_like_files = sorted({p for p in agent_like_files if p not in agent_file_set and not is_excluded(p)})

    return sorted(skill_dirs), loose_skill_files, sorted(set(agent_files)), agent_like_files


def copy_items(staging_root: Path) -> tuple[list[tuple[str, str, str]], list[str]]:
    (staging_root / "Agents").mkdir(parents=True, exist_ok=True)
    (staging_root / "Skills").mkdir(parents=True, exist_ok=True)

    skill_dirs, loose_skill_files, agent_files, agent_like_files = discover_items()

    used: set[Path] = set()
    index_rows: list[tuple[str, str, str]] = []
    warnings: list[str] = []

    for sdir in skill_dirs:
        try:
            cat = skill_category(sdir)
            name = sanitize_name(sdir.name)
            dest = unique_dest(staging_root / "Skills" / cat / name, used)
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.copytree(sdir, dest)
            index_rows.append(("SkillDir", str(sdir.relative_to(ROOT)), str(dest.relative_to(staging_root))))
        except Exception as exc:
            warnings.append(f"Skipped SkillDir `{sdir}`: {exc}")

    for sfile in loose_skill_files:
        try:
            cat = skill_category(sfile)
            name = sanitize_name(sfile.stem)
            dest = unique_dest(staging_root / "Skills" / cat / name, used)
            dest.mkdir(parents=True, exist_ok=True)
            shutil.copy2(sfile, dest / sfile.name)
            index_rows.append(("SkillFile", str(sfile.relative_to(ROOT)), str(dest.relative_to(staging_root))))
        except Exception as exc:
            warnings.append(f"Skipped SkillFile `{sfile}`: {exc}")

    for afile in agent_files:
        try:
            cat = agent_category(afile)
            name = sanitize_name(afile.stem)
            dest = unique_dest(staging_root / "Agents" / cat / name, used)
            dest.mkdir(parents=True, exist_ok=True)
            shutil.copy2(afile, dest / afile.name)
            index_rows.append(("AgentFile", str(afile.relative_to(ROOT)), str(dest.relative_to(staging_root))))
        except Exception as exc:
            warnings.append(f"Skipped AgentFile `{afile}`: {exc}")

    for afile in agent_like_files:
        try:
            cat = agent_category(afile)
            name = sanitize_name(afile.stem)
            dest = unique_dest(staging_root / "Agents" / cat / name, used)
            dest.mkdir(parents=True, exist_ok=True)
            shutil.copy2(afile, dest / afile.name)
            index_rows.append(("AgentLikeFile", str(afile.relative_to(ROOT)), str(dest.relative_to(staging_root))))
        except Exception as exc:
            warnings.append(f"Skipped AgentLikeFile `{afile}`: {exc}")

    return index_rows, warnings


def write_readme(staging_root: Path, index_rows: list[tuple[str, str, str]], warnings: list[str]) -> None:
    agents_count = sum(1 for r in index_rows if r[0].startswith("Agent"))
    skills_count = sum(1 for r in index_rows if r[0].startswith("Skill"))

    cats_agents: defaultdict[str, int] = defaultdict(int)
    cats_skills: defaultdict[str, int] = defaultdict(int)

    for _, _, rel_dest in index_rows:
        parts = Path(rel_dest).parts
        if parts[0] == "Agents" and len(parts) > 2:
            cats_agents[parts[1]] += 1
        if parts[0] == "Skills" and len(parts) > 2:
            cats_skills[parts[1]] += 1

    lines: list[str] = [
        "# NewAgents-Skills",
        "",
        "This directory contains a normalized copy of agent and skill artifacts discovered in the repository, organized by functionality.",
        "",
        "## Folder structure",
        "- `Agents/`: agent files organized into functional categories; each agent has its own folder.",
        "- `Skills/`: skill directories/files organized into functional categories; each skill has its own folder.",
        "",
        "## Categories used",
        "### Agents",
    ]

    for k in sorted(cats_agents):
        lines.append(f"- `{k}` ({cats_agents[k]})")

    lines.extend(["", "### Skills"])

    for k in sorted(cats_skills):
        lines.append(f"- `{k}` ({cats_skills[k]})")

    lines.extend(
        [
            "",
            "## Navigation and usage",
            "1. Start in `Agents/` or `Skills/`.",
            "2. Open a category folder matching your use case.",
            "3. Open the dedicated item folder (collision-safe names may include suffixes like `_1`, `_2`).",
            "4. Use contained files directly (e.g., `SKILL.md`, `.agent.md`, plus preserved `assets/`, `references/`, `scripts/` where present).",
            "",
            "## Summary",
            f"- Total copied agent items: **{agents_count}**",
            f"- Total copied skill items: **{skills_count}**",
            f"- Total copied items: **{len(index_rows)}**",
            "",
            "## Provenance index",
            "| Type | Source | Destination |",
            "|---|---|---|",
        ]
    )

    for typ, src, dst in sorted(index_rows):
        lines.append(f"| {typ} | `{src}` | `{dst}` |")

    if warnings:
        lines.extend(["", "## Warnings", "Some items could not be copied and were skipped:"])
        for item in warnings:
            lines.append(f"- {item}")

    (staging_root / "README.md").write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    with tempfile.TemporaryDirectory(prefix="newagents-skills-", dir=str(ROOT)) as temp_dir:
        staging_root = Path(temp_dir) / "NewAgents-Skills"
        rows, warnings = copy_items(staging_root)
        write_readme(staging_root, rows, warnings)

        if OUT_ROOT.exists():
            shutil.rmtree(OUT_ROOT)
        shutil.move(str(staging_root), str(OUT_ROOT))

    print(f"Created: {OUT_ROOT}")
    print(f"Copied items: {len(rows)}")
    print(f"Warnings: {len(warnings)}")


if __name__ == "__main__":
    main()
