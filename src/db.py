import os
import psycopg2
from dotenv import load_dotenv
import csv
from datetime import datetime

load_dotenv()  # loading variables z .env

def get_connection():
    return psycopg2.connect(
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD")
    )

def insert_weather_data(csv_path: str):
    conn = get_connection()
    cur = conn.cursor()

    with open(csv_path, newline='', encoding='utf-8') as file:
        next(file)  # pomijamy nagłówek
        reader = csv.reader(file)
        for row in reader:
            datetime_str, temp, hum = row
            cur.execute("""
                INSERT INTO weather_data (datetime, temperature_2m, relative_humidity_2m)
                VALUES (%s, %s, %s)
                ON CONFLICT (datetime) DO NOTHING;
            """, (datetime_str, float(temp), float(hum)))

    conn.commit()
    cur.close()
    conn.close()
    print(f"✅ Data from {csv_path} was loaded to DB.")
