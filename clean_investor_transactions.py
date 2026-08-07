import pandas as pd

# Read the investor transactions file
transactions = pd.read_csv("data/raw/08_investor_transactions.csv")

# Show column names
print("Column Names:")
print(transactions.columns)

# Show first 5 rows
print("\nFirst 5 Rows:")
print(transactions.head())

# Convert transaction_date to datetime
transactions["transaction_date"] = pd.to_datetime(transactions["transaction_date"])

# Display data types
print("\nData Types:")
print(transactions.dtypes)

# Check unique transaction types
print("\nTransaction Types:")
print(transactions["transaction_type"].unique())

# Check invalid transaction amounts
invalid_amount = transactions[transactions["amount_inr"] <= 0]

print("\nNumber of invalid amounts:")
print(len(invalid_amount))

# Check KYC status values
print("\nKYC Status:")
print(transactions["kyc_status"].unique())

# Save the cleaned file
transactions.to_csv("data/processed/08_investor_transactions.csv", index=False)

print("\nCleaned investor_transactions file saved successfully!")