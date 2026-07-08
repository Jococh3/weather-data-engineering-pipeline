import sqlite3  # Built-in Python library for working with SQLite databases.

import pandas as pd

DATABASE_PATH = "data/weather.db"  # Path to the SQLite database file.
CSV_PATH = "data/processed/bellevue_weather_daily.csv"  # Path to the CSV file containing processed weather data.


def load_processed_data():
    """Load the processed weather data from the CSV file."""

    return pd.read_csv(CSV_PATH)


def connect_to_database():
    """Establish a connection to the SQLite database."""

    return sqlite3.connect(DATABASE_PATH)


def load_data_to_database(data_df, connection):
    """Load the DataFrame into the SQLite database."""

    data_df.to_sql(
        "weather_daily",  # Name of the Database
        connection,  # Database connection
        if_exists="replace",  # Replace the table if it already exists
        index=False,  # Do not write DataFrame index as a column
    )


if __name__ == "__main__":
    data_df = load_processed_data()  # Load the processed data from CSV
    conn = connect_to_database()  # Connect to the SQLite database
    load_data_to_database(data_df, conn)  # Load the data into the database
    conn.close()  # Close the database connection

    print(f"Weather data loaded into {DATABASE_PATH}")
