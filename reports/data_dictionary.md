# Data Dictionary

## 01_fund_master.csv

| Column | Type | Description |
|----------|----------|----------|
| amfi_code | INTEGER | Unique AMFI scheme code |
| fund_house | TEXT | Mutual fund company |
| scheme_name | TEXT | Scheme name |
| category | TEXT | Fund category |
| sub_category | TEXT | Fund sub-category |
| expense_ratio_pct | REAL | Expense ratio percentage |
| risk_category | TEXT | Risk level |

---

## 02_nav_history.csv

| Column | Type | Description |
|----------|----------|----------|
| amfi_code | INTEGER | Fund identifier |
| date | DATE | NAV date |
| nav | REAL | Net Asset Value |

---

## 03_aum_by_fund_house.csv

| Column | Type | Description |
|----------|----------|----------|
| fund_house | TEXT | Fund house |
| aum_lakh_crore | REAL | Assets under management |
| num_schemes | INTEGER | Number of schemes |

---

## 04_monthly_sip_inflows.csv

| Column | Type | Description |
|----------|----------|----------|
| month | TEXT | Month |
| sip_inflow_crore | INTEGER | SIP inflows |
| active_sip_accounts_crore | REAL | Active SIP accounts |

---

## 07_scheme_performance.csv

| Column | Type | Description |
|----------|----------|----------|
| return_1yr_pct | REAL | 1-year return |
| return_3yr_pct | REAL | 3-year CAGR |
| sharpe_ratio | REAL | Risk-adjusted return |
| alpha | REAL | Excess return |
| beta | REAL | Market sensitivity |

---

## 08_investor_transactions.csv

| Column | Type | Description |
|----------|----------|----------|
| investor_id | TEXT | Investor ID |
| transaction_type | TEXT | SIP/Lumpsum/Redemption |
| amount_inr | INTEGER | Transaction amount |
| state | TEXT | Investor state |
| city | TEXT | Investor city |
| kyc_status | TEXT | KYC verification status |