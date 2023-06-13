import requests
import sys
import json
import argparse

def get_weather(city):
    api_key = "YOUR_API_KEY"
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": api_key, "units": "metric"}

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.HTTPError as e:
        print(f"Error: {e}")
        sys.exit(1)

def parse_weather_data(data):
    city = data["name"]
    temp = data["main"]["temp"]
    description = data["weather"][0]["description"]
    return f"{city}: {temp}°C, {description}"

def parse_arguments():
    parser = argparse.ArgumentParser(description="Get weather information for a city.")
    parser.add_argument("city", help="City name to get the weather forecast.")
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_arguments()
    city_name = args.city
    weather_data = get_weather(city_name)
    weather_report = parse_weather_data(weather_data)
    print(weather_report)
