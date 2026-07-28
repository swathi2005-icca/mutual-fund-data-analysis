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



import requests
import pandas as pd

schemes = {
    "SBI_Bluechip": 119551,
    "ICICI_Bluechip": 120503,
    "Nippon_Large_Cap": 118632,
    "Axis_Bluechip": 119092,
    "Kotak_Bluechip": 120841
}
for scheme_name, amfi_code in schemes.items():

    print(f"\nFetching NAV for {scheme_name}...")

    url = f"https://api.mfapi.in/mf/{amfi_code}"

    response = requests.get(url)

    data = response.json()

    nav_df = pd.DataFrame(data["data"])

    file_name = f"data/raw/{scheme_name}.csv"

    nav_df.to_csv(file_name, index=False)

    print(f"{scheme_name} data saved successfully.")
    print(nav_df.head())