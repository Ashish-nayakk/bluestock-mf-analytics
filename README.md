# 📊 Bluestock Mutual Fund Analytics Platform

> **End-to-End Mutual Fund Analytics, Financial Data Analysis & Power BI Business Intelligence Dashboard**

<p align="center">
  <strong>Built by Ashish Kumar Nayak</strong><br>
  B.Tech – Computer Science & Engineering<br>
  Centurion University of Technology and Management
</p>

<p align="center">

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?logo=pandas)
![SQL](https://img.shields.io/badge/SQL-Analytics-orange)
![SQLite](https://img.shields.io/badge/SQLite-Database-003B57?logo=sqlite)
![Power BI](https://img.shields.io/badge/Power%20BI-Dashboard-F2C811?logo=powerbi)
![GitHub](https://img.shields.io/badge/GitHub-Repository-181717?logo=github)

</p>

<p align="center">

🔗 **Repository:**  
https://github.com/Ashish-nayakk/bluestock-mf-analytics

</p>

---

# 📌 Project Overview

The **Bluestock Mutual Fund Analytics Platform** is an end-to-end data analytics and business intelligence project designed to transform raw and fragmented mutual-fund data into structured, query-ready information and interactive financial insights.

The project combines:

- 📥 Data ingestion
- 🧹 Data cleaning
- ✅ Data validation
- 🗄️ Relational database design
- 🔎 SQL analytics
- 🐍 Python-based analysis
- 📈 Financial performance analysis
- 📊 Power BI dashboard development
- 👥 Investor transaction analytics
- 💰 SIP inflow analysis
- 📉 NAV and benchmark comparison

The final solution provides an interactive **four-page Power BI dashboard** covering:

1. **Industry Overview**
2. **Fund Performance**
3. **Investor Analytics**
4. **SIP & Market Trends**

---

# 🎯 Project Objectives

The major objectives of this project are:

- Ingest historical mutual-fund and NAV data from public data sources.
- Validate NAV information against AMFI records.
- Clean and standardise raw financial datasets.
- Handle missing values, duplicates and inconsistent formats.
- Store structured data in a relational SQLite database.
- Perform SQL-based financial analysis.
- Analyse mutual-fund performance and risk indicators.
- Analyse investor transaction behaviour.
- Study SIP inflow patterns.
- Analyse category-level net inflows.
- Compare NAV and benchmark-index movements.
- Build an interactive Power BI dashboard for business intelligence.
- Present financial analytics through an easy-to-understand visual interface.

---

# 📊 Project Dashboard

The final Power BI dashboard contains **four analytical pages**.

---

## 1️⃣ Industry Overview

The **Industry Overview** page provides an executive-level summary of the mutual-fund dataset.

### KPI Cards

The dashboard displays:

| KPI | Visible Dashboard Value |
|---|---:|
| 💰 Total AUM | **39M** |
| 📈 Total SIP Inflows | **940K** |
| 👥 Total Folios | **416.42** |
| 📊 Total Schemes | **40** |

> KPI values shown above represent the dashboard state visible in the supplied screenshot. Interactive filters can change displayed values.

### Visualisations

#### Industry AUM Trend

Displays the yearly AUM trend across:

**2022 → 2023 → 2024 → 2025**

#### AUM by Fund House

The dashboard compares AUM across fund houses including:

- SBI Mutual Fund
- ICICI Prudential MF
- HDFC Mutual Fund
- Nippon India MF
- Kotak Mahindra MF
- Aditya Birla Sun Life MF
- UTI Mutual Fund
- Axis Mutual Fund
- Mirae Asset MF
- DSP Mutual Fund

### Interactive Filter

**Fund House**

Users can select individual fund houses or multiple fund houses for focused analysis.

---

# 2️⃣ Fund Performance

The **Fund Performance** page focuses on mutual-fund return and risk analysis.

### 📈 Return vs Risk Analysis

The scatter plot analyses:

- Benchmark 3-Year %
- Beta
- Fund-level observations
- Relative positioning of funds

This provides a visual way to explore the relationship between historical benchmark return and beta.

---

### 📋 Fund Performance Scorecard

The dashboard contains a detailed performance table with:

| Metric |
|---|
| Fund House |
| Category |
| Benchmark 3-Year % |
| Alpha |
| Beta |
| Expense Ratio % |

This allows users to compare multiple schemes using return, risk and cost-related indicators.

---

### 📉 NAV / Benchmark Analysis

The dashboard also provides a year-based trend comparison using:

- NAV
- Close Value / benchmark-related value
- Year

This allows historical NAV movement to be explored alongside benchmark information.

### Interactive Filter

**Fund House**

Users can filter performance analysis by fund house.

---

# 3️⃣ Investor Analytics

The **Investor Analytics** page focuses on transaction behaviour and investor segmentation.

### 🌍 Transaction Amount by State

The dashboard provides a state-wise comparison of transaction amounts.

Visible states include:

- West Bengal
- Gujarat
- Telangana
- Delhi
- Maharashtra
- Madhya Pradesh
- Rajasthan
- Uttar Pradesh
- and other states available through the visual.

---

### 🔄 Transaction Type Distribution

The dashboard categorises transactions into:

- **Lumpsum**
- **Redemption**
- **SIP**

The visible screenshot shows:

| Transaction Type | Visible Amount |
|---|---:|
| Lumpsum | 190M |
| Redemption | 123M |
| SIP | 19M |

> These values represent the visible dashboard filter state.

---

### 👤 Average SIP Amount by Age Group

The dashboard analyses average SIP/transaction amount across age groups.

Available age groups include:

- 18–25
- 26–35
- 36–45
- 46–55
- 56+

The dashboard supports interactive demographic filtering.

---

### 📅 Monthly Transaction Volume

A time-series visual tracks transaction activity over time.

This allows users to identify:

- Monthly transaction fluctuations
- High-volume periods
- Low-volume periods
- Overall transaction activity patterns

---

### Interactive Filters

The Investor Analytics page includes:

- **State**
- **City Tier**
- **Age Group**

City-tier categories visible in the dashboard include:

- B30
- T30

---

# 4️⃣ SIP & Market Trends

The **SIP & Market Trends** page analyses SIP inflows, category-level flows and benchmark-related market trends.

### 📅 Date Range Filter

The dashboard provides a date-range slicer covering the displayed analysis period.

The screenshot shows:

**2022 → 2025**

---

### 📈 SIP Inflows vs Benchmark

The dashboard compares:

- SIP Inflows
- Close Value / benchmark-related values
- Year
- Month

This allows users to visually compare SIP-flow behaviour with market-index movement.

---

### 📊 Category-Level Net Inflows

The dashboard provides a ranked category-level analysis.

Visible categories include:

- Liquid
- Sectoral/Thematic
- Flexi Cap
- Large & Mid Cap
- Short Duration
- Mid Cap
- Small Cap
- Hybrid
- Large Cap
- Value/Contra
- Gilt
- and other categories in the dataset.

The visible screenshot shows **Liquid** as the largest displayed category in the bar chart.

---

### 🌳 Category Inflow Treemap

A treemap provides a visual representation of category-level net inflows.

The size of each block represents its relative contribution within the displayed dataset/filter context.

---

# 🏗️ Project Architecture

```text
                  ┌─────────────────────────────┐
                  │ Public Mutual Fund Sources │
                  │            +                │
                  │            AMFI             │
                  └──────────────┬──────────────┘
                                 │
                                 ▼
                  ┌─────────────────────────────┐
                  │       Data Ingestion        │
                  │ Python + Requests + Pandas │
                  └──────────────┬──────────────┘
                                 │
                                 ▼
                  ┌─────────────────────────────┐
                  │    Data Cleaning & QA       │
                  │                             │
                  │ • Missing Values            │
                  │ • Duplicate Records         │
                  │ • Date Standardisation      │
                  │ • Numeric Standardisation   │
                  └──────────────┬──────────────┘
                                 │
                                 ▼
                  ┌─────────────────────────────┐
                  │       SQLite Database       │
                  │        + SQLAlchemy         │
                  └──────────────┬──────────────┘
                                 │
                    ┌────────────┴─────────────┐
                    │                          │
                    ▼                          ▼
          ┌──────────────────┐       ┌────────────────────┐
          │ Python / SQL     │       │     Power BI       │
          │ Analytics        │       │ Semantic Model     │
          └────────┬─────────┘       └──────────┬─────────┘
                   │                            │
                   └────────────┬───────────────┘
                                ▼
                    ┌────────────────────────┐
                    │ Business Intelligence  │
                    │ & Financial Insights    │
                    └────────────────────────┘
