import pandas as pd

# Load data
perf = pd.read_csv(
    "data/raw/07_scheme_performance.csv"
)

print("Original Shape:", perf.shape)

# Convert return columns
cols = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct",
    "expense_ratio_pct",
    "sharpe_ratio"
]

for col in cols:
    perf[col] = pd.to_numeric(
        perf[col],
        errors="coerce"
    )

# Expense ratio validation
perf["expense_valid"] = (
    perf["expense_ratio_pct"]
    .between(0.1, 2.5)
)

# Flag anomalies
perf["negative_sharpe"] = (
    perf["sharpe_ratio"] < 0
)

print("\nExpense Ratio Check:")
print(
    perf["expense_valid"]
    .value_counts()
)

print("\nNegative Sharpe Funds:")
print(
    perf["negative_sharpe"]
    .sum()
)

# Save
perf.to_csv(
    "data/processed/clean_scheme_performance.csv",
    index=False
)

print("\nSaved: clean_scheme_performance.csv")