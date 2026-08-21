# import requests
# import pandas as pd

# url = "https://api.mfapi.in/mf/125497"

# response = requests.get(url)

# if response.status_code == 200:
#     data = response.json()

#     df = pd.DataFrame(data["data"])
#     df.to_csv("data/raw/hdfc_top100_direct_nav.csv", index=False)

#     print("Data fetched successfully!")
#     print(df.head())
# else:
#     print("Failed to fetch data.")


"""
Fetch NAV data for selected mutual fund schemes.
"""

import os
import requests
import pandas as pd


schemes = {
    "SBI_Bluechip": 119551,
    "ICICI_Bluechip": 120503,
    "Nippon_Large_Cap": 118632,
    "Axis_Bluechip": 119092,
    "Kotak_Bluechip": 120841
}


def fetch_nav_data():
    """Fetch NAV history and save it as CSV files."""

    os.makedirs("data/raw", exist_ok=True)

    for scheme_name, amfi_code in schemes.items():
        print(f"Fetching NAV for {scheme_name}...")

        url = f"https://api.mfapi.in/mf/{amfi_code}"

        try:
            response = requests.get(url, timeout=30)
            response.raise_for_status()

            data = response.json()
            nav_df = pd.DataFrame(data["data"])

            file_name = f"data/raw/{scheme_name}.csv"
            nav_df.to_csv(file_name, index=False)

            print(f"{scheme_name} data saved successfully.")

        except requests.RequestException as error:
            print(f"Error fetching {scheme_name}: {error}")

        except KeyError:
            print(f"Invalid data received for {scheme_name}")


if __name__ == "__main__":
    fetch_nav_data()