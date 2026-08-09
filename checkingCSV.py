# import pandas as pd

# nav = pd.read_csv("data/processed/02_nav_history.csv")

# print(nav.head())
# print(nav.columns)
# print(nav["date"].min())
# print(nav["date"].max())
# print(nav["amfi_code"].nunique())

# import os

# print(os.listdir("data/processed"))

import os

print("Raw Folder:")
print(os.listdir("data/raw"))

print("\nProcessed Folder:")
print(os.listdir("data/processed"))