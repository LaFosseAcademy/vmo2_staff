# Day 4 & 5

## Cat Breed Challenge soltion
```python
import requests

response = requests.get("https://catfact.ninja/breeds")

if response.status_code == 200:
    data = response.json()
    data_list = data["data"]
    for single_cat in data_list:
        print(f"The cat breed {single_cat["breed"]} comes from {single_cat["country"]} and has a {single_cat["pattern"].lower()} {single_cat["coat"].lower()} coat.")
else:
    print("Request failed")
```


## RESTcountries API
```txt
https://restcountries.com/
```

## RESTcountries Challenge solution
```python
import requests


country_input = input("What country do you want to see border information about? ").lower()
response = requests.get(f"https://restcountries.com/v3.1/name/{country_input}?fields=borders")

if response.status_code == 200:
    data = response.json()
    
    if len(data[0]["borders"]) == 0:
        print(f"{country_input.title()} has no borders")
    else:
        countries_list = []
        for country in data[0]["borders"]:
            response = requests.get(f"https://restcountries.com/v3.1/alpha/{country.lower()}")
            if response.status_code == 200:
                country_data = response.json()
                countries_list.append(country_data[0]["name"]["official"])
        
        print(f"{country_input.title()} shares borders with: {", ".join(countries_list)}.")
else:
    print("Request failed")
```

## XML Starter 1
```python
import xml.etree.ElementTree as ET

xml_data = """
<customer>
  <name>Alex</name>
  <age>32</age>
</customer>
"""
```

### XML End 1
```python
import xml.etree.ElementTree as ET

customer = {
    "name": "Alex",
    "age": 32
}

root = ET.Element("customer")

name_element = ET.SubElement(root, "name")
name_element.text = customer["name"]

age_element = ET.SubElement(root, "age")
age_element.text = str(customer["age"])

tree = ET.ElementTree(root)
tree.write("customer.xml", encoding="utf-8", xml_declaration=True)
```

## XML Starter: Element Duplicates
```python
import xml.etree.ElementTree as ET

xml_data = """
<items>
    <item>Router</item>
    <item>Mobile</item>
    <item>Laptop</item>
</items>
"""

root = ET.fromstring(xml_data)
```

### XML Element Duplicates Parsing To Python
```python
import xml.etree.ElementTree as ET

xml_data = """
<items>
    <item>Router</item>
    <item>Mobile</item>
    <item>Laptop</item>
</items>
"""

root = ET.fromstring(xml_data)

items = []

for item in root.findall("item"):
    items.append(item.text)
    
print(items)
```

### Python List Persisted in XML
```python
import xml.etree.ElementTree as ET

items = ["Router", "Mobile", "Laptop"]

root = ET.Element("items")

for item in items:
    item_element = ET.SubElement(root, "item")
    item_element.text = item

tree = ET.ElementTree(root)
tree.write("items.xml", encoding="utf-8", xml_declaration=True)
```

### XML Deeply Nested Example Parsed to Python
```python
import xml.etree.ElementTree as ET

xml_data = """
<order>
    <items>
        <item>
            <name>Router</name>
        </item>
        <item>
            <name>Mobile</name>
        </item>
        <item>
            <name>Laptop</name>
        </item>
    </items>
</order>
"""

root = ET.fromstring(xml_data)

order_dict = {
    "items": []
}

for item in root.find("items").findall("item"):
    name = item.find("name").text
    order_dict["items"].append({"name": name})

print(order_dict)
```


## XML Class Challenge Starter
```python
import xml.etree.ElementTree as ET
import json

xml_data = """
<order>
    <items>
        <item>
            <name>Router</name>
            <price>89.99</price>
            <quantity>1</quantity>
            <sku>RTR-001</sku>
        </item>
        <item>
            <name>Mobile</name>
            <price>599.99</price>
            <quantity>2</quantity>
            <sku>MOB-204</sku>
        </item>
        <item>
            <name>Laptop</name>
            <price>1299.99</price>
            <quantity>1</quantity>
            <sku>LTP-550</sku>
        </item>
    </items>
</order>
"""


import xml.etree.ElementTree as ET
import json


class OrderConverter:

    @staticmethod
    def xml_to_dict(xml_string):
        root = ET.fromstring(xml_string)

        order_dict = {"items": []}

        # ADD CODE HERE

        return order_dict



    @staticmethod
    def dict_to_xml_file(data: dict, filename: str):
        root = ET.Element("order")
        items_elem = ET.SubElement(root, "items")

        # ADD CODE HERE

        tree = ET.ElementTree(root)
        tree.write(filename, encoding="utf-8", xml_declaration=True)



    @staticmethod
    def dict_to_json_file(data: dict, filename: str):
        # ADD CODE HERE


python_dict = OrderConverter.xml_to_dict(xml_data)

OrderConverter.dict_to_xml_file(python_dict, "orders.xml")
OrderConverter.dict_to_json_file(python_dict, "orders.json")
```

### XML Class Challenge Solution
```python
import xml.etree.ElementTree as ET
import json

xml_data = """
<order>
    <items>
        <item>
            <name>Router</name>
            <price>89.99</price>
            <quantity>1</quantity>
            <sku>RTR-001</sku>
        </item>
        <item>
            <name>Mobile</name>
            <price>599.99</price>
            <quantity>2</quantity>
            <sku>MOB-204</sku>
        </item>
        <item>
            <name>Laptop</name>
            <price>1299.99</price>
            <quantity>1</quantity>
            <sku>LTP-550</sku>
        </item>
    </items>
</order>
"""


import xml.etree.ElementTree as ET
import json


class OrderConverter:

    @staticmethod
    def xml_to_dict(xml_string):
        root = ET.fromstring(xml_string)

        order_dict = {"items": []}

        for item in root.find("items").findall("item"):
            item_data = {
                "name": item.find("name").text,
                "price": float(item.find("price").text),
                "quantity": int(item.find("quantity").text),
                "sku": item.find("sku").text
            }
            order_dict["items"].append(item_data)

        return order_dict

    @staticmethod
    def dict_to_xml_file(data: dict, filename: str):
        root = ET.Element("order")
        items_elem = ET.SubElement(root, "items")

        for item in data["items"]:
            item_elem = ET.SubElement(items_elem, "item")

            
            name_elem = ET.SubElement(item_elem, "name")
            name_elem.text = item["name"]

            price_elem = ET.SubElement(item_elem, "price")
            price_elem.text = str(item["price"])

            quantity_elem = ET.SubElement(item_elem, "quantity")
            quantity_elem.text = str(item["quantity"])

            sku_elem = ET.SubElement(item_elem, "sku")
            sku_elem.text = item["sku"]

        tree = ET.ElementTree(root)
        tree.write(filename, encoding="utf-8", xml_declaration=True)

    @staticmethod
    def dict_to_json_file(data: dict, filename: str):
        with open(filename, "w") as f:
            json.dump(data, f, indent=4)


python_dict = OrderConverter.xml_to_dict(xml_data)

OrderConverter.dict_to_xml_file(python_dict, "orders.xml")
OrderConverter.dict_to_json_file(python_dict, "orders.json")
```

## XML Class Challenge Clean Solution
```python
import xml.etree.ElementTree as ET
import json


xml_data = """
<order>
    <items>
        <item>
            <name>Router</name>
            <price>89.99</price>
            <quantity>1</quantity>
            <sku>RTR-001</sku>
        </item>
        <item>
            <name>Mobile</name>
            <price>599.99</price>
            <quantity>2</quantity>
            <sku>MOB-204</sku>
        </item>
        <item>
            <name>Laptop</name>
            <price>1299.99</price>
            <quantity>1</quantity>
            <sku>LTP-550</sku>
        </item>
    </items>
</order>
"""



class OrderConverter:

    @staticmethod
    def xml_to_dict(xml_string):
        root = ET.fromstring(xml_string)

        order_dict = {"items": []}

        for item in root.find("items").findall("item"):
            item_data = {
                "name": item.find("name").text,
                "price": float(item.find("price").text),
                "quantity": int(item.find("quantity").text),
                "sku": item.find("sku").text
            }
            order_dict["items"].append(item_data)

        return order_dict



    @staticmethod
    def dict_to_xml_file(data, filename):
        root = ET.Element("order")
        items_elem = ET.SubElement(root, "items")

        for item in data["items"]:
            item_elem = ET.SubElement(items_elem, "item")

            for key, value in item.items():

                child_elem = ET.SubElement(item_elem, key)
                child_elem.text = str(value)

        tree = ET.ElementTree(root)
        tree.write(filename, encoding="utf-8", xml_declaration=True)



    @staticmethod
    def dict_to_json_file(data, filename):
        with open(filename, "w") as f:
            json.dump(data, f, indent=4)


python_dict = OrderConverter.xml_to_dict(xml_data)
OrderConverter.dict_to_xml_file(python_dict, "orders.xml")
OrderConverter.dict_to_json_file(python_dict, "orders.json")
```
