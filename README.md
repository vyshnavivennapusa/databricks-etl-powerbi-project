# databricks-etl-powerbi-project
End-to-End E-Commerce Sales Analytics using Databricks, PySpark, SQL, and Power BI.
# 🚀 End-to-End E-Commerce Sales Analytics using Databricks & Power BI

<p align="center">

![Databricks](https://img.shields.io/badge/Databricks-FF3621?style=for-the-badge&logo=databricks&logoColor=white)
![PySpark](https://img.shields.io/badge/PySpark-E25A1C?style=for-the-badge&logo=apachespark&logoColor=white)
![SQL](https://img.shields.io/badge/SQL-336791?style=for-the-badge&logo=postgresql&logoColor=white)
![Power BI](https://img.shields.io/badge/Power_BI-F2C811?style=for-the-badge&logo=powerbi&logoColor=black)
![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)

</p>

---

## 📌 Project Overview

This project demonstrates an **end-to-end data engineering and analytics pipeline** built using the **Medallion Architecture (Bronze → Silver → Gold)** in Databricks.

Raw e-commerce data is ingested, cleaned, transformed into analytics-ready tables, analyzed using SQL, and finally visualized through an interactive Power BI dashboard.

The project showcases modern data engineering and business intelligence practices using PySpark, SQL, Delta tables, and Power BI.
## 🏗️ Project Architecture

The project follows the **Medallion Architecture**, where data moves through three layers before being used for analytics and visualization.

```text
                    Olist E-Commerce Dataset (CSV Files)
                                   │
                                   ▼
                     Databricks Volume (Raw Data)
                                   │
                                   ▼
                     🥉 Bronze Layer (Raw Ingestion)
                                   │
                                   ▼
                 🥈 Silver Layer (Cleaning & Transformation)
                                   │
                                   ▼
                  🥇 Gold Layer (Business-Ready Data)
                                   │
                    ┌──────────────┴──────────────┐
                    ▼                             ▼
              SQL Analysis                  Python EDA
                    │
                    ▼
          Interactive Power BI Dashboard
```
## 🛠️ Tech Stack

| Category | Technologies |
|----------|--------------|
| Programming | Python, PySpark |
| Data Processing | Apache Spark |
| Data Platform | Databricks |
| Storage | Delta Tables |
| Query Language | SQL |
| Visualization | Power BI |
| Version Control | Git & GitHub |
| Dataset | Olist Brazilian E-Commerce Dataset |
## ✨ Features

- Built an end-to-end ETL pipeline using Databricks.
- Implemented the Medallion Architecture (Bronze, Silver, Gold).
- Performed data cleaning, transformation, and feature engineering using PySpark.
- Created analytics-ready Gold tables for reporting.
- Performed business analysis using SQL.
- Designed an interactive Power BI dashboard with KPIs and visualizations.
- Managed the project using Git and GitHub.
