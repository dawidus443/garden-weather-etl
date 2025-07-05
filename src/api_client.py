# src/api_client.py

import requests
from datetime import datetime


def fetch_weather_data(latitude, longitude, start_date=None, end_date=None):
    """Fetch hourly weather data from Open-Meteo API."""

    today = datetime.today().strftime('%Y-%m-%d')
    start = start_date or today
    end = end_date or today

    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "start_date": start,
        "end_date": end,
        "hourly": "temperature_2m,relative_humidity_2m",
        "timezone": "Europe/Warsaw"
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json().get("hourly", {})

    except requests.RequestException as e:
        print(f"API error: {e}")
        return None
