import requests
from geopy.geocoders import Nominatim
from supersecretapi import *


def get_weather(city):
    geolocator = Nominatim(user_agent="city")
    location = geolocator.geocode(city)

    if location:
        lat = location.latitude
        long = location.longitude
        response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={long}&appid={secret_api}")

        if response.status_code == 200:
            json_data = response.json()
            celsius = json_data["main"]["temp"] - 273.15
            current_weather = json_data["weather"][0]["description"]
            print(f"The current weather in {city} is:\n{current_weather.capitalize()}\nTemperature: {celsius:.2f} C")

        else:
            print("Nothing was found.")

    else:
        print("Something went wrong with your search term. Try again.")


city = input("Enter a city:\n")
get_weather(city)




