# Data Dictionary - Mutual Fund Project

## 1. dim_fund Table

| Column Name | Data Type | Description | Source |
<!-- |---|---|---|---| -->
| amfi_code | INTEGER | Unique code for each mutual fund scheme | 01_fund_master.csv |
| fund_house | TEXT | Name of the mutual fund company | 01_fund_master.csv |
| scheme_name | TEXT | Name of the scheme | 01_fund_master.csv |
| category | TEXT | Category of fund like Equity or Debt | 01_fund_master.csv |
| sub_category | TEXT | Type of fund under category | 01_fund_master.csv |
| plan | TEXT | Plan type like Direct or Regular | 01_fund_master.csv |
| launch_date | TEXT | Scheme starting date | 01_fund_master.csv |
| benchmark | TEXT | Benchmark index of fund | 01_fund_master.csv |
| expense_ratio_pct | REAL | Expense charged by the fund | 01_fund_master.csv |
| exit_load_pct | REAL | Exit load percentage | 01_fund_master.csv |
| fund_manager | TEXT | Name of fund manager | 01_fund_master.csv |
| risk_category | TEXT | Risk level of fund | 01_fund_master.csv |


## 2. dim_date Table

| Column Name | Data Type | Description | Source |
<!-- |---|---|---|---| -->
| date | TEXT | Date value | Generated |
| year | INTEGER | Year from date | Generated |
| month | INTEGER | Month from date | Generated |
| day | INTEGER | Day from date | Generated |


## 3. fact_nav Table

| Column Name | Data Type | Description | Source |
<!-- |---|---|---|---| -->
| nav_id | INTEGER | Unique NAV record number | 02_nav_history.csv |
| amfi_code | INTEGER | Fund scheme code | 02_nav_history.csv |
| date | TEXT | NAV date | 02_nav_history.csv |
| nav | REAL | Net Asset Value of fund | 02_nav_history.csv |


## 4. fact_transactions Table

| Column Name | Data Type | Description | Source |
<!-- |---|---|---|---| -->
| transaction_id | INTEGER | Transaction unique ID | 08_investor_transactions.csv |
| investor_id | TEXT | Investor ID | 08_investor_transactions.csv |
| amfi_code | INTEGER | Scheme code | 08_investor_transactions.csv |
| date | TEXT | Transaction date | 08_investor_transactions.csv |
| transaction_type | TEXT | SIP, Lumpsum or Redemption | 08_investor_transactions.csv |
| amount_inr | REAL | Transaction amount | 08_investor_transactions.csv |
| state | TEXT | Investor state | 08_investor_transactions.csv |
| city | TEXT | Investor city | 08_investor_transactions.csv |
| kyc_status | TEXT | KYC verification status | 08_investor_transactions.csv |


## 5. fact_performance Table

| Column Name | Data Type | Description | Source |
<!-- |---|---|---|---| -->
| amfi_code | INTEGER | Fund scheme code | 09_scheme_performance.csv |
| return_1yr_pct | REAL | 1 year return percentage | 09_scheme_performance.csv |
| return_3yr_pct | REAL | 3 year return percentage | 09_scheme_performance.csv |
| return_5yr_pct | REAL | 5 year return percentage | 09_scheme_performance.csv |
| alpha | REAL | Extra return compared to benchmark | 09_scheme_performance.csv |
| beta | REAL | Market movement comparison | 09_scheme_performance.csv |
| sharpe_ratio | REAL | Risk adjusted return | 09_scheme_performance.csv |
| expense_ratio_pct | REAL | Fund expense ratio | 09_scheme_performance.csv |


## 6. fact_aum Table

| Column Name | Data Type | Description | Source |
<!-- |---|---|---|---| -->
| aum_id | INTEGER | Unique AUM record ID | 03_aum_by_fund_house.csv |
| date | TEXT | AUM date | 03_aum_by_fund_house.csv |
| fund_house | TEXT | Name of fund house | 03_aum_by_fund_house.csv |
| aum_lakh_crore | REAL | AUM value in lakh crore | 03_aum_by_fund_house.csv |
| aum_crore | REAL | AUM value in crore | 03_aum_by_fund_house.csv |
| num_schemes | INTEGER | Total schemes count | 03_aum_by_fund_house.csv |