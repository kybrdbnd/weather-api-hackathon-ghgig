import requests
import sys
import json
import argparse
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")


BASE_URL = "https://api.openweathermap.org/data/2.5"


def get_weather(lat: float, long: float) -> dict:
    params = {"lat": lat, "lon": long, "appid": API_KEY, "units": "metric"}
    url = f"{BASE_URL}/weather"
    try:
        req = requests.get(url, params=params)
        req.raise_for_status()
        res = req.json()
        return res
    except requests.exceptions.HTTPError as e:
        raise Exception(f"Error: {e}")


def parse_weather_data(data):
    city = data["name"]
    temp = data["main"]["temp"]
    description = data["weather"][0]["description"]
    return f"{city}: {temp}°C, {description}"


# def parse_arguments():
#     parser = argparse.ArgumentParser(description="Get weather information for a city.")
#     parser.add_argument("city", help="City name to get the weather forecast.")
#     return parser.parse_args()


if __name__ == "__main__":
    # args = parse_arguments()
    # city_name = args.city
    lat = 28.7041
    long = 77.1025
    weather_data = get_weather(lat, long)
    weather_report = parse_weather_data(weather_data)
    print(weather_report)
