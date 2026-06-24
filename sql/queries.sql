-- 1. Top 5 funds by AUM

SELECT scheme_name,
       aum_crore
FROM fact_performance
ORDER BY aum_crore DESC
LIMIT 5;


-- 2. Average NAV per month

SELECT
strftime('%Y-%m', date) AS month,
AVG(nav) AS avg_nav
FROM fact_nav
GROUP BY month
ORDER BY month;


-- 3. Transactions by State

SELECT state,
COUNT(*) AS total_transactions
FROM fact_transactions
GROUP BY state
ORDER BY total_transactions DESC;


-- 4. SIP vs Lumpsum vs Redemption

SELECT transaction_type,
COUNT(*) AS total_count
FROM fact_transactions
GROUP BY transaction_type;


-- 5. Funds with Expense Ratio < 1%

SELECT scheme_name,
expense_ratio_pct
FROM fact_performance
WHERE expense_ratio_pct < 1
ORDER BY expense_ratio_pct;


-- 6. Top 10 Funds by Sharpe Ratio

SELECT scheme_name,
sharpe_ratio
FROM fact_performance
ORDER BY sharpe_ratio DESC
LIMIT 10;


-- 7. Average Transaction Amount by State

SELECT state,
ROUND(AVG(amount_inr),2) AS avg_amount
FROM fact_transactions
GROUP BY state
ORDER BY avg_amount DESC;


-- 8. Fund House AUM Ranking

SELECT fund_house,
MAX(aum_lakh_crore) AS latest_aum
FROM fact_aum
GROUP BY fund_house
ORDER BY latest_aum DESC;


-- 9. Category-wise Inflows

SELECT category,
SUM(net_inflow_crore) AS total_inflow
FROM fact_category_inflows
GROUP BY category
ORDER BY total_inflow DESC;


-- 10. Morningstar Rating Distribution

SELECT morningstar_rating,
COUNT(*) AS funds
FROM fact_performance
GROUP BY morningstar_rating
ORDER BY morningstar_rating;