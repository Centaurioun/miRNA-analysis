from __future__ import annotations

import csv
import hashlib
import json
import os
import shutil
import traceback
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, Iterable, List

import pandas as pd

ROOT = Path('/Users/centaurioun/Repos/miRNA-analysis')
ARCHIVE = ROOT / 'Final_Analysis_Archive'
MANIFEST_PATH = ARCHIVE / 'migration_manifest.json'
AUDIT_PATH = ARCHIVE / 'organization_audit.log'
REPORT_PATH = ARCHIVE / 'Final_Reanalysis_Executive_Summary.md'
README_PATH = ARCHIVE / 'README.md'

CATEGORIES = {
    '01_Methodological_Reports': ARCHIVE / '01_Methodological_Reports',
    '02_Model_Diagnostics': ARCHIVE / '02_Model_Diagnostics',
    '03_Assumption_Ledgers': ARCHIVE / '03_Assumption_Ledgers',
    '04_Artifact_Parity_Checks': ARCHIVE / '04_Artifact_Parity_Checks',
    '05_Execution_Logs_and_Prompts': ARCHIVE / '05_Execution_Logs_and_Prompts',
}

ROOT_ARTIFACTS = {
    '07-deferred-v2-issues-closure-results.md',
    'Analysi-Review-Report-miRNA_qpcr-28-03-2026.md',
    'jupyter_run.log',
    'miRNA_qpcr_reanalysis_report.md',
    'prompt-for-multi-agent-review-of-miRNA.md',
    'session_statistical_review_reproduction_2026-03-28.md',
}

SOURCE_PREFIXES = (
    'outputs/',
    'review-recovery-2026-03-28/',
    'prompts/review-recovery-2026-03-28/',
)

CSV_EXTENSIONS = {'.csv'}
TEXT_EXTENSIONS = {'.md', '.log'}


def timestamp() -> str:
    return datetime.now(timezone.utc).isoformat(timespec='seconds')


def write_audit(action: str, source: str, destination: str, status: str) -> None:
    AUDIT_PATH.parent.mkdir(parents=True, exist_ok=True)
    line = f'[{timestamp()}] | [{action}] | [{source}] | [{destination}] | [{status}]\n'
    with AUDIT_PATH.open('a', encoding='utf-8') as handle:
        handle.write(line)


def clean_name(rel_path: Path) -> str:
    base = rel_path.as_posix().replace('/', '__').replace(' ', '_')
    if len(base) > 180:
        digest = hashlib.sha1(base.encode('utf-8')).hexdigest()[:10]
        base = f'{rel_path.stem}__{digest}{rel_path.suffix}'
    return base


def is_target_source(path: Path) -> bool:
    if path.suffix.lower() not in CSV_EXTENSIONS.union(TEXT_EXTENSIONS):
        return False
    rel = path.relative_to(ROOT).as_posix()
    if rel.startswith(SOURCE_PREFIXES):
        return True
    return path.name in ROOT_ARTIFACTS


def categorize(path: Path) -> str:
    rel = path.relative_to(ROOT).as_posix()
    name = path.name.lower()

    if rel.startswith('prompts/review-recovery-2026-03-28/') or 'prompt' in name or name.endswith('.prompt.md') or 'chat-log' in name or 'chat-logs' in name or name.endswith('.log'):
        return '05_Execution_Logs_and_Prompts'

    if any(token in name for token in ['assumption_ledger', 'discrepancy_log', 'input_registry', 'transformation_log', 'provenance_map']):
        return '03_Assumption_Ledgers'

    if any(token in name for token in ['completion_map', 'results_registry', 'model_comparison_family_registry', 'multiplicity_family_registry', 'p2_reproducibility_artifact_check', 'qa_gate_results_reproduced', 'claim_classification', 'revision_checklist', 'pending_checks', 'closeout_summary', 'tolerance_summary']):
        return '04_Artifact_Parity_Checks'

    if rel.startswith('review-recovery-2026-03-28/') or rel.startswith('outputs/review-recovery-2026-03-28/') or rel.startswith('outputs/review-recovery-2026-03-28-backup/'):
        if name.endswith('.md'):
            return '01_Methodological_Reports'
        return '05_Execution_Logs_and_Prompts'

    diagnostic_tokens = [
        'bootstrap_', 'calibration_', 'clinical_', 'confounding_', 'exploratory_pca_',
        'gapdh_', 'missingness_', 'model_comparison_', 'multiplicity_', 'permutation_',
        'searched_panel_', 'single_vs_panel_', 'summary_by_group', 'task_model_',
        'taskwise_', 'threshold_', 'q01_', 'q02_', 'q03_', 'q05_', 'q06_', 'q07_', 'q08_',
        'p1_listwise_', 'p2_tolerance_', 'q09_', 'qa_gate_',
    ]
    if any(token in name for token in diagnostic_tokens):
        if 'q09_' in name or 'qa_gate' in name:
            return '04_Artifact_Parity_Checks'
        return '02_Model_Diagnostics'

    if name.endswith('.md'):
        return '01_Methodological_Reports'

    return '04_Artifact_Parity_Checks'


def destination_for(source: Path) -> Path:
    return CATEGORIES[categorize(source)] / clean_name(source.relative_to(ROOT))


def collect_sources() -> List[Path]:
    candidates: List[Path] = []
    for path in ROOT.rglob('*'):
        if not path.is_file():
            continue
        if not is_target_source(path):
            continue
        rel = path.relative_to(ROOT).as_posix()
        if rel in ROOT_ARTIFACTS or rel.startswith(SOURCE_PREFIXES):
            candidates.append(path)
    # Explicitly include the output copies of the governing inputs that sit inside the outputs archive tree.
    candidates = sorted(set(candidates))
    return candidates


def build_manifest(sources: Iterable[Path]) -> List[Dict[str, str]]:
    manifest: List[Dict[str, str]] = []
    for source in sources:
        category = categorize(source)
        destination = destination_for(source)
        manifest.append({
            'old_file_path': str(source),
            'new_file_path': str(destination),
            'category': category,
        })
    return manifest


def copy_manifest(manifest: List[Dict[str, str]]) -> None:
    for item in manifest:
        source = Path(item['old_file_path'])
        destination = Path(item['new_file_path'])
        destination.parent.mkdir(parents=True, exist_ok=True)
        try:
            shutil.copy2(source, destination)
            write_audit('COPY', str(source), str(destination), 'OK')
        except Exception as exc:  # pragma: no cover - logged for human inspection
            write_audit('COPY', str(source), str(destination), f'ERROR: {exc}')
            write_audit('TRACEBACK', str(source), str(destination), traceback.format_exc().replace('\n', ' | '))


def csv_headers(path: Path) -> List[str]:
    try:
        with path.open('r', encoding='utf-8', newline='') as handle:
            reader = csv.reader(handle)
            return next(reader, [])
    except Exception:
        return []


def build_folder_readme(folder: Path, title: str, purpose: str, provenance: str) -> str:
    files = sorted([p for p in folder.iterdir() if p.is_file()])
    csv_files = [p for p in files if p.suffix.lower() == '.csv']
    md_files = [p for p in files if p.suffix.lower() == '.md']
    log_files = [p for p in files if p.suffix.lower() == '.log']

    lines = [
        f'# {title}',
        '',
        f'**Purpose.** {purpose}',
        '',
        f'**Provenance.** {provenance}',
        '',
        '## Contents',
        '',
        f'- CSV files: {len(csv_files)}',
        f'- Markdown files: {len(md_files)}',
        f'- Log files: {len(log_files)}',
        '',
    ]

    if csv_files:
        lines.extend(['## Data dictionary', '', '| File | Columns |', '| --- | --- |'])
        for csv_path in csv_files:
            headers = csv_headers(csv_path)
            col_text = ', '.join(headers) if headers else 'Unable to parse headers'
            lines.append(f'| `{csv_path.name}` | {col_text} |')
        lines.append('')

    if md_files:
        lines.extend(['## Narrative artifacts', ''])
        for md_path in md_files:
            lines.append(f'- `{md_path.name}`')
        lines.append('')

    if log_files:
        lines.extend(['## Execution logs', ''])
        for log_path in log_files:
            lines.append(f'- `{log_path.name}`')
        lines.append('')

    return '\n'.join(lines).rstrip() + '\n'


def write_readmes() -> None:
    ARCHIVE.mkdir(parents=True, exist_ok=True)
    root_readme = [
        '# Final Analysis Archive',
        '',
        'This directory is a copied, auditable archive of the miRNA-qPCR reanalysis artifacts.',
        '',
        '## Layout',
        '',
        '- `01_Methodological_Reports/` — narrative reports, closeout summaries, and technical write-ups.',
        '- `02_Model_Diagnostics/` — model performance, robustness, calibration, and clinical association diagnostics.',
        '- `03_Assumption_Ledgers/` — assumption, transformation, discrepancy, and provenance ledgers.',
        '- `04_Artifact_Parity_Checks/` — QA, parity, reproducibility, and closeout confirmation artifacts.',
        '- `05_Execution_Logs_and_Prompts/` — prompts, chat logs, and execution records.',
        '',
        '## Navigation tips',
        '',
        'Start with the parity checks for final status, then move to model diagnostics for performance and robustness, and finish with the methodological reports for the narrative closeout.',
        '',
        'All files were copied with their source-path context encoded into the filename so the archive remains collision-free and traceable.',
        '',
    ]
    README_PATH.write_text('\n'.join(root_readme), encoding='utf-8')

    folder_meta = {
        '01_Methodological_Reports': (
            'Methodological reports and synthesis documents.',
            'Derived from final report outputs, reviewer-facing summaries, and closeout narrative artifacts.',
        ),
        '02_Model_Diagnostics': (
            'Model diagnostics, validation summaries, and robustness checks.',
            'Derived from nested-CV, bootstrap, permutation, calibration, and clinical association result files.',
        ),
        '03_Assumption_Ledgers': (
            'Assumption tracking and transformation provenance.',
            'Derived from ledger-style outputs that document assumptions, transformations, and discrepancy handling.',
        ),
        '04_Artifact_Parity_Checks': (
            'Parity, QA, and reproducibility confirmation artifacts.',
            'Derived from closeout checks, artifact inventories, completion maps, and final decision logs.',
        ),
        '05_Execution_Logs_and_Prompts': (
            'Prompts, chat logs, and execution records.',
            'Derived from review prompts, chat log exports, and run-time log files.',
        ),
    }

    for name, folder in CATEGORIES.items():
        readme = build_folder_readme(folder, name.replace('_', ' '), *folder_meta[name])
        (folder / 'README.md').write_text(readme, encoding='utf-8')


def write_manifest(manifest: List[Dict[str, str]]) -> None:
    MANIFEST_PATH.write_text(json.dumps(manifest, indent=2, ensure_ascii=False), encoding='utf-8')
    write_audit('MANIFEST', str(MANIFEST_PATH), str(MANIFEST_PATH), f'Created {len(manifest)} entries')


def validate_manifest(manifest: List[Dict[str, str]]) -> List[str]:
    missing = []
    for item in manifest:
        destination = Path(item['new_file_path'])
        if not destination.exists() or destination.stat().st_size <= 0:
            missing.append(item['new_file_path'])
    return missing


def build_report() -> None:
    task_perf = pd.read_csv(destination_for(ROOT / 'outputs/task_model_performance_nestedcv.csv'))
    results = pd.read_csv(destination_for(ROOT / 'outputs/results_registry.csv'))
    q09 = pd.read_csv(destination_for(ROOT / 'outputs/session-statistical-review/q09_closeout_summary.csv'))
    claims = pd.read_csv(destination_for(ROOT / 'outputs/session-statistical-review/q09_claim_classification.csv'))

    def best_task_row(task: str) -> pd.Series:
        sub = task_perf[task_perf['Task'] == task].copy()
        return sub.sort_values(['AUC', 'Accuracy'], ascending=False).iloc[0]

    best_rows = [best_task_row(task) for task in ['Task1_S_vs_G', 'Task2_G_vs_P', 'Task3_S_vs_P']]
    best_table = pd.DataFrame([
        {
            'Task': row['Task'],
            'Best model family': row['Model_Family'],
            'Model label': row.get('Model_Label', row.get('model_label', '')),
            'AUC': row['AUC'],
            'Accuracy': row['Accuracy'],
            'Sensitivity': row['Sensitivity'],
            'Specificity': row['Specificity'],
        }
        for row in best_rows
    ])

    report_lines = [
        '# Final Reanalysis Executive Summary',
        '',
        '## KPI dashboard',
        '',
        '| Metric | Value |',
        '| --- | --- |',
        f"| Final decision | {q09.loc[q09['Question'] == 'Final decision', 'Answer'].iloc[0]} |",
        f"| Confirmation from reviewer closeout | {q09.loc[q09['Question'] == 'Does this confirm the notebook result?', 'Answer'].iloc[0]} |",
        f"| Missingness / attrition gate | {q09.loc[q09['Question'] == 'Missingness/attrition gate pass', 'Answer'].iloc[0]} |",
        f"| Most harmful age fraction under q07 | {q09.loc[q09['Question'] == 'q07 AGE most_harmful_fraction', 'Answer'].iloc[0]} |",
        f"| Task2 delta median (q03) | {q09.loc[q09['Question'] == 'q03 Task2 delta_median', 'Answer'].iloc[0]} |",
        f"| Task3 delta median (q03) | {q09.loc[q09['Question'] == 'q03 Task3 delta_median', 'Answer'].iloc[0]} |",
        f"| Task2 delta median (q05) | {q09.loc[q09['Question'] == 'q05 Task2 delta_median', 'Answer'].iloc[0]} |",
        f"| Task3 delta median (q05) | {q09.loc[q09['Question'] == 'q05 Task3 delta_median', 'Answer'].iloc[0]} |",
        '',
        '## Best internal classifiers by task',
        '',
        best_table.to_markdown(index=False),
        '',
        '## Initial problem state',
        '',
        'The dataset began with a leakage concern: apparent discrimination was vulnerable to reference-gene instability, broader Ct structure, and selection-affected model search. The analysis therefore hardened the workflow with nested cross-validation, explicit FDR control, permutation checks, and repeated robustness/attrition checks.',
        '',
        '## Methodological interventions',
        '',
        '- Nested CV with in-fold tuning and OOF summaries for the main classifiers.',
        '- Benjamini-Hochberg FDR control for family-wise inferential reporting.',
        '- Listwise deletion accounting and explicit attrition ceilings.',
        '- Structure-control comparisons to test whether broad Ct patterns outperformed biomarker-specific panels.',
        '',
        '## Artifact traceability',
        '',
        f'- [Model diagnostics](02_Model_Diagnostics/{destination_for(ROOT / "outputs/task_model_performance_nestedcv.csv").name})',
        f'- [Assumption ledger](03_Assumption_Ledgers/{destination_for(ROOT / "outputs/assumption_ledger.csv").name})',
        f'- [Parity checks](04_Artifact_Parity_Checks/{destination_for(ROOT / "outputs/session-statistical-review/q09_closeout_summary.csv").name})',
        f'- [Prompts and logs](05_Execution_Logs_and_Prompts/{destination_for(ROOT / "prompts/review-recovery-2026-03-28/README.md").name})',
        '',
        '## Final scientific conclusions',
        '',
        claims.to_markdown(index=False),
        '',
        '### Interpretation',
        '',
        'Task 1 remains exploratory and cautiously worded. Task 2 retains strong internal separation, but the archived q03/q05 delta medians indicate limited incremental biomarker value over structure controls. Task 3 shows very strong internal discrimination, yet the broader-global and combined models indicate that apparent performance is not automatically equivalent to disease-specific biological signal. The safest conclusion is that the dataset supports strong internal classification patterns under the archived leakage-safe workflow, with interpretation constrained by structure-related signal and selection sensitivity.',
        '',
        '## Reproducibility note',
        '',
        'This archive is a copied, collision-safe snapshot. The source files remain untouched. All copied artifacts are discoverable through the manifest and the audit log, and every folder contains a local README with a data dictionary for its CSV files.',
        '',
    ]
    REPORT_PATH.write_text('\n'.join(report_lines), encoding='utf-8')


def main() -> None:
    ARCHIVE.mkdir(parents=True, exist_ok=True)
    for folder in CATEGORIES.values():
        folder.mkdir(parents=True, exist_ok=True)
    write_audit('CREATE_TREE', str(ROOT), str(ARCHIVE), 'Archive root and category folders ready')

    sources = collect_sources()
    manifest = build_manifest(sources)
    write_manifest(manifest)
    copy_manifest(manifest)

    missing = validate_manifest(manifest)
    if missing:
        write_audit('VALIDATION', str(MANIFEST_PATH), str(ARCHIVE), f'Missing {len(missing)} files after initial copy')
        copy_manifest([item for item in manifest if item['new_file_path'] in missing])
        missing = validate_manifest(manifest)
        if missing:
            write_audit('VALIDATION', str(MANIFEST_PATH), str(ARCHIVE), f'Persistent missing files: {len(missing)}')
            raise RuntimeError(f'Copy validation failed for {len(missing)} files')

    write_readmes()
    build_report()
    write_audit('COMPLETE', str(ROOT), str(ARCHIVE), f'{len(manifest)} files copied and validated')


if __name__ == '__main__':
    main()
