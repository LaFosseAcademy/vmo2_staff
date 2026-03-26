from classes.TFLClient import TFLClient 


waterloo = TFLClient("Hammersmith and city", "")
print(waterloo.get_line_status())