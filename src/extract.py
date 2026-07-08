import json
from pathlib import Path

import requests


def fetch_weather_data():
    """Fetch daily weather data for Bellevue from the Open-Meteo API."""

    url = "https://api.open-meteo.com/v1/forecast"

    params = {
        "latitude": 47.6101,
        "longitude": -122.2015,
        "daily": "temperature_2m_max,temperature_2m_min,precipitation_sum",
        "timezone": "America/Los_Angeles",
    }

    response = requests.get(url, params=params)
    response.raise_for_status()  # Raise an error for bad responses (4xx or 5xx)

    return response.json()  # Return the JSON data as a Python dictionary


def save_raw_data(data):
    """Save the raw API response as a JSON file."""

    raw_path = Path("data/raw/bellevue_weather_raw.json")
    raw_path.parent.mkdir(
        parents=True, exist_ok=True
    )  # Create the directory if it doesn't exist

    with open(raw_path, "w") as file:
        json.dump(data, file, indent=4)


if __name__ == "__main__":
    data = fetch_weather_data()
    save_raw_data(data)
    print("Raw weather data fetched and saved successfully.")
