# Mutual Fund Data Analysis

## Project Overview

This project is developed as part of the **Bluestock Fintech Data Analyst Capstone Project**.

The main aim of this project is to analyze mutual fund data and generate useful insights about **NAV, AUM, SIP inflows, fund performance, risk, and investor transactions**.

The project uses Python, SQL, SQLite, and Power BI for data processing, analysis, and visualization.

---

## Objectives

* Collect and clean mutual fund data.
* Store the cleaned data in a SQLite database.
* Perform Exploratory Data Analysis (EDA).
* Analyze NAV and fund performance.
* Calculate risk and performance metrics.
* Analyze SIP inflows and investor transactions.
* Create an interactive Power BI dashboard.
* Generate useful business insights from the data.

---

## Tools and Technologies

* **Python**
* **Pandas**
* **NumPy**
* **Matplotlib**
* **SQL**
* **SQLite**
* **Jupyter Notebook**
* **Power BI**
* **Git & GitHub**

---

## Project Structure

mutual_fund_project/
│
├── dashboard/                    # Power BI dashboard
├── data/
│   ├── raw/                      # Raw datasets
│   └── processed/                # Cleaned datasets
├── notebooks/                    # Analysis notebooks
├── reports/                      # Project reports
├── sql/                          # SQL files
│
├── bluestock_mf.db               # SQLite database
├── data_ingestion.py             # Data ingestion
├── load_data.py                  # Load data
├── load_database.py              # Load data into database
├── check_tables.py               # Check database tables
├── checkingCSV.py                # CSV validation
├── clean_investor_transactions.py
├── clean_nav_history.py
├── clean_scheme_performance.py
├── fund_master_analysis.py
├── live_nav_fetch.py
├── recommender.py
├── validate_amfi.py
├── verify_data.py
│
├── EDA_Analysis.ipynb             # Exploratory Data Analysis
├── Performance_Analytics.ipynb    # Performance Analysis
│
├── alpha_beta.csv                 # Beta analysis results
├── benchmark_comparison.png       # Benchmark comparison
├── fund_scorecard.csv             # Fund scorecard
├── maximum_drawdown.csv           # Maximum drawdown results
├── tracking_error.csv             # Tracking error results
│
├── data_dictionary.md              # Data dictionary
├── requirements.txt                # Python dependencies
└── README.md                       # Project documentation

---

## Dataset

The project contains mutual fund datasets related to:

* Fund details
* Historical NAV
* AUM
* Monthly SIP inflows
* Investor transactions

Some of the datasets contain:

* **40 Mutual Fund Schemes**
* **46,000+ NAV records**
* **32,000+ Transaction records**
* **90 AUM records**
* **48 Monthly SIP records**

---

## Project Workflow

```text
Data Collection
      ↓
Data Cleaning
      ↓
Data Transformation
      ↓
SQLite Database
      ↓
Exploratory Data Analysis
      ↓
Performance & Risk Analysis
      ↓
Power BI Dashboard
      ↓
Final Insights
```

---

## 📈 Analysis Performed

### 1. NAV Analysis

* Analyzed historical NAV trends.
* Compared NAV movements across mutual fund schemes.
* Studied trends from 2022 to 2026.

### 2. AUM Analysis

* Analyzed AUM by fund house.
* Studied AUM growth trends.
* Compared different AMCs.

### 3. SIP Analysis

* Analyzed monthly SIP inflows.
* Studied SIP growth patterns.
* Compared SIP inflows across categories.

### 4. Investor Analysis

* Analyzed transactions by state.
* Studied transaction types such as SIP, Lumpsum, and Redemption.
* Analyzed transactions by age group and city tier.

### 5. Fund Performance

The project includes analysis of:

* Returns
* Risk / Standard Deviation
* Sharpe Ratio
* Beta
* Value at Risk (VaR)

---

## Power BI Dashboard

The Power BI dashboard contains the following pages:

### Page 1 – Industry Overview

* Total AUM
* SIP Inflows
* Folios
* Number of Schemes
* Industry AUM Trend
* AUM by AMC

### Page 2 – Fund Performance

* Return vs Risk
* Fund Performance Scorecard
* NAV Performance
* Fund House, Category and Plan filters

### Page 3 – Investor Analytics

* Transaction Amount by State
* SIP / Lumpsum / Redemption
* Age Group vs Average SIP
* Monthly Transaction Volume

### Page 4 – SIP & Market Trends

* Monthly SIP Trends
* SIP Inflow Analysis
* Category-wise Trends
* Market Trends

---

## Key Insights

The project helps to understand:

* Mutual fund industry growth.
* SIP investment trends.
* AUM distribution among AMCs.
* Relationship between fund return and risk.
* Investor transaction behavior.
* Geographic distribution of investors.
* Different investment patterns.

---

## Main Deliverables

* ETL Pipeline
* Cleaned Dataset
* SQLite Database
* EDA Notebook
* Performance Metrics Notebook
* Power BI Dashboard
* Final Project Report
* Project Presentation

---

## Author

**Swathi B.U**

BCA Graduate

**Project:** Mutual Fund Data Analysis
**Organization:** Bluestock Fintech
**Domain:** Data Analytics / Fintech
