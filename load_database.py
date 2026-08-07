import sqlite3

# Create database
conn = sqlite3.connect("bluestock_mf.db")

# Read schema file
file = open("sql/schema.sql", "r")
schema = file.read()
file.close()

# Remove old tables if they exist and create new tables

conn.executescript("""
DROP TABLE IF EXISTS fact_nav;
DROP TABLE IF EXISTS fact_transactions;
DROP TABLE IF EXISTS fact_performance;
DROP TABLE IF EXISTS fact_aum;
DROP TABLE IF EXISTS dim_fund;
DROP TABLE IF EXISTS dim_date;

""" + schema)

conn.commit()

conn.close()

print("SQLite database created successfully!")