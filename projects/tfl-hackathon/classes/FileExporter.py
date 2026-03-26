import json
import xml.etree.ElementTree as ET
from datetime import datetime


class FileExporter:
    @staticmethod
    def get_date():
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    @staticmethod
    def export_to_json(line_name: str, status: str, filename: str = "output.json"):
        entry = {
            "line": line_name,
            "status": status,
            "date": FileExporter.get_date()
        }

        try:
            with open(f"{line_name}_{filename}", "r", encoding="utf-8") as f:
                data = json.load(f)
        except:
            data = []

        if not isinstance(data, list):
            data = [data]

        data.append(entry)

        with open(f"{line_name}_{filename}", "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)

        return f"Saved JSON to {line_name}_{filename}"

    @staticmethod
    def export_to_xml(line_name: str, status: str, filename: str = "output.xml"):
        try:
            tree = ET.parse(f"{line_name}_{filename}")
            root = tree.getroot()
        except:
            root = ET.Element("line_status_history")
            tree = ET.ElementTree(root)

        entry = ET.SubElement(root, "entry")

        ET.SubElement(entry, "line").text = line_name
        ET.SubElement(entry, "status").text = status
        ET.SubElement(entry, "date").text = FileExporter.get_date()

        tree.write(f"{line_name}_{filename}", encoding="utf-8", xml_declaration=True)

        return f"Saved XML to {line_name}_{filename}"