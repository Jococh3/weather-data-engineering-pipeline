# Weather Data Engineering Pipeline

A Python ETL project that retrieves daily forecast data for five Washington cities from the Open-Meteo API, transforms it, checks data quality, and stores the results in SQLite for SQL analysis.

## What it does

1. **Extract** — Requests daily maximum and minimum temperature and precipitation for Bellevue, Seattle, Redmond, Kirkland, and Tacoma. Raw responses are saved as JSON.
2. **Transform** — Combines the city responses into one table, parses dates, retains temperatures in Celsius, calculates Fahrenheit values, and writes a processed CSV.
3. **Validate** — Checks that the processed table is nonempty, contains required columns, has no missing values, and has maximum temperatures greater than or equal to minimum temperatures.
4. **Load** — Replaces the `weather_daily` table in SQLite with the current forecast rows.

```mermaid
flowchart LR
    A["Open-Meteo API"] --> B["Extract JSON"]
    B --> C["Transform to CSV"]
    C --> D["Quality checks"]
    D --> E["SQLite: weather_daily"]
    E --> F["SQL analysis"]
```

## Technology

Python, pandas, requests, SQLite, SQL, and Python logging.

## Repository layout

- `main.py` runs the four pipeline stages in order.
- `src/config.py` contains city coordinates, API settings, and output paths.
- `src/extract.py`, `src/transform.py`, `src/data_quality.py`, and `src/load.py` implement the pipeline.
- `src/query_database.py` provides a database query helper.
- `sql/analysis_queries.sql` contains sample analysis queries.
- `notebooks/exploration.ipynb` contains exploratory analysis.
- `data/database/weather_data.db` is a checked-in SQLite snapshot. A pipeline run refreshes its `weather_daily` table.
- `data/raw/`, `data/processed/`, and `logs/` are generated at runtime.

The `sql/create_tables.sql` and `sql/load_data.sql` files are currently empty and are not used by the pipeline; pandas creates or replaces the table during the load stage.

## Run locally

Requirements: Python and an internet connection. Open-Meteo access does not require an API key.

```bash
git clone https://github.com/Jococh3/weather-data-engineering-pipeline.git
cd weather-data-engineering-pipeline
python -m venv .venv
```

Activate the environment, then install dependencies and run the pipeline:

```bash
# macOS / Linux
source .venv/bin/activate
pip install -r requirements.txt
python main.py
```

On Windows PowerShell, activate with `.venv\\Scripts\\Activate.ps1`, then run the same install and pipeline commands.

The pipeline writes raw responses to `data/raw/weather_data.json`, transformed rows to `data/processed/weather_data.csv`, and the SQLite database to `data/database/weather_data.db`. It writes run details to `logs/weather_pipeline.log`.

## Example SQL

Average forecasted maximum temperature by city:

```sql
SELECT city, ROUND(AVG(max_temp_f), 1) AS avg_max_temp_f
FROM weather_daily
GROUP BY city
ORDER BY avg_max_temp_f DESC;
```

Warmest forecasted city and day:

```sql
SELECT city, weather_date, max_temp_f
FROM weather_daily
ORDER BY max_temp_f DESC
LIMIT 1;
```

## Scope and limitations

- The source is forecast data, not a historical observation archive.
- Each run replaces the existing `weather_daily` table; it does not preserve past forecast snapshots.
- The repository does not currently include an automated test suite.
- Forecast values and row counts depend on the API response at run time.
