import sqlite3
import pandas as pd

# Database row counts
conn = sqlite3.connect("bluestock_mf.db")
cursor = conn.cursor()

tables = ["fact_nav", "fact_transactions", "fact_performance"]

print("Database Row Counts")
for table in tables:
    cursor.execute(f"SELECT COUNT(*) FROM {table}")
    print(table, ":", cursor.fetchone()[0])

conn.close()

print("\nCSV Row Counts")

# CSV row counts
nav = pd.read_csv("data/processed/02_nav_history.csv")
transactions = pd.read_csv("data/processed/08_investor_transactions.csv")
performance = pd.read_csv("data/processed/09_scheme_performance.csv")

print("NAV CSV:", len(nav))
print("Transactions CSV:", len(transactions))
print("Performance CSV:", len(performance))