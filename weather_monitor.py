import requests
import time
import sqlite3
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("API_KEY")
CITIES = ["Delhi", "Mumbai", "Chennai", "Bangalore", "Kolkata", "Hyderabad"]

# Function to convert Kelvin to Celsius
def kelvin_to_celsius(temp_kelvin):
    return temp_kelvin - 273.15

# Initialize database
def init_db():
    conn = sqlite3.connect('weather.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS weather_data
                 (city TEXT, timestamp INTEGER, temperature REAL, feels_like REAL, weather TEXT)''')
    conn.commit()
    conn.close()

def store_weather_data(city, temperature, feels_like, weather, timestamp):
    conn = sqlite3.connect('weather.db')
    c = conn.cursor()
    c.execute('INSERT INTO weather_data (city, timestamp, temperature, feels_like, weather) VALUES (?, ?, ?, ?, ?)',
              (city, timestamp, temperature, feels_like, weather))
    conn.commit()
    conn.close()

# Function to fetch weather data from OpenWeatherMap
def fetch_weather_data():
    for city in CITIES:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
        response = requests.get(url).json()

        if response.get("main"):
            temperature = kelvin_to_celsius(response["main"]["temp"])
            feels_like = kelvin_to_celsius(response["main"]["feels_like"])
            weather = response["weather"][0]["main"]
            timestamp = response["dt"]

            store_weather_data(city, temperature, feels_like, weather, timestamp)
            print(f"Weather for {city} stored successfully.")
        else:
            print(f"Error fetching data for {city}")
