import json
from pathlib import Path

import requests

from src.config import API_URL, CITIES, RAW_DATA_PATH, TIMEZONE

from src.logger import setup_logger

logger = setup_logger()


def fetch_weather_data(city):
    """Fetch daily weather data for one city from the Open-Meteo API."""

    params = {
        "latitude": city["latitude"],
        "longitude": city["longitude"],
        "daily": "temperature_2m_max,temperature_2m_min,precipitation_sum",
        "timezone": TIMEZONE,
    }

    response = requests.get(API_URL, params=params)
    response.raise_for_status()

    weather_data = response.json()

    # Add city name so we can identify the source later.
    weather_data["city"] = city["city"]

    return weather_data


def save_raw_data(weather_data):
    """Save all raw city weather responses as one JSON file."""

    raw_path = Path(RAW_DATA_PATH)
    raw_path.parent.mkdir(parents=True, exist_ok=True)

    with open(raw_path, "w") as file:
        json.dump(weather_data, file, indent=4)


def run():
    """Run the extract step for all configured cities."""

    all_weather_data = []

    # Loop through each city in config.py and fetch its weather data.
    for city in CITIES:
        logger.info(f"Fetching weather data for {city['city']}")

        city_weather_data = fetch_weather_data(city)

        logger.info(f"Successfully retrieved weather data for {city['city']}")

        all_weather_data.append(city_weather_data)

    save_raw_data(all_weather_data)

    logger.info("Raw weather data fetched and saved successfully.")


if __name__ == "__main__":
    run()
