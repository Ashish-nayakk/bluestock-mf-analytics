import pandas as pd

# Load data
tx = pd.read_csv("data/raw/08_investor_transactions.csv")

print("Original Shape:", tx.shape)

# Convert date
tx["transaction_date"] = pd.to_datetime(
    tx["transaction_date"]
)

# Standardize transaction types
tx["transaction_type"] = (
    tx["transaction_type"]
      .astype(str)
      .str.strip()
      .str.title()
)

# Keep valid transaction types
valid_types = [
    "Sip",
    "Lumpsum",
    "Redemption"
]

tx = tx[
    tx["transaction_type"].isin(valid_types)
]

# Amount must be positive
tx = tx[
    tx["amount_inr"] > 0
]

# Validate KYC status
valid_kyc = [
    "Verified",
    "Pending"
]

tx = tx[
    tx["kyc_status"].isin(valid_kyc)
]

print("Cleaned Shape:", tx.shape)

print("\nTransaction Types:")
print(tx["transaction_type"].value_counts())

print("\nKYC Status:")
print(tx["kyc_status"].value_counts())

# Save
tx.to_csv(
    "data/processed/clean_investor_transactions.csv",
    index=False
)

print("\nSaved: clean_investor_transactions.csv")