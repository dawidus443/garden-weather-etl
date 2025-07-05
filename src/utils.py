import csv


def save_weather_to_csv(weather_data: dict, output_file: str) -> None:
    """Saving weather data to CSV file."""

    times = weather_data.get("time", [])
    temps = weather_data.get("temperature_2m", [])
    humidity = weather_data.get("relative_humidity_2m", [])

    with open(output_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["datetime", "temperature_2m", "relative_humidity_2m"])

        for t, temp, hum in zip(times, temps, humidity):
            writer.writerow([t, temp, hum])

    print(f"✅ Data saved to {output_file}")
