# Python Challenge: OpenMeteo API with Latitude and Longitude — Solutions

These solutions show one clear way to solve the OpenWeather API challenge.

They include:

- using `requests` to call the API
- getting weather by latitude and longitude
- using a list of dictionaries
- looping through multiple locations
- printing a simple weather report
- basic error handling

---

## Full Solution

```python
import requests


def get_weather(lat, lon, location_name):
    url = f"https://api.open-meteo.com/v1/forecast?latitude={str(lat)}&longitude={str(lon)}&current_weather=true"
    
    try:
        response = requests.get(url)

        data = response.json()
        temperature = data["current_weather"]["temperature"]

        return f"{location_name}: {temperature} degrees C"

    except:
        return "Error in API request"


def print_weather_report(locations):
    for location in locations:
        name = location["name"]
        lat = location["lat"]
        lon = location["lon"]

        result = get_weather(lat, lon, name)
        print(result)


locations = [
    {"name": "Hong Kong", "lat": 22.3193, "lon": 114.1694},
    {"name": "Paris", "lat": 48.8566, "lon": 2.3522},
    {"name": "Cairo", "lat": 30.0444, "lon": 31.2357},
    {"name": "Tokyo", "lat": 35.6762, "lon": 139.6503},
    {"name": "New York", "lat": 40.7128, "lon": -74.0060}
]

print_weather_report(locations)
```

