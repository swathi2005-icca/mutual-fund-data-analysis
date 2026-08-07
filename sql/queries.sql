-- Query 1: Top 5 Funds by AUM

SELECT
    fund_house,
    aum_crore
FROM fact_aum
ORDER BY aum_crore DESC
LIMIT 5;

-- Query 2: Average NAV per Month

SELECT
    substr(date, 1, 7) AS month,
    ROUND(AVG(nav), 2) AS average_nav
FROM fact_nav
GROUP BY substr(date, 1, 7)
ORDER BY month;

-- Query 3: SIP Year-over-Year (YoY) Growth

SELECT
    substr(date, 1, 4) AS year,
    COUNT(*) AS total_sip_transactions,
    ROUND(SUM(amount_inr), 2) AS total_sip_amount
FROM fact_transactions
WHERE transaction_type = 'SIP'
GROUP BY substr(date, 1, 4)
ORDER BY year;

-- Query 4: Transactions by State

SELECT
    state,
    COUNT(*) AS total_transactions,
    ROUND(SUM(amount_inr), 2) AS total_transaction_amount
FROM fact_transactions
GROUP BY state
ORDER BY total_transaction_amount DESC;

-- Query 5: Funds with Expense Ratio Less Than 1%

-- PRAGMA table_info(fact_performance);

SELECT
    scheme_name,
    fund_house,
    expense_ratio_pct
FROM fact_performance
WHERE expense_ratio_pct < 1
ORDER BY expense_ratio_pct ASC;

-- Query 6: Top 10 Funds by Latest NAV



-- SELECT COUNT(*) FROM dim_fund;

-- Query 6: Top 10 Funds by Latest NAV

SELECT
    f.scheme_name,
    f.fund_house,
    n.nav,
    n.date
FROM fact_nav n
JOIN dim_fund f
    ON n.amfi_code = f.amfi_code
ORDER BY n.nav DESC
LIMIT 10;

-- Query 7: Total Investment by Transaction Type

SELECT
    transaction_type,
    COUNT(*) AS total_transactions,
    ROUND(SUM(amount_inr), 2) AS total_amount
FROM fact_transactions
GROUP BY transaction_type
ORDER BY total_amount DESC;

-- Query 8: KYC Status Distribution

SELECT
    kyc_status,
    COUNT(*) AS total_records
FROM fact_transactions
GROUP BY kyc_status
ORDER BY total_records DESC;

-- Query 9: Top 5 Cities by Investment Amount

SELECT
    city,
    ROUND(SUM(amount_inr), 2) AS total_investment
FROM fact_transactions
GROUP BY city
ORDER BY total_investment DESC
LIMIT 5;

-- Query 10: Number of Schemes by Fund House

SELECT
    fund_house,
    COUNT(amfi_code) AS total_schemes
FROM dim_fund
GROUP BY fund_house
ORDER BY total_schemes DESC;