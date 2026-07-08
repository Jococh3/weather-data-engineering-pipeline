# Weather Data Engineering Pipeline

## Overview

This project demonstrates an end-to-end ETL (Extract, Transform, Load) data engineering pipeline built in Python.

The pipeline retrieves daily weather forecast data for multiple Washington cities using the Open-Meteo API, transforms and validates the data, and loads it into a SQLite database for SQL analysis.

The project was designed to demonstrate practical data engineering concepts including API integration, modular ETL architecture, data quality validation, relational databases, SQL analytics, and maintainable Python project organization.

---

## Technologies Used

- Python 3
- Pandas
- Requests
- SQLite
- Jupyter Notebook
- SQL
- Git & GitHub

---

## Project Structure

```text
weather-data-pipeline/
│
├── data/
│   ├── raw/
│   │   └── weather_data.json
│   │
│   ├── processed/
│   │   └── weather_data.csv
│   │
│   └── database/
│       └── weather_data.db
│
├── notebooks/
│   └── exploration.ipynb
│
├── sql/
│   └── analysis_queries.sql
│
├── src/
│   ├── extract.py
│   ├── transform.py
│   ├── data_quality.py
│   ├── load.py
│   └── query_database.py
│
├── config.py
├── main.py
├── README.md
├── requirements.txt
└── .gitignore
```

---

## ETL Pipeline

### 1. Extract

The extraction stage:

- Reads project settings from `config.py`
- Connects to the Open-Meteo API
- Retrieves weather forecasts for multiple Washington cities
- Stores the raw API responses as JSON

Current cities include:

- Bellevue
- Seattle
- Redmond
- Kirkland
- Tacoma

Output:

```
data/raw/weather_data.json
```

---

### 2. Transform

The transformation stage:

- Loads the raw JSON data
- Converts nested API responses into Pandas DataFrames
- Combines multiple cities into a single dataset
- Converts dates into datetime objects
- Renames columns using database-friendly names
- Calculates temperatures in Fahrenheit
- Saves the cleaned dataset as a CSV

Output:

```
data/processed/weather_data.csv
```

---

### 3. Data Quality

Before loading data into the database, the pipeline validates:

- Dataset is not empty
- Required columns exist
- No missing values
- Maximum temperatures are greater than or equal to minimum temperatures

The pipeline immediately stops if validation fails.

---

### 4. Load

The validated dataset is loaded into a SQLite database.

Database:

```
data/database/weather_data.db
```

Table:

```
weather_daily
```

The table is recreated each time the pipeline runs to ensure the database reflects the latest processed data.

---

## Configuration

Project settings are centralized in `config.py`, including:

- Weather API endpoint
- Supported cities
- Time zone
- Input and output file locations
- Database location

Centralizing configuration makes the project easier to maintain and extend without modifying multiple files.

---

## Running the Pipeline

Clone the repository:

```bash
git clone https://github.com/<your-username>/weather-data-pipeline.git
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the complete ETL pipeline:

```bash
python main.py
```

---

## Example SQL Queries

### View all weather records

```sql
SELECT *
FROM weather_daily;
```

### Average forecasted temperatures by city

```sql
SELECT
    city,
    ROUND(AVG(max_temp_f), 1) AS avg_max_temp_f,
    ROUND(AVG(min_temp_f), 1) AS avg_min_temp_f
FROM weather_daily
GROUP BY city
ORDER BY avg_max_temp_f DESC;
```

### Warmest forecasted day

```sql
SELECT
    city,
    weather_date,
    max_temp_f
FROM weather_daily
ORDER BY max_temp_f DESC
LIMIT 1;
```

---

## Skills Demonstrated

- ETL pipeline development
- REST API integration
- JSON processing
- Data transformation using Pandas
- Multi-city data ingestion
- Data quality validation
- SQLite database management
- SQL querying and analytics
- Modular Python application design
- Configuration management
- Git version control
- Software project organization

---

## Future Improvements

Planned enhancements include:

- Structured logging
- Historical weather data collection
- Advanced SQL analytics
- Unit testing
- Docker containerization
- PostgreSQL integration
- Workflow orchestration (Apache Airflow or Prefect)
- Interactive dashboard using Streamlit or Power BI

---

## About This Project

This project was built as a hands-on learning exercise to develop practical data engineering skills. Rather than focusing solely on data analysis, the emphasis was on designing a modular, maintainable ETL pipeline that mirrors the structure of production data workflows.

Future iterations will continue expanding the pipeline with additional automation, analytics, and cloud-ready features.

---

## Author

**Joshua Cochran**

M.S. Data Science  
Indiana University