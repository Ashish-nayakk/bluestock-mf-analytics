import pandas as pd

# Load data
nav = pd.read_csv("data/raw/02_nav_history.csv")

print("Original Shape:", nav.shape)

# Convert date column
nav["date"] = pd.to_datetime(nav["date"])

# Sort
nav = nav.sort_values(
    ["amfi_code", "date"]
)

# Remove duplicates
nav = nav.drop_duplicates()

# Forward fill missing NAV values
nav["nav"] = (
    nav.groupby("amfi_code")["nav"]
       .ffill()
)

# Keep only positive NAV
nav = nav[nav["nav"] > 0]

print("Cleaned Shape:", nav.shape)

# Check nulls
print("\nMissing NAV:")
print(nav["nav"].isnull().sum())

# Save
nav.to_csv(
    "data/processed/clean_nav_history.csv",
    index=False
)

print("\nSaved: clean_nav_history.csv")