# ETL Dataset Monitoring Factory Workers’ Daily Performance & Attrition

## 🏗️ Technical Architecture & Tool Stack
![Technical Architecture - Airflow Batch Processing](https://raw.githubusercontent.com/mhdalfarisy/mhdalfarisy.github.io/main/src/assets/images/Batch_Processing_Flow_airflow.png)

## 📌 Project Overview
This project demonstrates an End-to-End **Batch Processing Pipeline** designed to handle large-scale data workflows. The pipeline automates data ingestion from flat files, performs complex transformations, and stores the processed data in a relational database for advanced business intelligence and visualization.

---

## 🛠️ Tech Stack
* **Orchestration:** [Apache Airflow](https://airflow.apache.org/) (Managing DAGs and task dependencies).
* **Processing:** [Python](https://www.python.org/) (Pandas for data transformation and ETL logic).
* **Database:** [PostgreSQL](https://www.postgresql.org/) (Serving as the Data Sink/Warehouse).
* **Containerization:** [Docker](https://www.docker.com/) (Ensuring consistent environments for Airflow and DB).
* **Visualization:** [Power BI](https://powerbi.microsoft.com/) (Interactive dashboards and analytical reporting).

---

## ⚙️ Data Pipeline Workflow

### 1. Ingestion (Extract)
* Raw data is sourced from **CSV** files.
* The extraction process is triggered and monitored by **Apache Airflow** DAGs.

### 2. Processing (Transform)
* **Data Cleaning:** Handling missing values, duplicates, and data type formatting.
* **Business Logic:** Applying transformations using Python to prepare the data for analytical schemas.
* **Efficiency:** Scripted for high-performance batch processing within a containerized environment.

### 3. Storage (Load)
* Processed data is loaded into a **PostgreSQL** database.
* Optimized table structures (Star Schema/Snowflake) to ensure fast query performance for BI tools.

### 4. Monitoring & Visualization
* **Containerization:** The entire stack (Airflow, Postgres) runs on **Docker** for seamless deployment.
* **Reporting:** Power BI connects to PostgreSQL to deliver real-time insights and trend analysis.

---

## 📂 Project Structure
```text
.
├── dags/
│   └── etl_workflow.py       # Airflow DAG definitions
├── scripts/
│   └── transformation.py     # Python ETL logic
├── docker-compose.yaml       # Docker configuration for Airflow & Postgres
├── data/
│   └── raw_data.csv          # Source dataset
└── README.md
