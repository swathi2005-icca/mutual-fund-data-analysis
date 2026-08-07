import pandas as pd

# Read the scheme performance file
performance = pd.read_csv("data/raw/07_scheme_performance.csv")

# Show column names
print("Column Names:")
print(performance.columns)

# Show first 5 rows
print("\nFirst 5 Rows:")
print(performance.head())

# Check data types
print("\nData Types:")
print(performance.dtypes)

# Check missing values in return columns
print("\nMissing Values:")

print("Return 1 Year:", performance["return_1yr_pct"].isnull().sum())
print("Return 3 Year:", performance["return_3yr_pct"].isnull().sum())
print("Return 5 Year:", performance["return_5yr_pct"].isnull().sum())

# Check expense ratio range
invalid_expense = performance[
    (performance["expense_ratio_pct"] < 0.1) |
    (performance["expense_ratio_pct"] > 2.5)
]

print("\nNumber of invalid expense ratios:")
print(len(invalid_expense))

# Check for negative return values
anomalies = performance[
    (performance["return_1yr_pct"] < 0) |
    (performance["return_3yr_pct"] < 0) |
    (performance["return_5yr_pct"] < 0)
]

print("\nNumber of anomaly records:")
print(len(anomalies))

# Save the cleaned file
performance.to_csv("data/processed/09_scheme_performance.csv", index=False)

print("\nCleaned scheme_performance file saved successfully!")