# ST02-ex02-api-weather.py

# ===================================================
# API Request for weather forecast for Waco, TX
# FWD – National Weather Service office
#       in the Fort Worth forecast region
# Grid Point (95,68) - Waco
# ===================================================

import requests

# -----------------------------
# Call the API
# ---------------------------- -
url = "https://api.weather.gov/gridpoints/FWD/95,68/forecast"
response = requests.get(url)


# -----------------------------
# Convert the payload to a dict
# -----------------------------
data = response.json()

# -----------------------------
# Consume the payload
# -----------------------------

today = data["properties"]["periods"][0]
print("Day: ", today["name"])
print("Temp: ", today["temperature"])
print("Unit: ", today["temperatureUnit"])
print()
print(
    f"Day: {today['name']}, the weather is {today['temperature']}{today['temperatureUnit']}"
)
