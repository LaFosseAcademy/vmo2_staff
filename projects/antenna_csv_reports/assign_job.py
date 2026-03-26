import json
import requests

def find_closest_engineer(antenna):
    
    antenna_longitude = antenna.longitude
    antenna_latitude = antenna.latitude
    
    with open("./staff/engineers.json", "r", encoding="utf-8")as f:
        engineers = json.load(f)
        
    closest_engineer = None
    closest_distance = float("inf")
    
    for engineer in engineers:
        distance_x = engineer["longitude"] - antenna_longitude
        distance_y = engineer["latitude"] - antenna_latitude
        distance = distance_x**2 + distance_y **2
        
        if distance < closest_distance:
            closest_distance = distance
            closest_engineer = engineer
    
    return closest_engineer





def fetch_weather(antenna):
    antenna_longitude = antenna.longitude
    antenna_latitude = antenna.latitude
    
    response = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={antenna_latitude}&longitude={antenna_longitude}&current_weather=true")
    if response.status_code == 200:
        data = response.json()
        weather = {
            "temp_c": data["current_weather"]["temperature"],
            "windspeed": data["current_weather"]["windspeed"]
        }
        return weather
    else:
        return "Unable to retrieve weather"
