import requests
from .FileExporter import FileExporter

class TFLClient:
    
    BASE_URL = "https://api.tfl.gov.uk/Line/"
    VALID_LINES = ["bakerloo", "circle", "district", "hammersmith-city", "jubilee", "metropolitan", "northern", "piccadilly", "victoria", "waterloo"]
    
    def __init__(self, line: str, key: str):
        self.original_line = line
        self.line = self.process_line(line)
        self.key = key
        
    @staticmethod
    def process_line(line: str):
        line_lower_case = line.strip().lower()
        line_no_and = line_lower_case.replace("and", "") 
        line_no_ampersand = line_no_and.replace("&", "")
        line_clean_spaces = " ".join(line_no_ampersand.split())
        line_dashes_instead_of_whitespace = line_clean_spaces.replace(" ", "-")
        processed_line = line_dashes_instead_of_whitespace
        if processed_line in TFLClient.VALID_LINES: 
            return processed_line
        else:
            return False
         
        
    def get_line_status(self):
        
        if self.line == False:
            return "Invalid line"
        
        try:
            response = requests.get(f"{self.BASE_URL}{self.line}/status?app_key={self.key}")
            if response.status_code == 200:
                data = response.json()
                line_status = data[0]['lineStatuses'][0]['statusSeverityDescription']
                FileExporter.export_to_json(self.line, line_status)
                FileExporter.export_to_xml(self.line, line_status)
                return f"{self.original_line.title()}: {line_status}"
            else:
                return response.status_code
            
        except:
            return "Error"
        