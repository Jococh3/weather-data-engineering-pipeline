# Weather Data Engineering Pipeline

## Overview

This project demonstrates an end-to-end ETL (Extract, Transform, Load) data engineering pipeline built in Python.

The pipeline retrieves daily weather forecast data for Bellevue, Washington from the Open-Meteo API, transforms and validates the data, and loads it into a SQLite database for analysis.

The goal of this project was to gain hands-on experience with common data engineering concepts including API integration, data transformation, data quality validation, relational databases, and project organization.

---

## Technologies Used

- Python 3
- Pandas
- Requests
- SQLite
- Jupyter Notebook
- Git / GitHub

---

## Project Structure

```text
sports-data-pipeline/
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── weather.db
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
├── main.py
├── README.md
├── requirements.txt
└── .gitignore
```

---

## ETL Pipeline

### 1. Extract

- Connects to the Open-Meteo public API
- Retrieves daily weather forecast data for Bellevue, WA
- Saves the raw API response as JSON

Output:

```
data/raw/bellevue_weather_raw.json
```

---

### 2. Transform

- Loads the raw JSON data
- Converts the nested JSON into a Pandas DataFrame
- Converts dates into datetime objects
- Renames columns using database-friendly names
- Calculates Fahrenheit temperatures
- Adds the city name
- Saves the cleaned dataset as a CSV

Output:

```
data/processed/bellevue_weather_daily.csv
```

---

### 3. Data Quality

The pipeline validates the processed dataset by checking for:

- Empty datasets
- Missing values
- Invalid temperature relationships (maximum temperature must be greater than or equal to minimum temperature)

The pipeline stops immediately if validation fails.

---

### 4. Load

The validated dataset is loaded into a SQLite database using Pandas.

Database:

```
data/weather.db
```

Table:

```
weather_daily
```

---

## Running the Pipeline

Clone the repository:

```bash
git clone <repository-url>
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the entire pipeline:

```bash
python main.py
```

---

## Example SQL Query

```sql
SELECT *
FROM weather_daily;
```

---

## Skills Demonstrated

- ETL pipeline development
- REST API integration
- JSON processing
- Data transformation using Pandas
- Data quality validation
- SQLite database loading
- SQL querying
- Python project organization
- Modular programming
- Git version control

---

## Future Improvements

Planned enhancements include:

- Support for multiple cities
- Historical weather data collection
- Logging
- Automated scheduling
- Unit testing
- Docker containerization
- PostgreSQL support
- Data visualization dashboard

---

## Author

Joshua Cochran

Indiana University

M.S. Data Science