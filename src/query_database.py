import sqlite3

import pandas as pd

from src.config import DATABASE_PATH

connection = sqlite3.connect(DATABASE_PATH)

query = """
SELECT
    city,
    ROUND(AVG(max_temp_f), 1) AS avg_max_temp_f,
    ROUND(AVG(min_temp_f), 1) AS avg_min_temp_f
FROM weather_daily
GROUP BY city
ORDER BY avg_max_temp_f DESC;
"""

weather_df = pd.read_sql_query(query, connection)

connection.close()

print(weather_df)
