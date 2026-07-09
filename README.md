# Weather Data Engineering Pipeline

## Overview

This project demonstrates an end-to-end ETL (Extract, Transform, Load) data engineering pipeline built in Python.

The pipeline retrieves daily weather forecast data for multiple Washington cities using the Open-Meteo API, transforms and validates the data, and loads it into a SQLite database for SQL analysis.

The project emphasizes modular software design, maintainability, and production-inspired engineering practices while demonstrating core data engineering concepts.

---

## Features

- 🌤️ Collects weather forecasts from the Open-Meteo API
- 🌎 Supports multiple Washington cities
- ⚙️ Centralized project configuration
- 🔄 Modular ETL architecture
- ✅ Data quality validation
- 🗄️ Loads cleaned data into SQLite
- 📊 SQL analytics queries
- 📝 Structured logging to both the console and log files

---

## Technologies Used

- Python 3
- Pandas
- Requests
- SQLite
- SQL
- Logging
- Jupyter Notebook
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
├── logs/
│   └── weather_pipeline.log
│
├── notebooks/
│   └── exploration.ipynb
│
├── sql/
│   ├── analysis_queries.sql
│   ├── create_tables.sql
│   └── load_data.sql
│
├── src/
│   ├── __init__.py
│   ├── config.py
│   ├── logger.py
│   ├── extract.py
│   ├── transform.py
│   ├── data_quality.py
│   ├── load.py
│   └── query_database.py
│
├── main.py
├── README.md
├── requirements.txt
└── .gitignore
```

---

## ETL Pipeline

```text
Open-Meteo API
       │
       ▼
   extract.py
       │
       ▼
 weather_data.json
       │
       ▼
 transform.py
       │
       ▼
 weather_data.csv
       │
       ▼
data_quality.py
       │
       ▼
    load.py
       │
       ▼
 weather_data.db
       │
       ▼
 SQL Analytics
```

---

## Extract

The extraction stage:

- Reads project settings from `config.py`
- Connects to the Open-Meteo API
- Retrieves daily forecasts for multiple Washington cities
- Saves the raw API responses as JSON

Current cities include:

- Bellevue
- Seattle
- Redmond
- Kirkland
- Tacoma

---

## Transform

The transformation stage:

- Loads the raw JSON responses
- Converts nested weather data into Pandas DataFrames
- Combines multiple cities into a single dataset
- Converts dates into datetime objects
- Renames columns for readability
- Calculates temperatures in Fahrenheit
- Exports the cleaned data as CSV

---

## Data Quality

Before loading the data into the database, the pipeline validates:

- Dataset is not empty
- Required columns exist
- No missing values
- Maximum temperature is greater than or equal to minimum temperature

The pipeline immediately stops if validation fails.

---

## Load

The validated dataset is loaded into a SQLite database.

Database:

```text
data/database/weather_data.db
```

Table:

```text
weather_daily
```

---

## Logging

The pipeline uses Python's built-in `logging` module instead of `print()` statements.

Each run records:

- Pipeline start and completion
- Weather retrieval for each city
- Transformation progress
- Validation status
- Database loading
- Record counts

Logs are written to:

```text
logs/weather_pipeline.log
```

Example output:

```text
INFO Starting weather ETL pipeline.
INFO Fetching weather data for Bellevue
INFO Successfully retrieved weather data for Bellevue
INFO Loaded raw weather data for 5 cities.
INFO Transformed weather data into 35 rows.
INFO Starting data validation.
INFO Data validation passed.
INFO Loaded 35 weather records into data/database/weather_data.db
INFO Weather ETL pipeline completed successfully.
```

---

## Configuration

Project settings are centralized in `src/config.py`.

This includes:

- Supported cities
- API endpoint
- Time zone
- File paths
- Database location

This allows the pipeline to be extended without modifying multiple files.

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

Run the pipeline:

```bash
python main.py
```

---

## Example SQL Queries

Average forecasted temperature by city:

```sql
SELECT
    city,
    ROUND(AVG(max_temp_f), 1) AS avg_max_temp_f,
    ROUND(AVG(min_temp_f), 1) AS avg_min_temp_f
FROM weather_daily
GROUP BY city
ORDER BY avg_max_temp_f DESC;
```

Warmest forecasted day:

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
- Data transformation with Pandas
- Multi-city data ingestion
- Data quality validation
- SQLite database management
- SQL analytics
- Structured logging
- Modular Python application design
- Configuration management
- Git version control
- Software architecture

---

## Future Improvements

Planned enhancements include:

- Historical weather data collection
- Incremental database loading
- Duplicate prevention
- Unit testing with pytest
- Docker containerization
- PostgreSQL integration
- Workflow orchestration with Airflow or Prefect
- Interactive dashboard with Streamlit

---

## About This Project

This project was built as a hands-on learning exercise to develop practical data engineering skills. Rather than focusing solely on data analysis, the emphasis is on designing a modular, maintainable ETL pipeline that mirrors the structure and practices commonly found in production data engineering workflows.

---

## Author

**Joshua Cochran**

M.S. Data Science  
Indiana University