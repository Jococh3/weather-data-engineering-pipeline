import json
from pathlib import Path

import pandas as pd

from src.config import PROCESSED_DATA_PATH, RAW_DATA_PATH

from src.logger import setup_logger

logger = setup_logger()


def load_raw_data():
    """Load the raw multi-city weather data from the JSON file."""

    with open(RAW_DATA_PATH, "r") as file:
        raw_data = json.load(file)

    return raw_data


def transform_city_weather(city_data):
    """Transform one city's raw weather data into a cleaned DataFrame."""

    daily_data = city_data["daily"]
    weather_df = pd.DataFrame(daily_data)

    weather_df["time"] = pd.to_datetime(weather_df["time"])

    weather_df = weather_df.rename(
        columns={
            "time": "weather_date",
            "temperature_2m_max": "max_temp_c",
            "temperature_2m_min": "min_temp_c",
            "precipitation_sum": "precipitation_mm",
        }
    )

    weather_df["max_temp_f"] = weather_df["max_temp_c"] * 9 / 5 + 32
    weather_df["min_temp_f"] = weather_df["min_temp_c"] * 9 / 5 + 32
    weather_df["city"] = city_data["city"]

    return weather_df


def transform_weather_data(raw_data):
    """Transform all city weather records into one combined DataFrame."""

    city_dataframes = []

    for city_data in raw_data:
        city_weather_df = transform_city_weather(city_data)
        city_dataframes.append(city_weather_df)

    weather_df = pd.concat(city_dataframes, ignore_index=True)

    return weather_df


def save_processed_data(weather_df):
    """Save the transformed weather data to a CSV file."""

    processed_path = Path(PROCESSED_DATA_PATH)
    processed_path.parent.mkdir(parents=True, exist_ok=True)
    weather_df.to_csv(processed_path, index=False)


def run():
    """Run the transform step."""

    logger.info("Starting transform step.")

    raw_data = load_raw_data()
    logger.info(f"Loaded raw weather data for {len(raw_data)} cities.")

    weather_df = transform_weather_data(raw_data)
    logger.info(f"Transformed weather data into {len(weather_df)} rows.")

    save_processed_data(weather_df)
    logger.info(f"Processed weather data saved to {PROCESSED_DATA_PATH}")


if __name__ == "__main__":
    run()
