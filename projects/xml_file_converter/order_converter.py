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
    # RECIEVE THE PYTHON DICT AND ADD A FILE NAME
    def dict_to_xml_file(data: dict, filename: str):
        # DEFINE THE ROOT ELEMENT
        root = ET.Element("order")
        # CREATE CHILD OF ROOT CALLED ITEMS
        items_elem = ET.SubElement(root, "items")

        # ITERATE OVER ITEMS LIST
        for item in data["items"]:
            # FOR EACH SINGULAR ITEM CREATED A CHILD ELEMENT FOR ITEMS ELEMEMENT
            item_elem = ET.SubElement(items_elem, "item")

            
            # CREATE A CHILD ELEMENT FOR EACH ITEM ELEMENT
            name_elem = ET.SubElement(item_elem, "name")
            # GIVE TE VALUE TAKEN FROM THE NESTED DICTIONARY KEY
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
