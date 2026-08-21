"""
Read and inspect raw CSV files for basic data quality checks.
"""

from pathlib import Path

import pandas as pd


RAW_DATA_PATH = Path("data/raw")


def inspect_csv_files(data_path=RAW_DATA_PATH):
    """Display basic information about CSV files in the raw data folder."""

    if not data_path.exists():
        raise FileNotFoundError(f"Data folder not found: {data_path}")

    csv_files = sorted(data_path.glob("*.csv"))

    if not csv_files:
        raise FileNotFoundError(f"No CSV files found in: {data_path}")

    for file_path in csv_files:
        try:
            df = pd.read_csv(file_path)

            print(f"\nFile: {file_path.name}")
            print(f"Shape: {df.shape}")

            print("\nData Types:")
            print(df.dtypes)

            print("\nFirst 5 Rows:")
            print(df.head())

            print("\nMissing Values:")
            print(df.isnull().sum())

            print("\nDuplicate Rows:")
            print(df.duplicated().sum())

            print("-" * 50)

        except Exception as error:
            print(f"Error reading {file_path.name}: {error}")


if __name__ == "__main__":
    inspect_csv_files()