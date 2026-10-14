import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("WEATHER_API_KEY")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


def get_weather(city):
    if not API_KEY:
        print("API key missing. Check your .env file.")
        return

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(
            BASE_URL, params=params, timeout=10
        )

        if response.status_code == 200:
            data = response.json()

            print("\n--- Weather Report ---")
            print("City:", data["name"])
            print("Temperature:", data["main"]["temp"], "°C")
            print("Feels Like:", data["main"]["feels_like"], "°C")
            print("Humidity:", data["main"]["humidity"], "%")
            print("Condition:", data["weather"][0]["description"])
            print("Wind Speed:", data["wind"]["speed"], "m/s")

        elif response.status_code == 404:
            print("City not found. Please check the spelling.")
        elif response.status_code == 401:
            print("Invalid or inactive API key.")
        else:
            print("Request failed:", response.status_code)

    except requests.exceptions.RequestException as error:
        print("Network error:", error)


if __name__ == "__main__":
    city = input("Enter city name: ").strip()

    if city:
        get_weather(city)
    else:
        print("Please enter a city name.")


