import pandas as pd

# Read fund master file
df = pd.read_csv("data/raw/01_fund_master.csv")

print("Fund Houses")
print(df["fund_house"].unique())

print("\nCategories")
print(df["category"].unique())

print("\nSub Categories")
print(df["sub_category"].unique())

# Check whether risk_grade column is available
if "risk_grade" in df.columns:
    print("\nRisk Grades")
    print(df["risk_grade"].unique())
else:
    print("\nRisk grade column is not available in this file.")