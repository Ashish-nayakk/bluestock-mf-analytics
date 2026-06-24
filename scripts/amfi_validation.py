import pandas as pd

fund = pd.read_csv(
    "data/raw/01_fund_master.csv"
)

nav = pd.read_csv(
    "data/raw/02_nav_history.csv"
)

missing_codes = (
    set(fund["amfi_code"])
    - set(nav["amfi_code"])
)

print("Missing Codes:")
print(missing_codes)

print(
    f"Total Missing: {len(missing_codes)}"
)