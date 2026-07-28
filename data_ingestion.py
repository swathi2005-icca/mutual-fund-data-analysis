import pandas as pd
import os

path = "data/raw"

files = os.listdir(path)

for file in files:
    if file.endswith(".csv"):

        print("\nFile:", file)

        df = pd.read_csv(path + "/" + file)

        print("Shape:", df.shape)

        print("\nData Types")
        print(df.dtypes)

        print("\nFirst 5 Rows")
        print(df.head())

        print("\nMissing Values")
        print(df.isnull().sum())

        print("\nDuplicate Rows")
        print(df.duplicated().sum())

        print("-" * 50)