# Day 1

## Large Data Task

```python
o2_academy_sites_uk = (
    {
        "name": "O2 Academy Brixton",
        "location": {
            "city": "London",
            "region": "Greater London",
            "postcode": "W2 6HY",
        },
        "primary_use": "live music",
        "secondary_uses": ["club nights", "stand-up comedy", "corporate events", "community showcases"],
        "capacity": {"standing": 1800, "seated": 750, "total": 2550},
        "operations": {"staff": ["Mark Catney", "Faizal Shajahan"]},
    },
    {
        "name": "O2 Academy Manchester",
        "location": {
            "city": "Manchester",
            "region": "Greater Manchester",
            "postcode": "M4 6BF",
        },
        "primary_use": "live music",
        "secondary_uses": ["club nights", "podcast tapings", "brand activations"],
        "capacity": {"standing": 1850, "seated": 770, "total": 2620},
        "operations": {"staff": ["Behnam Bahmani"]},
    },
    {
        "name": "O2 Academy Birmingham",
        "location": {
            "city": "Birmingham",
            "region": "West Midlands",
            "address_hint": "Digbeth music quarter / rail-arch cluster",
            "postcode": "B5 6QB",
            "geo": {"lat": None, "lon": None},
        },
        "primary_use": "live music",
        "capacity": {"standing": 1900, "seated": 790, "total": 2690},
        "operations": {"staff": ["Arun Kukke", "Zahi Kozaily"]},
    },
    {
        "name": "O2 Academy Glasgow",
        "location": {
            "city": "Glasgow",
            "region": "Glasgow City",
            "postcode": "G3 8AZ",
        },
        "primary_use": "live music",
        "capacity": {"standing": 1950, "seated": 810, "total": 2760},
        "operations": {"staff": ["Asim Farooq", "Zain Ul Abideen"]},
    },
    {
        "name": "O2 Academy Leeds",
        "location": {
            "city": "Leeds",
            "region": "West Yorkshire",
            "postcode": "LS10 1JR",
        },
        "primary_use": "live music",
        "capacity": {"standing": 2000, "seated": 830, "total": 2830},
        "operations": {"staff": ["Sadaf Chaudhary"]},
    },
    {
        "name": "O2 Academy Bristol",
        "location": {
            "city": "Bristol",
            "region": "Bristol",
            "postcode": "BS1 6QF",
        },
        "primary_use": "live music",
        "capacity": {"standing": 2050, "seated": 850, "total": 2900},
        "operations": {"staff": ["Iftikhar Safdar", "Kosala Samaranayake"]},
    },
    {
        "name": "O2 Academy Newcastle",
        "location": {
            "city": "Newcastle upon Tyne",
            "region": "Tyne and Wear",
            "postcode": "NE1 3AF",
        },
        "primary_use": "live music",
        "capacity": {"standing": 2100, "seated": 870, "total": 2970},
        "operations": {"staff": ["Mark Eden", "Paul Grover"]},
    },
    {
        "name": "O2 Academy Liverpool",
        "location": {
            "city": "Liverpool",
            "region": "Merseyside",
            "postcode": "L1 0BS",
        },
        "primary_use": "live music",
        "capacity": {"standing": 2150, "seated": 890, "total": 3040},
        "operations": {"staff": ["Ehsan Gohar"]},
    },
    {
        "name": "O2 Academy Cardiff",
        "location": {
            "city": "Cardiff",
            "region": "Cardiff",
            "postcode": "CF10 5BZ",
        },
        "primary_use": "live music",
        "capacity": {"standing": 2200, "seated": 910, "total": 3110},
        "operations": {"staff": ["Sumair Chaudhary", "Saima Iftikhar"]},
    },
    {
        "name": "O2 Academy Nottingham",
        "location": {
            "city": "Nottingham",
            "region": "Nottinghamshire",
            "postcode": "NG1 1HF",
        },
        "primary_use": "live music",
        "capacity": {"standing": 2250, "seated": 930, "total": 3180},
        "operations": {"staff": ["Hassan Atique", "Burhanuddin Khaja"]},
    },
    {
        "name": "O2 Academy Sheffield",
        "location": {
            "city": "Sheffield",
            "region": "South Yorkshire",
            "postcode": "S3 8RY",
        },
        "primary_use": "live music",
        "capacity": {"standing": 2300, "seated": 950, "total": 3250},
        "operations": {"staff": ["Linda Wilkins"]},
    },
    {
        "name": "O2 Academy Edinburgh",
        "location": {
            "city": "Edinburgh",
            "region": "City of Edinburgh",
            "postcode": "EH6 6QQ",
        },
        "primary_use": "live music",
        "capacity": {"standing": 2350, "seated": 970, "total": 3320},
        "operations": {"staff": ["Simon Clemson", "Jason Leroy", "Emile Sherrott"]},
    },
)
```


## Built in String functions
```python
site_name = "London Central"
print(site_name.lower())
print(site_name.upper())

lower_site_name = "london central"
print(lower_site_name.title())

site_name_whitespace = "    London Central    "
print(site_name_whitespace.strip())

sites = "London,Birmingham,Manchester"
print(sites.split(","))
```

## Built in int & float functions
```python
string_to_int = int("42")
string_to_float = float("42.24")

pie = 3.1415926536
print(round(pie, 2))

negative_number = -10
print(abs(negative_number))

print(pow(2,3))


print(min(1,2,3,4))
print(max(1,2,3,4))


print(sum([1,2,3,4]))
```

## Built in Boolean function
```python
print(bool(1))
print(bool(0))

print(bool("Hello World"))
print(bool(""))

print(bool([]))
print(bool(["London", "Paris"]))
```


## Control Flow Challenges

### Challenge 1

Write an **if/else** statement which takes the data below and prints: 
- *Site operating normally* 
- **if**:
  - the site is active
  - latency is below 50 ms
  - users are less than 200
- Otherwise, prints *Site needs investigation*

```python
site_name = "London Central"
latency_ms = 35.5
connected_users = 120
is_active = True
```

### Challenge 1 Solution
```python
site_name = "London Central"
latency_ms = 35.5
connected_users = 120
is_active = True

if is_active == True and latency_ms < 50 and connected_users < 200:
    print("Site operating normally")
else:
    print("Site needs investigation")
```

### Challenge 2 

Write a series of **if/elif/else** statements which takes the data below and prints:
- *Site offline*
  - If the site is **not active**
- *Site operating nomrally* 
  - If the site is **active** and:
    - latency < 50
    - packet_loss < 1
    - connected_users < 150
- *Site experiencing latency issues*
  - If the latency is between 50 and 100
- *Network packet loss detected*
  - If packet loss is greater than 1.5
- *Site overloaded*
  - If connected users are greater than 200
- *Site operating with major issues*
  - If issues with latency, packet loss and connected users exist above given thresholds
- *Site operating with minor issues*
  - For any other situation

```python
site_name = "Manchester Central"
latency_ms = 72.4
connected_users = 230
packet_loss = 1.8
is_active = True
```

### Challenge 2 Solution 
```python
site_name = "Manchester Central"
latency_ms = 72.4
connected_users = 230
packet_loss = 1.8
is_active = True

if is_active == False:
    print("Site offline")
elif latency_ms < 50 and packet_loss < 1 and connected_users < 150:
    print("Site operating normally")
elif latency_ms >= 50 and packet_loss > 1.5 and connected_users > 200:
    print("Site operating with major issues")
elif latency_ms >= 50 and latency_ms <= 100:
    print("Site experiencing latency issues")
elif packet_loss > 1.5:
    print("Network packet loss detected")
elif connected_users > 200:
    print("Site overloaded")
else:
    print("Site operating with minor issues")
```


## Loops

### For Loops
```python
devices = ["Router", "Mobile", "Landline"]

for i, device in enumerate(devices):
    print(i, device)
```

### While Loops
```python
attempts = 0
max_attempts = 3
password = "LaFosse"

while attempts < max_attempts:
    user_input = input("Enter password: ")

    if user_input == password:
        print("Access granted")
        break
    else:
        print("Incorrect password")
        attempts += 1

if attempts == max_attempts:
    print("Maximum attempts reached")
    
print("End of script")
```

### Loop Challenge
```python
checkout_items = [
    {"name": "Laptop", "price": 900.99, "internet_connection_needed": True},
    {"name": "Printer", "price": 52.99, "internet_connection_needed": False},
    {"name": "Smart TV", "price": 349.00, "internet_connection_needed": True},
    {"name": "USB Drive", "price": 15.99, "internet_connection_needed": False},
]
```

### Loop Challenge Solution
```python
checkout_items = [
    {"name": "Laptop", "price": 900.99, "internet_connection_needed": True},
    {"name": "Printer", "price": 52.99, "internet_connection_needed": False},
    {"name": "Smart TV", "price": 349.00, "internet_connection_needed": True},
    {"name": "USB Drive", "price": 15.99, "internet_connection_needed": False},
]

for item in checkout_items:
    if item["internet_connection_needed"]:
        print("Broadband subscription required")
        break
```

## Functions

```python
customer_speed = 300

def upgrade_speed(current_speed, speed_increase):
    current_speed += speed_increase
    return f"Customer speed is now {current_speed}"


print(upgrade_speed(customer_speed, 100))
```

### Manipulating data within a function
```python
user = {
    "name": "Emile",
    "broadband_speed": 100,
    "is_vip": False,
    "devices": ["Router", "Mobile", "Smart TV"],
    "member_since": "2018/01/12"
}

def offer_vip(customer):
    member_start_year = int(customer["member_since"].split("/")[0])
    vip_eligable = member_start_year < 2020 and customer["is_vip"] == False
    return vip_eligable
    
print(offer_vip(user))
```

### Function Exercise
```python
emile = {
    "name": "Emile",
    "broadband_speed": 100,
    "is_vip": False,
    "devices": ["Router", "Mobile", "Smart TV"],
    "member_since": "2018/01/12",
    "address_information_present": False,
    "mobile_number": +447123456789
}
```

### Function Exercise Solution

```python
emile = {
    "name": "Emile",
    "broadband_speed": 100,
    "is_vip": False,
    "devices": ["Router", "Mobile", "Smart TV"],
    "member_since": "2018/01/12",
    "address_information_present": False,
    "mobile_number": +447123456789
}

def contact_customer_for_upgrade(user):
    """
    Checks a customer's broadband speed and contacts them if an upgrade is recommended.

    If the customer's broadband speed is below 200 Mbps, the function determines
    the appropriate contact method:
    - Sends a letter if address information is available
    - Sends an SMS if no address is present

    If the broadband speed is 200 Mbps or higher, no action is taken.

    Args:
        user (dict): A dictionary containing customer information, including:
            - name (str)
            - broadband_speed (int)
            - address_information_present (bool)
            - mobile_number (int or str)

    Returns: 
        str: Whether contact is required and method
    """
    if user["broadband_speed"] < 200:
        if user["address_information_present"]:
            print(f"Sending upgrade letter to {user['name']}'s address.")
        else:
            print(f"Sending SMS to {user['mobile_number']} about broadband upgrade.")
    else:
        print("No contact needed.")
        
        
# help(contact_customer_for_upgrade)

contact_customer_for_upgrade(emile)
```


### Optional & Union Challenge Solution
```python
from typing import Optional

def calculate_total(base_cost: float, discount: Optional[int] = None) -> float:
    """
    Calculates the final total cost after applying an optional discount.

    If no discount is provided (i.e. discount is None), the base cost is
    returned unchanged. Otherwise, the discount value is subtracted from
    the base cost.

    Args:
        base_cost (float): The original cost before any discount.
        discount (Optional[int]): The discount amount to apply, or None.

    Returns:
        float: The final calculated cost.
    """
    if discount is None:
        return base_cost
    else: 
        return base_cost - discount
    
print(calculate_total(50.34))
```
