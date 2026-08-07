import pandas as pd

nav = pd.read_csv("data/raw/02_nav_history.csv")

print("Column Names:")
print(nav.columns)

print("\nFirst 5 Rows:")
print(nav.head())

# Convert date column to datetime
nav["date"] = pd.to_datetime(nav["date"])

print("\nData Types:")
print(nav.dtypes)

# Sort the data
nav = nav.sort_values(by=["amfi_code", "date"])

print("\nData after sorting:")
print(nav.head())

# Check duplicate rows
duplicate_rows = nav.duplicated().sum()

print("\nNumber of duplicate rows:")
print(duplicate_rows)

# Remove duplicate rows
nav = nav.drop_duplicates()

print("\nDuplicate rows removed.")
print("Total rows after removing duplicates:", len(nav))

# Check for invalid NAV values
invalid_nav = nav[nav["nav"] <= 0]

print("\nNumber of invalid NAV values:")
print(len(invalid_nav))

# Check for missing NAV values
missing_nav = nav["nav"].isnull().sum()

print("\nNumber of missing NAV values:")
print(missing_nav)

# Fill missing NAV values (if any)
nav["nav"] = nav["nav"].ffill()

print("\nMissing NAV values after filling:")
print(nav["nav"].isnull().sum())

# Save the cleaned data
nav.to_csv("data/processed/02_nav_history.csv", index=False)

print("\nCleaned file saved successfully!")