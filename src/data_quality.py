"""Validate transformed weather data before it is loaded into SQLite."""

import pandas as pd

from src.config import PROCESSED_DATA_PATH
from src.logger import setup_logger

logger = setup_logger()

REQUIRED_COLUMNS = {
    "weather_date",
    "max_temp_c",
    "min_temp_c",
    "precipitation_mm",
    "max_temp_f",
    "min_temp_f",
    "city",
}


def load_processed_data():
    """Load the processed weather data from the CSV file."""

    return pd.read_csv(PROCESSED_DATA_PATH)


def validate_data(data_df):
    """Validate the processed weather data and raise on invalid input."""

    if data_df.empty:
        raise ValueError("Processed dataset is empty.")

    missing_columns = REQUIRED_COLUMNS.difference(data_df.columns)
    if missing_columns:
        missing = ", ".join(sorted(missing_columns))
        raise ValueError(f"Processed dataset is missing required columns: {missing}.")

    if data_df.isnull().values.any():
        raise ValueError("Processed dataset contains missing values.")

    if not (data_df["max_temp_c"] >= data_df["min_temp_c"]).all():
        raise ValueError("Maximum temperature is less than minimum temperature.")

    return True


def run():
    """Run the data quality checks."""

    logger.info("Starting data validation.")
    weather_df = load_processed_data()
    validate_data(weather_df)
    logger.info("Data validation passed.")


if __name__ == "__main__":
    run()
