# import sqlite3

# conn = sqlite3.connect("bluestock_mf.db")

# cursor = conn.cursor()

# cursor.execute("""
#     SELECT name
#     FROM sqlite_master
#     WHERE type = 'table'
#     ORDER BY name
# """)

# tables = cursor.fetchall()

# print("Tables in bluestock_mf.db:")
# for table in tables:
#     print(table[0])

# conn.close()

import pandas as pd
import os

folder = "data/raw"

files = [
    "01_fund_master.csv",
    "02_nav_history.csv",
    "03_aum_by_fund_house.csv",
    "04_monthly_sip_inflows.csv",
    "05_category_inflows.csv",
    "06_industry_folio_count.csv",
    "07_scheme_performance.csv",
    "08_investor_transactions.csv",
    "09_portfolio_holdings.csv",
    "10_benchmark_indices.csv"
]

for file in files:
    path = os.path.join(folder, file)

    df = pd.read_csv(path)

    print("\n" + "=" * 60)
    print(file)
    print("Rows:", len(df))
    print("Columns:")
    print(list(df.columns))