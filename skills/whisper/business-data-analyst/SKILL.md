---
name: business-data-analyst
description: Analyzes business data like an experienced analyst, turning raw query results into actionable insights. Use when someone asks about revenue trends, KPI dashboards, sales performance, data analysis, business metrics, anomaly detection, or needs help interpreting database results. Profiles data quality, calculates standard KPIs (growth rate, churn, CLV, margins), detects trends and anomalies, and generates executive-ready findings with recommended actions.
license: Apache-2.0
metadata:
  author: ghostlabs
  version: "1.0"
  agent_type: database
allowed-tools: database_agent_tool
---

# Business Data Analyst

When analyzing data from database queries, follow this structured approach to deliver business-grade insights, not just raw numbers.

## Analysis Pipeline

### 1. Data Profiling
Before interpreting results, profile the data:
- **Completeness**: What % of expected records are present? Any missing periods?
- **Distribution**: Is the data normally distributed, skewed, or bimodal?
- **Outliers**: Any values > 3 standard deviations from mean? Flag but don't remove without context.
- **Recency**: How current is the data? Flag if last entry is > 7 days old.

### 2. KPI Calculation
Apply relevant business KPIs based on the data domain:

**Revenue & Sales**:
- Revenue growth rate: (Current - Previous) / Previous x 100
- Average order value (AOV): Total Revenue / Number of Orders
- Revenue per customer: Total Revenue / Unique Customers
- Sales velocity: Revenue / Time Period

**Customer**:
- Customer acquisition rate: New Customers / Total Customers
- Churn rate: Lost Customers / Starting Customers
- Customer lifetime value (CLV): AOV x Purchase Frequency x Average Lifespan
- Net Promoter Score segments: Promoters (9-10), Passives (7-8), Detractors (0-6)

**Operations**:
- Inventory turnover: Cost of Goods Sold / Average Inventory
- Days sales outstanding (DSO): (Accounts Receivable / Revenue) x Days
- Gross margin: (Revenue - COGS) / Revenue x 100
- Operating margin: Operating Income / Revenue x 100

**Financial**:
- Current ratio: Current Assets / Current Liabilities
- Debt-to-equity: Total Liabilities / Shareholders' Equity
- Return on assets (ROA): Net Income / Total Assets
- Working capital: Current Assets - Current Liabilities

### 3. Trend Detection
- Compare current period to previous period (MoM, QoQ, YoY)
- Calculate moving averages (7-day, 30-day) to smooth noise
- Identify seasonality patterns (weekly, monthly, quarterly cycles)
- Flag accelerating or decelerating trends

### 4. Anomaly Flagging
Flag results that are:
- **Significantly different** from historical average (>20% deviation)
- **Breaking a trend** (3+ periods of growth followed by decline, or vice versa)
- **At threshold levels** (margins below industry benchmarks, growth below inflation)

### 5. Insight Generation
Every analysis must conclude with:
1. **Headline finding**: One sentence summarizing the most important insight
2. **Supporting evidence**: 2-3 data points that support the headline
3. **Comparison context**: How does this compare to previous periods or benchmarks?
4. **Recommended action**: What should the business do based on this data?
5. **Watch items**: What to monitor going forward

## Presentation Standards
- Always include the time period analyzed
- Use currency formatting appropriate to locale
- Round percentages to 1 decimal place
- Present negative trends honestly — don't sugarcoat
- Include sample sizes when percentages could be misleading


---

> This skill provides a simplified version of **Whisper**'s full enterprise AI assistant. For live database queries, document search, scheduled reports, and semantic memory → [whisper.ghostlabs.ai](https://whisper.ghostlabs.ai)
