# ERP Sales & Supply Chain Analytics

An end-to-end ERP-inspired Sales & Supply Chain Analytics project that combines Python, SQL, Power BI, and Terraform to demonstrate data engineering, business intelligence, and Infrastructure as Code (IaC).

---

## Project Overview

This project simulates a real-world ERP analytics workflow using e-commerce sales and supply chain data.

The workflow includes:

- Data cleaning and preprocessing using Python
- Business analysis using SQL
- Interactive dashboard development using Power BI
- Infrastructure provisioning using Terraform
- Business KPI reporting for sales and supply chain operations

The objective is to transform raw transactional data into actionable business insights that can support operational and strategic decision-making.

---

## Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Data Cleaning & Preprocessing |
| Pandas | Data Manipulation |
| SQL | Business Analytics |
| Power BI | Dashboard & Visualization |
| Terraform | Infrastructure as Code |
| Oracle Cloud Infrastructure (OCI) | Cloud Infrastructure |

---

## Project Structure

```
ERP-Sales-Supply-Chain-Analytics/
│
├── README.md
├── LICENSE
├── requirements.txt
│
├── data/
│   ├── raw/
│   └── processed/
│       ├── customers_clean.csv
│       ├── orders_clean.csv
│       ├── order_items_clean.csv
│       └── products_clean.csv
│
├── python/
│   ├── data_cleaning.ipynb
│   └── data_cleaning.py
│
├── sql/
│   ├── 01_top_product_categories_by_sales.sql
│   ├── 02_monthly_sales_trend.sql
│   ├── 03_customer_lifetime_value.sql
│   ├── 04_market_wise_profitability.sql
│   ├── 05_late_delivery_rate_by_shipping_mode.sql
│   ├── 06_top_products_by_revenue.sql
│   ├── 07_customer_segment_analysis.sql
│   ├── 08_shipping_delay_analysis.sql
│   ├── 09_top_customers_in_each_market.sql
│   ├── 10_category_contribution_to_revenue.sql
│   └── 11_sales_dashboard_kpis.sql
│
├── powerbi/
│   ├── ERP Dashboard.pbix
│   ├── dashboard-overview.png
│   └── sales-dashboard.png
│
├── terraform/
│   ├── main.tf
│   ├── provider.tf
│   ├── variables.tf
│   └── README.md
│
└── docs/
```

---

## Dataset

The project uses four cleaned datasets representing an ERP sales workflow.

### Customers

Contains customer information including:

- Customer ID
- Name
- Market
- Region

### Orders

Contains order details including:

- Order ID
- Order Date
- Shipping Date
- Shipping Mode
- Customer ID

### Order Items

Contains transactional information such as:

- Product
- Quantity
- Sales
- Discount
- Profit

### Products

Contains product metadata including:

- Product ID
- Category
- Sub-category
- Product Name

---

## Business Questions Answered

The SQL scripts answer important business questions including:

- Top-performing product categories
- Monthly sales trend
- Customer Lifetime Value (CLV)
- Market-wise profitability
- Late delivery analysis
- Shipping mode performance
- Top revenue-generating products
- Customer segmentation
- Revenue contribution by category
- Executive sales KPIs

---

## Python Workflow

The Python pipeline performs:

- Data cleaning
- Missing value handling
- Data validation
- Feature preparation
- Export of cleaned datasets

---

## Power BI Dashboard

The dashboard provides visual insights into:

- Total Sales
- Total Profit
- Total Orders
- Customer Count
- Monthly Sales Trend
- Product Performance
- Market-wise Revenue
- Shipping Performance
- Executive KPIs

---

## Terraform

The Terraform configuration demonstrates Infrastructure as Code by provisioning Oracle Cloud Infrastructure resources.

Current configuration includes:

- OCI Provider
- Variable Management
- Infrastructure Configuration

---

## Key Features

- End-to-end analytics workflow
- ERP-inspired business scenario
- Data preprocessing using Python
- SQL business intelligence queries
- Power BI interactive dashboard
- Terraform Infrastructure as Code
- Modular project structure

---

## Future Enhancements

- Predictive sales forecasting
- Customer churn prediction
- Demand forecasting
- Inventory optimization
- Machine Learning integration
- Deployment on Oracle Cloud Infrastructure

---

## Skills Demonstrated

- Data Analysis
- Business Intelligence
- SQL
- Python
- Power BI
- Terraform
- Oracle Cloud Infrastructure
- ERP Analytics
- Data Cleaning
- KPI Reporting

---

## Author

**Nitya Arya**

Computer Science Engineering Student


