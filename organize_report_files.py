import os
import shutil
from pathlib import Path
import glob

def organize_report_files():
    # Define directories
    base_dir = Path("/Users/centaurioun/Repos/miRNA-analysis")
    outputs_dir = base_dir / "outputs"
    target_dir = outputs_dir / "miRNA-ipynb-analysis-results-reports-29-03-2026"

    # Define sub-folder structure
    subfolders = {
        "data_and_inputs": [
            "miRNA-qPCR-analysis-results.csv",
            "miRNA-qPCR-reanalysis.md"
        ],
        "scripts_and_notebooks": [
            "miRNA_qpcr_reanalysis.ipynb"
        ],
        "analysis_results/01_data_qa_and_provenance": [
            "outputs/input_registry.csv",
            "outputs/missingness_listwise_impact.csv",
            "outputs/gapdh_*.csv",
            "outputs/transformation_log.csv"
        ],
        "analysis_results/02_leakage_remediation": [
            "outputs/task_model_performance_nestedcv.csv",
            "outputs/searched_panel_*.csv",
            "outputs/threshold_sensitivity_oof.csv",
            "outputs/calibration_oof_diagnostics.csv",
            "outputs/single_vs_panel_summary.csv"
        ],
        "analysis_results/03_statistical_hardening": [
            "outputs/permutation_*.csv",
            "outputs/bootstrap_*.csv",
            "outputs/taskwise_*.csv",
            "outputs/multiplicity_family_registry.csv"
        ],
        "analysis_results/04_clinical_and_eda": [
            "outputs/clinical_*.csv",
            "outputs/exploratory_pca_variance.csv",
            "outputs/summary_by_group.csv",
            "outputs/confounding_and_broader_comparisons.csv"
        ],
        "analysis_results/05_audit_ledgers": [
            "outputs/assumption_ledger.csv",
            "outputs/completion_map.csv",
            "outputs/p2_reproducibility_artifact_check.csv",
            "outputs/results_registry.csv",
            "outputs/discrepancy_log.csv",
            "outputs/model_comparison_family_registry.csv"
        ]
    }

    # Execute copies
    copied_count = 0
    missing_files = []

    for folder_name, patterns in subfolders.items():
        # Create the subfolder safely
        dest_path = target_dir / folder_name
        dest_path.mkdir(parents=True, exist_ok=True)

        for pattern in patterns:
            # Resolve glob patterns relative to the base directory
            matched_files = glob.glob(str(base_dir / pattern))

            if not matched_files:
                missing_files.append(pattern)
                continue

            for file_path in matched_files:
                src_file = Path(file_path)
                if src_file.is_file():
                    try:
                        shutil.copy2(src_file, dest_path / src_file.name)
                        copied_count += 1
                        print(f"Copied: {src_file.name} -> {folder_name}/")
                    except Exception as e:
                        print(f"Failed to copy {src_file.name}: {e}")

    print("\n" + "="*50)
    print(f"Transfer Complete! Successfully copied {copied_count} files.")
    print(f"Organized structure is located at: {target_dir.relative_to(base_dir)}")

    if missing_files:
        print("\nNote: The following patterns did not match any files:")
        for miss in missing_files:
            print(f" - {miss}")

if __name__ == "__main__":
    organize_report_files()