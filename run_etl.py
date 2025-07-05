from src.api_client import fetch_weather_data
from src.utils import save_weather_to_csv
from src.db import insert_weather_data
import os

if __name__ == "__main__":
    latitude = 52.2297
    longitude = 21.0122

    weather_data = fetch_weather_data(latitude, longitude)

    if weather_data:
        output_path = os.path.join("data", "raw", "weather_data.csv")
        os.makedirs("data/raw", exist_ok=True)
        save_weather_to_csv(weather_data, output_path)
        insert_weather_data(output_path)
    else:
        print("Failed to get data from API.")
