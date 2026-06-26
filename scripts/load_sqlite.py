import pandas as pd
from sqlalchemy import create_engine

# Create SQLite database
engine = create_engine(
    "sqlite:///bluestock_mf.db"
)

# Files to load
files = {
    "dim_fund": "data/raw/01_fund_master.csv",
    "fact_nav": "data/processed/clean_nav_history.csv",
    "fact_aum": "data/raw/03_aum_by_fund_house.csv",
    "fact_sip": "data/raw/04_monthly_sip_inflows.csv",
    "fact_category_inflows": "data/raw/05_category_inflows.csv",
    "fact_folio_count": "data/raw/06_industry_folio_count.csv",
    "fact_performance": "data/processed/clean_scheme_performance.csv",
    "fact_transactions": "data/processed/clean_investor_transactions.csv",
    "fact_holdings": "data/raw/09_portfolio_holdings.csv",
    "fact_benchmark": "data/processed/clean_benchmark_indices.csv"
}

for table, path in files.items():

    df = pd.read_csv(path)

    df.to_sql(
        table,
        engine,
        if_exists="replace",
        index=False
    )

    print(
        f"{table}: {len(df)} rows loaded"
    )

print("\nDatabase created successfully!")