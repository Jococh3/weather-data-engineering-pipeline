import sqlite3

import pandas as pd

from config import DATABASE_PATH, PROCESSED_DATA_PATH


def load_processed_data():
    """Load the processed weather CSV into a DataFrame."""
    return pd.read_csv(PROCESSED_DATA_PATH)


def connect_to_database():
    """Create a connection to the SQLite database."""
    return sqlite3.connect(DATABASE_PATH)


def load_data_to_database(weather_df, connection):
    """Load the weather DataFrame into a SQLite table."""

    weather_df.to_sql(
        "weather_daily",
        connection,
        if_exists="replace",
        index=False,
    )


def run():
    """Run the load step."""

    weather_df = load_processed_data()
    connection = connect_to_database()
    load_data_to_database(weather_df, connection)
    connection.close()

    print(f"Weather data loaded into {DATABASE_PATH}")


if __name__ == "__main__":
    run()
