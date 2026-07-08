"""
This is a test file to query the SQLite database and load the data into a pandas DataFrame.
"""

import sqlite3
import pandas as pd

DATABASE_PATH = "data/weather.db"

connection = sqlite3.connect(DATABASE_PATH)

query = """
SELECT *
FROM weather_daily;
"""

weather_df = pd.read_sql_query(query, connection)

connection.close()

print(weather_df)