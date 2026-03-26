# Python Challenge: Weather API with Latitude and Longitude

In this challenge, you will build a small Python program that fetches live weather data using an API.

You will practice:

- making HTTP requests with `requests`
- working with JSON data
- using latitude and longitude
- writing reusable functions
- looping through a list of dictionaries
- handling simple errors

---

## Goal

Create a program that:

1. takes latitude and longitude values
2. calls a weather API
3. retrieves the current temperature
4. prints a formatted weather report for one or more locations

---

## API to Use

Use the **Open-Meteo API** (no API key required):

```
https://api.open-meteo.com/v1/forecast
```

Example request format:

```
https://api.open-meteo.com/v1/forecast?latitude=LAT&longitude=LON&current_weather=true
```

---

## Challenge 1: Fetch Weather for One Location

Write a function called:

```python
get_weather(lat, lon, location_name)
```

### Requirements

- Build the API URL using the given latitude and longitude
- Send a request using `requests.get()`
- Extract the **current temperature** from the response
- Return a formatted string like:

```python
"Paris: 12.3 degrees C"
```

---

## Challenge 2: Handle Errors

Improve your function so it doesn’t crash if something goes wrong.

- Use `try` / `except`
- Return a simple error message if the API request fails

---

## Challenge 3: Store Multiple Locations

Create a list of dictionaries where each dictionary contains:

- `"name"`
- `"lat"`
- `"lon"`

Example:

```python
locations = [
    {"name": "Hong Kong", "lat": 22.3193, "lon": 114.1694},
    {"name": "Paris", "lat": 48.8566, "lon": 2.3522}
]
```

---

## Challenge 4: Loop Through Locations

Write a function:

```python
print_weather_report(locations)
```

### Requirements

- Loop through the list of locations
- Call your `get_weather()` function for each one
- Print the result

---

## Expected Output

Your program should print something like:

```
Hong Kong: 26.4 degrees C
Paris: 11.2 degrees C
Cairo: 24.8 degrees C
Tokyo: 17.1 degrees C
New York: 9.6 degrees C
```

(Note: values will vary depending on live weather data)

---

## Suggested Structure

```python
import requests

def get_weather(lat, lon, location_name):
    pass


def print_weather_report(locations):
    pass


locations = [
    # your data here
]

print_weather_report(locations)
```

---

## Extension Ideas

If you finish early, try:

- rounding the temperature
- printing wind speed (`current_weather["windspeed"]`)
- printing weather time
- skipping locations that fail
- letting the user input their own coordinates

---

## Reflection Questions

- Why is a function useful here?
- Why use a list of dictionaries instead of separate variables?
- What part of the JSON response contains the temperature?
- How could you extend this into a real app?

---

This is a great exercise for learning how real-world APIs work in Python 🚀

