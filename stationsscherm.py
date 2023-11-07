import tkinter as tk
from tkinter import messagebox
import requests
import json

# weather data from the OpenWeatherMap API
def get_weather(api_key, station_location):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={station_location}&appid={api_key}"
    response = requests.get(url)
    data = json.loads(response.text)
    weather_description = data['weather'][0]['description']
    temperature = data['main']['temp'] - 273.15  # Convert to Celsius
    return f"Weather: {weather_description}, Temperature: {temperature:.2f}°C"

