"""Basic schema and integrity checks for the AI4I dataset."""
from __future__ import annotations

import argparse
from pathlib import Path

import pandas as pd

EXPECTED_COLUMNS = {
    "Type",
    "Air temperature [K]",
    "Process temperature [K]",
    "Rotational speed [rpm]",
    "Torque [Nm]",
    "Tool wear [min]",
    "Machine failure",
}
LEAKAGE_COLUMNS = {"TWF", "HDF", "PWF", "OSF", "RNF"}


def validate_dataset(path: str | Path) -> pd.DataFrame:
    """Load the CSV and validate minimum expected schema and target values."""
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(f"Dataset not found: {path}")

    df = pd.read_csv(path)
    missing = EXPECTED_COLUMNS - set(df.columns)
    if missing:
        raise ValueError(f"Missing expected columns: {sorted(missing)}")

    if df.empty:
        raise ValueError("Dataset is empty.")

    if df["Machine failure"].isna().any():
        raise ValueError("Target contains missing values.")

    target_values = set(df["Machine failure"].dropna().unique())
    if not target_values.issubset({0, 1}):
        raise ValueError(f"Target must be binary 0/1; found: {target_values}")

    leakage_present = LEAKAGE_COLUMNS.intersection(df.columns)
    print(f"Rows: {len(df):,}")
    print(f"Columns: {len(df.columns)}")
    print(f"Target distribution:\n{df['Machine failure'].value_counts(dropna=False)}")
    print(f"Potential leakage columns (exclude from predictors): {sorted(leakage_present)}")
    print("Basic validation passed.")
    return df


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", required=True, help="Path to the downloaded AI4I CSV")
    args = parser.parse_args()
    validate_dataset(args.input)


if __name__ == "__main__":
    main()
