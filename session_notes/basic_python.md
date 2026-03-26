# Session One - Code Assist

## TFL Program

```python
import requests

lines = ["Bakerloo", "Central", "Circle", "District", "Jubilee", "Metropolitan", "Northern", "Piccadilly", "Victoria"]


key = "your-tfl-api-key"

for line in lines:

    response = requests.get(f"https://api.tfl.gov.uk/Line/{line}/status?app_key={key}")
    
    if response.status_code == 200:
        data = response.json()
        service = data[0]['lineStatuses'][0]['statusSeverityDescription']
        
        print(f"{line} line has {service}")
    else:
        print(f"{line} returned status code {response.status_code}.")
```



## If statement task

```python
import datetime

current_month = datetime.datetime.now().month
print(current_month)
```


## List task

```python
continents = ["africa", "Africa", "north murica", "South America", "Antartica", "europe"]
```

## Dictionary task

```python
customers = [
    {
        "name": "Alex Turner",
        "age": 34,
        "member_since": 2019,
        "current_speed": 150,
        "devices": ["router", "TV box", "smartphone"]
    },
    {
        "name": "Priya Shah",
        "age": 28,
        "member_since": 2021,
        "current_speed": 150,
        "devices": ["router", "tablet"]
    },
    {
        "name": "Michael O'Connor",
        "age": 45,
        "member_since": 2017,
        "current_speed": 500,
        "devices": ["router", "laptop", "WiFi booster"]
    },
    {
        "name": "Sophie Williams",
        "age": 31,
        "member_since": 2016,
        "current_speed": 180,
        "devices": ["router", "games console"]
    }
]
```
