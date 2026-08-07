import pandas as pd
from sqlalchemy import create_engine

# Connect to SQLite database
engine = create_engine("sqlite:///bluestock_mf.db")

# Read CSV files

fund_data = pd.read_csv("data/raw/01_fund_master.csv")
nav_data = pd.read_csv("data/processed/02_nav_history.csv")
transaction_data = pd.read_csv("data/processed/08_investor_transactions.csv")
performance_data = pd.read_csv("data/processed/09_scheme_performance.csv")
aum_data = pd.read_csv("data/raw/03_aum_by_fund_house.csv")


# Rename column

transaction_data.rename(columns={"transaction_date": "date"}, inplace=True)


# Keep only required transaction columns

transaction_data = transaction_data[
[
    "investor_id",
    "amfi_code",
    "date",
    "transaction_type",
    "amount_inr",
    "state",
    "city",
    "kyc_status"
]
]


# Load dimension table

fund_data.to_sql(
    "dim_fund",
    engine,
    if_exists="append",
    index=False
)


# Load fact tables

nav_data.to_sql(
    "fact_nav",
    engine,
    if_exists="append",
    index=False
)

transaction_data.to_sql(
    "fact_transactions",
    engine,
    if_exists="append",
    index=False
)

performance_data.to_sql(
    "fact_performance",
    engine,
    if_exists="append",
    index=False
)

aum_data.to_sql(
    "fact_aum",
    engine,
    if_exists="append",
    index=False
)


print("Data loaded successfully!")