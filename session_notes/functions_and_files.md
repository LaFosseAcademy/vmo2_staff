# Session Two Code Utilised

## Default Parameters
```python
def calculate_speed_difference(current_speed, new_speed=1000):
    """Return how much faster teh new speed is compared to the current one"""
    difference = new_speed - current_speed
    message = return_message(difference)
    return message

def return_message(speed_difference):
    if speed_difference > 0:
        return f"Your speed increase will be {speed_difference}Mbs"
    else:
        return f"Your speed decrease will be {abs(speed_difference)}Mbs"

print(calculate_speed_difference(350, 500))
print(calculate_speed_difference(350))
```

## Restaurant Bill Calculator 

```python
def calculate_bill(total, service_charge=12.5):
    return total + ((total / 100) * service_charge)

print(f"Your bill is: {calculate_bill(100)}")
print(f"Your bill is: {calculate_bill(100, 10)}")
```

## Mutable Parameters
```python
def add_device(device, devices=None):
    if devices is None:
        devices = []
    devices.append(device)
    return devices

emiles_devices = add_device("Mobile")
simons_devices = add_device("TV")

print(emiles_devices)
print(simons_devices)

edmiles_devices = add_evice("Router", emiles_devices)
print(emiles_devices)
```

## Variadic Functions
```python
def log_equipment(*items, **details):
    print("Equipment found:", items)
    for item in items:
        if item == "Battery Backup":
            battery_found()
    
    if details:
        # NEW CODE
        for key, value in details.items():
            print(f"{key} - {value}")

def battery_found():
    print("**** Battery found, process for safe disposal ****")

log_equipment("Radio Unit", "Antenna", "Battery Backup", site="O2 Academy Brixton", region="South London")
```


## JSON reading and writing
```python
import json  

data = {
    "customer": "Alex",
    "speed": 500,
    "plan": "Fibre Max"
}

# Converts Python to JSON and writes to file
with open("customer.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4)

# Converts JSON to Python and reads from file
with open("customer.json", "r", encoding="utf-8") as f:
    loaded_data = json.load(f)

print("Loaded:", loaded_data)
```



## Reading CSV Data

### CSV Mock Data - vmo2-tickets.csv
```csv
ticket_id,created_date,customer_id,service,issue_type,severity,status,assigned_team
VMO2-1002,2026-01-03,CUST-55210,Mobile,Slow Data,Minor,Closed,Radio Access
VMO2-1003,2026-01-04,CUST-99102,TV,Channel Missing,Major,In Progress,TV Platform
VMO2-1004,2026-01-04,CUST-44773,Broadband,Intermittent Drop,Major,Closed,Network Ops
VMO2-1005,2026-01-05,CUST-22019,Mobile,Voicemail Issue,Minor,Closed,Core Voice
VMO2-1006,2026-01-05,CUST-77331,Broadband,Router Failure,Severe,In Progress,CPE Support
VMO2-1007,2026-01-06,CUST-66542,TV,Playback Error,Minor,Closed,TV Platform
VMO2-1008,2026-01-06,CUST-11883,Mobile,No Signal,Severe,Open,Radio Access
VMO2-1009,2026-01-07,CUST-90444,Broadband,Slow Speed,Minor,Closed,Network Ops
VMO2-1010,2026-01-07,CUST-33991,Mobile,SMS Failure,Major,In Progress,Core Messaging
VMO2-1011,2026-01-08,CUST-77220,TV,App Crash,Minor,Closed,TV Platform
VMO2-1012,2026-01-08,CUST-55678,Broadband,No Connectivity,Severe,Open,Network Ops
VMO2-1013,2026-01-09,CUST-12003,Mobile,Roaming Issue,Major,Closed,Core Voice
VMO2-1014,2026-01-09,CUST-88177,Broadband,Packet Loss,Major,In Progress,Network Ops
VMO2-1015,2026-01-10,CUST-44321,TV,Audio Sync,Minor,Closed,TV Platform
VMO2-1016,2026-01-10,CUST-66754,Mobile,No Signal,Severe,Open,Radio Access
VMO2-1017,2026-01-11,CUST-99821,Broadband,Slow Speed,Minor,Closed,Network Ops
VMO2-1018,2026-01-11,CUST-33456,TV,Channel Missing,Major,In Progress,TV Platform
VMO2-1019,2026-01-12,CUST-77109,Mobile,VoLTE Issue,Major,Closed,Core Voice
VMO2-1020,2026-01-12,CUST-55233,Broadband,Router Failure,Severe,In Progress,CPE Support
VMO2-1021,2026-01-13,CUST-88901,TV,Playback Error,Minor,Closed,TV Platform
VMO2-1022,2026-01-13,CUST-44309,Mobile,Slow Data,Minor,Closed,Radio Access
VMO2-1024,2026-01-14,CUST-77654,TV,App Crash,Minor,Closed,TV Platform
VMO2-1025,2026-01-15,CUST-11802,Mobile,SMS Failure,Major,In Progress,Core Messaging
VMO2-1026,2026-01-15,CUST-90412,Broadband,Packet Loss,Major,Closed,Network Ops
VMO2-1027,2026-01-16,CUST-66345,TV,Audio Sync,Minor,Closed,TV Platform
VMO2-1028,2026-01-16,CUST-55128,Mobile,Roaming Issue,Major,Open,Core Voice
VMO2-1029,2026-01-17,CUST-77288,Broadband,Intermittent Drop,Major,In Progress,Network Ops
VMO2-1030,2026-01-17,CUST-33904,TV,Playback Error,Minor,Closed,TV Platform
VMO2-1033,2026-01-19,CUST-77211,Broadband,Backhaul Congestion,Severe,Open,Network Ops
VMO2-1034,2026-01-19,CUST-11992,Mobile,No Signal,Major,Closed,Radio Access
VMO2-1035,2026-01-20,CUST-55310,TV,Channel Missing,Minor,Closed,TV Platform
VMO2-1036,2026-01-20,CUST-88409,Broadband,DNS Failure,Severe,In Progress,Network Ops
VMO2-1037,2026-01-21,CUST-66123,Mobile,Slow Data,Minor,Closed,Radio Access
VMO2-1039,2026-01-22,CUST-77880,TV,Playback Error,Minor,Closed,TV Platform
VMO2-1040,2026-01-22,CUST-99001,Broadband,Core Link Failure,Severe,In Progress,Network Ops
```

### Python interacting with file - main.py
```python
import csv

with open("vmo2-tickets.csv", "r", encoding="utf-8") as f:
    tickets = list(csv.DictReader(f))

def find_tickets(items, team, severity):
    for item in items:
        if item["assigned_team"] == team and item["severity"] == severity:
            print(item)

find_tickets(tickets, "Network Ops", "Severe")
```


## Writing CSV Data
```python
import csv

with open("new_vmo2_customers.csv", "w", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["customer_name", "customer_postcode", "customer_package"])
    writer.writerows([
        ["Olivia Turner", "SW1A 1AA", "Volt M200 Fibre"],
        ["James Patel", "M1 1AE", "Volt M350 Fibre"],
        ["Amelia Hughes", "B1 1BB", "Volt Gig1 Fibre"],
        ["Noah Thompson", "LS1 4AP", "Volt M125 Fibre"],
        ["Isla Campbell", "G1 2FF", "Volt M500 Fibre"],
        ["Jack Robinson", "BS1 5AH", "Volt M350 Fibre"],
        ["Ava Edwards", "CF10 1EP", "Volt M200 Fibre"],
        ["Harry Walker", "NE1 3PJ", "Volt Gig1 Fibre"],
        ["Emily Green", "L1 8JQ", "Volt M125 Fibre"],
        ["George Hall", "EH2 2YB", "Volt M500 Fibre"],
        ["Sophia Lewis", "NG1 6DQ", "Volt M350 Fibre"],
        ["Charlie Young", "OX1 1AA", "Volt M200 Fibre"],
        ["Mia King", "PL1 2AA", "Volt M125 Fibre"],
        ["Freddie Wright", "YO1 7HB", "Volt Gig1 Fibre"],
        ["Grace Scott", "BT1 5GS", "Volt M350 Fibre"],
        ["Leo Adams", "AB10 1XG", "Volt M500 Fibre"],
        ["Lily Baker", "CV1 2GT", "Volt M200 Fibre"],
        ["Oscar Nelson", "LE1 5TR", "Volt M350 Fibre"],
        ["Evie Carter", "MK9 3EP", "Volt Gig1 Fibre"],
        ["Theo Mitchell", "WD17 1EU", "Volt M125 Fibre"],
    ])
```


## VMO2 Mock Customer Data - vmo2-customers.csv
```csv
customer_id,customer_name,segment,region,join_date,product_bundle,tenure_months,customer_status,contact_number
CUST-20001,Aaron Taylor,Consumer,Bristol,2019-10-01,Mobile Only,23,Active,447700900001
CUST-20002,Hannah Morris,SMB,Manchester,2023-08-16,Broadband Only,10,Active,447700900002
CUST-20003,Lily Garcia,Consumer,London,2023-04-18,Mobile Only,97,Active,447700900003
CUST-20004,Matthew Wright,Consumer,Leicester,2020-02-14,Business Broadband,6,Inactive,447700900004
CUST-20005,Jack Collins,Consumer,Bristol,2018-09-29,Mobile Only,103,Active,447700900005
CUST-20006,Noah Hernandez,Consumer,Glasgow,2023-10-09,TV + Broadband,109,Active,447700900006
CUST-20007,Amelia Carter,Consumer,Liverpool,2017-11-19,TV Only,43,Inactive,447700900007
CUST-20008,Sofia Young,Consumer,Reading,2017-10-12,Volt Bundle,90,Active,447700900008
CUST-20009,Oscar Davies,SMB,Manchester,2021-04-06,TV + Broadband,64,Active,447700900009
CUST-20010,Isabella White,Consumer,Leeds,2024-07-08,TV + Broadband,95,Inactive,447700900010
CUST-20011,Victoria Johnson,Consumer,Birmingham,2022-12-28,Mobile + TV,37,Active,447700900011
CUST-20012,Mason Clark,SMB,Cardiff,2024-09-19,TV Only,34,Active,447700900012
CUST-20013,Natalie Reed,Consumer,London,2020-07-16,Broadband Only,40,Active,447700900013
CUST-20014,Joseph Stewart,Consumer,Cardiff,2022-08-07,Broadband Only,88,Active,447700900014
CUST-20015,Henry Moore,Consumer,Nottingham,2023-01-17,TV + Broadband,101,Active,447700900015
CUST-20016,Elizabeth King,Consumer,Birmingham,2022-09-19,Broadband Only,17,Inactive,447700900016
CUST-20017,George Jackson,Consumer,Brighton,2024-08-19,Broadband Only,82,Active,447700900017
CUST-20018,Mason Turner,SMB,Nottingham,2019-10-27,TV Only,7,Active,447700900018
CUST-20019,George Edwards,SMB,Brighton,2019-12-29,Business Broadband,88,Active,447700900019
CUST-20020,Oscar Lopez,Consumer,London,2019-12-15,TV Only,103,Active,447700900020
CUST-20021,Isla Cook,Consumer,Cardiff,2022-09-11,TV Only,31,Active,447700900021
CUST-20022,Ryan White,Consumer,Brighton,2022-12-13,Volt Bundle,82,Active,447700900022
CUST-20023,James Taylor,SMB,Brighton,2020-06-13,Mobile Only,13,Active,447700900023
CUST-20024,Joseph Davies,Consumer,Sheffield,2017-10-11,Business Broadband,74,Inactive,447700900024
CUST-20025,Harry Evans,Consumer,Nottingham,2018-11-08,TV + Broadband,73,Inactive,447700900025
CUST-20026,Charlotte Thompson,SMB,Brighton,2024-09-26,Mobile Only,97,Active,447700900026
CUST-20027,Joshua Parker,Consumer,Nottingham,2022-01-24,Volt Bundle,37,Active,447700900027
CUST-20028,Emily Patel,Consumer,Leeds,2023-08-08,Mobile Only,6,Active,447700900028
CUST-20029,Aaron Brown,Consumer,London,2020-09-15,Volt Bundle,71,Active,447700900029
CUST-20030,Joshua Adams,Consumer,Birmingham,2023-05-28,TV Only,66,Active,447700900030
CUST-20031,Michael Wright,Consumer,Manchester,2024-05-23,Broadband Only,51,Active,447700900031
CUST-20032,Amelia Sanchez,Consumer,Cardiff,2024-03-31,Volt Bundle,13,Active,447700900032
CUST-20033,Emily Wilson,Consumer,Leeds,2023-01-06,Broadband Only,23,Active,447700900033
CUST-20034,Amelia Scott,Consumer,Manchester,2021-12-21,Business Broadband,76,Active,447700900034
CUST-20035,Victoria Carter,Consumer,Manchester,2019-08-27,Mobile Only,58,Active,447700900035
CUST-20036,Lily King,SMB,Birmingham,2021-04-02,Volt Bundle,55,Active,447700900036
CUST-20037,Amelia Rodriguez,Consumer,Reading,2023-03-27,Mobile + TV,97,Active,447700900037
CUST-20038,Leo Rodriguez,Consumer,London,2023-07-01,Mobile + TV,75,Active,447700900038
CUST-20039,Ethan Brown,Consumer,Sheffield,2022-08-22,Business Broadband,73,Active,447700900039
CUST-20040,Daniel Davies,SMB,Manchester,2023-09-04,Volt Bundle,92,Inactive,447700900040
CUST-20041,Mia Taylor,SMB,Leicester,2019-10-06,TV Only,82,Active,447700900041
CUST-20042,Noah Wright,Consumer,Leicester,2022-11-12,TV + Broadband,39,Active,447700900042
CUST-20043,Zoe Walker,Consumer,Liverpool,2018-06-21,Mobile + TV,88,Active,447700900043
CUST-20044,Ethan Rogers,SMB,London,2022-02-21,TV Only,78,Inactive,447700900044
CUST-20045,Ava Carter,Consumer,Bristol,2018-06-27,TV + Broadband,14,Inactive,447700900045
CUST-20046,Isabella Rodriguez,Consumer,Nottingham,2024-11-21,TV + Broadband,84,Inactive,447700900046
CUST-20047,Victoria Nelson,Consumer,Nottingham,2020-05-11,Mobile + TV,19,Inactive,447700900047
CUST-20048,Harry Robinson,Consumer,Manchester,2023-03-17,Mobile Only,40,Active,447700900048
CUST-20049,Lily Stewart,Consumer,Cardiff,2024-02-11,Business Broadband,39,Active,447700900049
CUST-20050,Henry Brown,Consumer,Liverpool,2020-02-08,Volt Bundle,6,Active,447700900050
CUST-20051,Harry Cook,SMB,Birmingham,2021-12-15,TV Only,96,Active,447700900051
CUST-20052,Emma Taylor,Consumer,Reading,2018-09-03,TV Only,10,Inactive,447700900052
CUST-20053,Elizabeth Mitchell,Consumer,Birmingham,2017-06-21,TV + Broadband,52,Inactive,447700900053
CUST-20054,Sophia Allen,Consumer,Leeds,2024-06-24,Volt Bundle,51,Inactive,447700900054
CUST-20055,Logan Phillips,Consumer,Leeds,2018-10-28,Business Broadband,109,Active,447700900055
CUST-20056,Logan Patel,Consumer,Glasgow,2021-08-14,Business Broadband,91,Inactive,447700900056
CUST-20057,Ella Clark,Consumer,Reading,2018-03-19,Broadband Only,10,Inactive,447700900057
CUST-20058,Freddie Martin,Consumer,Sheffield,2020-12-03,TV + Broadband,107,Inactive,447700900058
CUST-20059,Freddie Patel,Consumer,Liverpool,2020-09-06,TV + Broadband,14,Inactive,447700900059
CUST-20060,Amelia Allen,Consumer,Liverpool,2024-08-15,Business Broadband,74,Active,447700900060
CUST-20061,James Taylor,SMB,Bristol,2019-01-02,TV Only,39,Active,447700900061
CUST-20062,David Lopez,Consumer,Brighton,2020-07-08,Broadband Only,83,Inactive,447700900062
CUST-20063,George Hernandez,SMB,Leeds,2019-11-10,Volt Bundle,96,Active,447700900063
CUST-20064,Harper Carter,Consumer,Reading,2024-07-09,Mobile Only,52,Active,447700900064
CUST-20065,Joshua Hall,Consumer,Cardiff,2018-05-26,Mobile + TV,44,Active,447700900065
CUST-20066,Joshua Wright,Consumer,Reading,2020-04-26,TV Only,22,Active,447700900066
CUST-20067,Joshua Hernandez,Consumer,Birmingham,2023-11-27,TV Only,44,Active,447700900067
CUST-20068,Emma Lewis,Consumer,Liverpool,2023-07-04,TV Only,89,Active,447700900068
CUST-20069,Jacob Hill,Consumer,Nottingham,2022-04-23,Business Broadband,107,Active,447700900069
CUST-20070,Joshua Davies,Consumer,Cardiff,2024-02-06,TV Only,48,Active,447700900070
CUST-20071,Ryan Martinez,Consumer,Leeds,2019-03-27,Mobile Only,9,Active,447700900071
CUST-20072,Michael Phillips,Consumer,Manchester,2022-02-09,Broadband Only,86,Active,447700900072
CUST-20073,Zoe Collins,Consumer,Liverpool,2019-09-27,Mobile Only,89,Active,447700900073
CUST-20074,Ryan Reed,SMB,Brighton,2021-10-08,Mobile Only,28,Inactive,447700900074
CUST-20075,Christopher Nelson,Consumer,Nottingham,2019-10-18,Business Broadband,21,Active,447700900075
CUST-20076,Amelia Evans,Consumer,Nottingham,2023-09-05,TV + Broadband,102,Inactive,447700900076
CUST-20077,Sofia Sanchez,SMB,Liverpool,2023-02-23,Broadband Only,26,Active,447700900077
CUST-20078,Michael Hill,Consumer,Leeds,2024-02-25,TV + Broadband,104,Inactive,447700900078
CUST-20079,Evelyn Cook,Consumer,Sheffield,2017-11-14,Mobile + TV,42,Active,447700900079
CUST-20080,Emily Walker,SMB,Manchester,2018-07-21,Mobile Only,35,Active,447700900080
CUST-20081,Mia Stewart,Consumer,Liverpool,2021-07-28,TV + Broadband,75,Active,447700900081
CUST-20082,Oliver Thompson,Consumer,Liverpool,2023-07-21,Mobile + TV,8,Inactive,447700900082
CUST-20083,Ryan Perez,Consumer,London,2020-12-11,TV + Broadband,102,Active,447700900083
CUST-20084,Logan Carter,Consumer,Nottingham,2023-10-07,Mobile Only,68,Active,447700900084
CUST-20085,Charlotte Adams,Consumer,Glasgow,2024-07-02,Mobile + TV,108,Active,447700900085
CUST-20086,Jack Scott,SMB,Leicester,2022-12-28,Volt Bundle,56,Active,447700900086
CUST-20087,Joshua Patel,Consumer,Liverpool,2018-07-10,Business Broadband,65,Active,447700900087
CUST-20088,Henry Hernandez,Consumer,Sheffield,2020-08-31,TV + Broadband,103,Inactive,447700900088
CUST-20089,Amelia Rogers,SMB,Liverpool,2019-10-31,Business Broadband,16,Active,447700900089
CUST-20090,Layla Carter,Consumer,Glasgow,2019-07-08,Mobile + TV,14,Inactive,447700900090
CUST-20091,Victoria Williams,Consumer,Leeds,2019-03-28,Business Broadband,8,Active,447700900091
CUST-20092,Ella Moore,Consumer,Manchester,2023-04-30,Mobile Only,65,Active,447700900092
CUST-20205,Chris O'Newman,Consumer,Wolverhampton,2017-07-30,TV + Broadband,67,Active,447700900113
CUST-20093,Natalie Young,Consumer,Leicester,2018-04-15,Business Broadband,110,Active,447700900093
CUST-20094,Poppy Wilson,Consumer,Bristol,2023-06-17,Mobile + TV,54,Active,447700900094
CUST-20095,Zoe Martin,Consumer,Reading,2024-01-14,Mobile Only,19,Active,447700900095
CUST-20096,Poppy Edwards,Consumer,Manchester,2023-05-08,Business Broadband,11,Active,447700900096
CUST-20097,Charlotte Evans,Consumer,Nottingham,2024-04-06,TV + Broadband,7,Inactive,447700900097
CUST-20098,Evelyn Wilson,Consumer,Glasgow,2024-02-17,Business Broadband,64,Active,447700900098
CUST-20099,Charlotte Harris,Consumer,Cardiff,2020-01-12,TV Only,109,Inactive,447700900099
CUST-20100,Natalie Green,Consumer,Reading,2023-08-24,TV + Broadband,47,Inactive,447700900100
CUST-20101,Noah Clark,SMB,Leeds,2022-03-19,TV Only,84,Active,447700900101
CUST-20102,Emily Patel,Consumer,Glasgow,2019-01-15,Broadband Only,33,Active,447700900102
CUST-20103,Henry Hall,Consumer,Leicester,2024-11-12,TV + Broadband,77,Active,447700900103
CUST-20104,Leo Davies,Consumer,Liverpool,2022-06-25,TV Only,103,Active,447700900104
CUST-20105,Michael Parker,Consumer,Sheffield,2017-03-12,Volt Bundle,43,Active,447700900105
CUST-20106,Christopher Martinez,Consumer,Leicester,2021-02-20,Broadband Only,76,Active,447700900106
CUST-20107,Charlotte Morris,Consumer,Glasgow,2024-11-18,Broadband Only,40,Active,447700900107
CUST-20108,Freddie Taylor,Consumer,Glasgow,2018-05-05,Mobile + TV,74,Inactive,447700900108
CUST-20109,Christopher Harris,Consumer,Reading,2022-06-07,TV + Broadband,98,Active,447700900109
CUST-20110,Ryan Nelson,Consumer,Manchester,2019-03-07,TV + Broadband,35,Active,447700900110
CUST-20111,Poppy Clarke,Consumer,Birmingham,2020-01-29,Volt Bundle,12,Active,447700900111
CUST-20112,Christopher Moore,Consumer,Brighton,2022-07-04,Volt Bundle,7,Active,447700900112
CUST-20113,Michael Green,Consumer,Birmingham,2017-07-30,TV + Broadband,67,Active,447700900113
CUST-20113,Michael O'Sullivan,Consumer,Wolverhampton,2017-07-30,TV + Broadband,67,Active,447700900113
CUST-20114,Ava King,Consumer,Leicester,2024-01-23,Mobile + TV,12,Active,447700900114
CUST-20115,Joseph Lewis,Consumer,Leeds,2018-05-01,TV Only,103,Active,447700900115
CUST-20116,David Phillips,Consumer,Nottingham,2021-04-08,Broadband Only,62,Active,447700900116
CUST-20117,Elizabeth Lopez,Consumer,Leicester,2017-09-04,TV Only,100,Active,447700900117
CUST-20118,Ryan Thompson,Consumer,Bristol,2024-05-29,Volt Bundle,26,Active,447700900118
CUST-20119,Abigail Johnson,Consumer,Liverpool,2022-01-20,Mobile + TV,82,Active,447700900119
CUST-20120,Sophia Garcia,Consumer,Bristol,2024-11-19,Business Broadband,64,Active,447700900120
CUST-20121,Freddie Robinson,Consumer,Cardiff,2023-08-13,Mobile + TV,108,Inactive,447700900121
CUST-20122,Charlotte Taylor,Consumer,Cardiff,2018-09-03,TV + Broadband,24,Active,447700900122
CUST-20123,Jack Lewis,Consumer,Leicester,2020-03-28,Broadband Only,21,Active,447700900123
CUST-20124,Poppy Collins,Consumer,Bristol,2022-08-12,TV Only,69,Active,447700900124
CUST-20125,David Williams,SMB,Reading,2020-08-13,TV Only,38,Active,447700900125
CUST-20126,Freddie Edwards,Consumer,Leicester,2023-08-02,Volt Bundle,103,Active,447700900126
CUST-20127,Amelia Perez,Consumer,Brighton,2018-12-19,Broadband Only,72,Active,447700900127
CUST-20128,Amelia Harris,SMB,Liverpool,2024-02-14,Business Broadband,68,Inactive,447700900128
CUST-20129,Michael Allen,Consumer,Glasgow,2024-07-07,Volt Bundle,26,Active,447700900129
CUST-20130,Christopher Adams,Consumer,Liverpool,2023-03-04,Volt Bundle,64,Active,447700900130
CUST-20131,Henry Walker,Consumer,Brighton,2021-07-14,Business Broadband,71,Inactive,447700900131
CUST-20132,Emma Evans,SMB,Sheffield,2021-08-20,Volt Bundle,30,Active,447700900132
CUST-20133,Sofia Rogers,Consumer,Sheffield,2017-07-31,Mobile Only,40,Active,447700900133
CUST-20134,Oscar Hill,SMB,Sheffield,2018-05-13,Volt Bundle,86,Active,447700900134
CUST-20135,Ella Stewart,Consumer,Nottingham,2017-02-26,TV Only,58,Active,447700900135
CUST-20136,George Scott,SMB,Cardiff,2018-09-23,Broadband Only,97,Active,447700900136
CUST-20137,Zoe Clark,Consumer,Sheffield,2022-04-19,Mobile Only,64,Active,447700900137
CUST-20138,Mason Martin,SMB,Nottingham,2018-07-14,Business Broadband,14,Active,447700900138
CUST-20139,Logan Hall,SMB,Nottingham,2019-12-31,Business Broadband,6,Active,447700900139
CUST-20140,Poppy Roberts,Consumer,Cardiff,2022-06-29,Business Broadband,25,Active,447700900140
CUST-20141,Michael Allen,Consumer,Brighton,2023-02-04,Broadband Only,64,Inactive,447700900141
CUST-20142,Leo Collins,Consumer,Liverpool,2019-08-15,Business Broadband,105,Active,447700900142
CUST-20143,Ethan Morris,Consumer,Brighton,2021-04-11,Broadband Only,90,Inactive,447700900143
CUST-20144,Victoria Jackson,Consumer,London,2018-06-02,TV Only,81,Active,447700900144
CUST-20145,Isla Hill,Consumer,Sheffield,2017-03-04,Mobile + TV,24,Active,447700900145
CUST-20146,Victoria Jackson,Consumer,Brighton,2019-12-22,TV + Broadband,85,Active,447700900146
CUST-20147,Victoria Davies,SMB,Cardiff,2022-12-26,Broadband Only,46,Active,447700900147
CUST-20148,Ryan Adams,SMB,London,2023-12-05,Volt Bundle,36,Active,447700900148
CUST-20149,Oscar Garcia,Consumer,Liverpool,2018-02-08,Business Broadband,87,Active,447700900149
CUST-20150,Isla Hill,Consumer,Bristol,2017-04-29,Volt Bundle,47,Inactive,447700900150
CUST-20151,Oscar Allen,Consumer,Birmingham,2019-09-28,TV Only,58,Active,447700900151
CUST-20152,Grace White,Consumer,Leicester,2021-04-16,TV Only,93,Active,447700900152
CUST-20153,Elizabeth Jackson,Consumer,Cardiff,2019-11-07,Broadband Only,38,Active,447700900153
CUST-20154,Amelia Rodriguez,Consumer,Birmingham,2017-10-30,Broadband Only,50,Inactive,447700900154
CUST-20155,Poppy Cook,SMB,Reading,2019-10-22,Broadband Only,44,Active,447700900155
CUST-20156,Mason Green,Consumer,Liverpool,2023-06-01,TV + Broadband,79,Active,447700900156
CUST-20157,Christopher Rodriguez,Consumer,Cardiff,2021-06-10,TV + Broadband,7,Active,447700900157
CUST-20158,Hannah Reed,Consumer,London,2023-10-20,Mobile + TV,69,Inactive,447700900158
CUST-20159,Oscar Reed,Consumer,Leicester,2020-12-14,Mobile Only,87,Active,447700900159
CUST-20160,Henry Edwards,Consumer,Brighton,2024-05-24,Mobile + TV,23,Active,447700900160
CUST-20161,Aaron Parker,Consumer,Brighton,2021-12-11,Volt Bundle,80,Active,447700900161
CUST-20162,Harry Davies,SMB,Glasgow,2021-08-29,Mobile Only,31,Active,447700900162
CUST-20163,Matthew Young,Consumer,Bristol,2018-11-05,TV + Broadband,67,Inactive,447700900163
CUST-20164,Oscar Morris,SMB,Brighton,2018-04-17,Broadband Only,15,Active,447700900164
CUST-20165,Freddie Edwards,Consumer,Liverpool,2023-04-02,TV + Broadband,17,Inactive,447700900165
CUST-20166,Emma Robinson,Consumer,Sheffield,2021-02-18,Mobile + TV,101,Active,447700900166
CUST-20167,Elizabeth Hernandez,Consumer,Glasgow,2018-03-20,Mobile + TV,35,Active,447700900167
CUST-20205,Daniel Foster,SMB,Blackpool,2020-06-30,Broadband Only,58,Active,447700900205
CUST-20168,Sofia Mitchell,Consumer,Leicester,2019-06-26,Mobile + TV,14,Active,447700900168
CUST-20169,Amelia Collins,Consumer,Liverpool,2018-04-23,Mobile Only,11,Inactive,447700900169
CUST-20170,Poppy Adams,Consumer,Leeds,2023-01-11,Mobile Only,55,Active,447700900170
CUST-20171,Joshua Morris,Consumer,Nottingham,2021-09-13,TV Only,101,Active,447700900171
CUST-20172,Logan Parker,Consumer,Sheffield,2023-11-27,Broadband Only,41,Active,447700900172
CUST-20173,Isabella Thompson,Consumer,Leeds,2021-01-25,Volt Bundle,93,Active,447700900173
CUST-20174,Victoria Allen,Consumer,Bristol,2019-02-17,Volt Bundle,64,Active,447700900174
CUST-20175,Lily Parker,Consumer,London,2017-07-27,Business Broadband,48,Active,447700900175
CUST-20176,Harry Perez,Consumer,Brighton,2023-03-21,Mobile Only,81,Active,447700900176
CUST-20177,Freddie Hall,Consumer,Brighton,2023-09-08,Volt Bundle,41,Inactive,447700900177
CUST-20178,Mia Moore,Consumer,Brighton,2018-12-16,Volt Bundle,90,Inactive,447700900178
CUST-20179,Harry Clarke,Consumer,Brighton,2019-09-02,TV Only,47,Active,447700900179
CUST-20180,Henry Brown,Consumer,Liverpool,2022-11-25,Volt Bundle,101,Active,447700900180
CUST-20181,Jacob Reed,Consumer,Leicester,2018-03-23,Broadband Only,70,Active,447700900181
CUST-20182,Sofia Williams,Consumer,Cardiff,2022-11-06,TV + Broadband,64,Active,447700900182
CUST-20183,James Brown,SMB,Liverpool,2021-10-13,Mobile + TV,19,Active,447700900183
CUST-20184,Jacob Johnson,SMB,Glasgow,2023-10-28,Mobile Only,14,Active,447700900184
CUST-20185,Sofia Cook,Consumer,Reading,2020-08-24,Broadband Only,82,Active,447700900185
CUST-20186,Amelia Baker,Consumer,Manchester,2024-11-14,Volt Bundle,89,Active,447700900186
CUST-20187,Natalie Mitchell,Consumer,Leeds,2021-10-28,Broadband Only,35,Active,447700900187
CUST-20188,Amelia King,Consumer,Manchester,2020-07-04,Broadband Only,46,Active,447700900188
CUST-20189,Isabella Jackson,Consumer,Sheffield,2017-10-02,Volt Bundle,16,Active,447700900189
CUST-20190,Isla Morris,Consumer,Brighton,2018-06-17,TV Only,13,Active,447700900190
CUST-20191,Abigail Mitchell,Consumer,Manchester,2021-08-10,TV + Broadband,91,Inactive,447700900191
CUST-20192,Charlotte Sanchez,Consumer,Bristol,2023-09-26,TV + Broadband,51,Active,447700900192
CUST-20193,Daniel Thompson,Consumer,Sheffield,2019-07-08,Business Broadband,19,Active,447700900193
CUST-20194,Abigail Young,Consumer,Bristol,2023-06-10,Mobile Only,109,Active,447700900194
CUST-20195,Abigail Reed,Consumer,Leicester,2024-07-27,Mobile + TV,77,Active,447700900195
CUST-20196,Joshua Collins,Consumer,Birmingham,2020-01-25,Mobile + TV,103,Active,447700900196
CUST-20197,Emily Allen,Consumer,Birmingham,2023-05-09,Mobile + TV,57,Active,447700900197
CUST-20198,Layla Cook,SMB,Manchester,2022-12-13,Mobile Only,54,Active,447700900198
CUST-20199,Emily White,Consumer,Reading,2020-08-21,Business Broadband,78,Active,447700900199
CUST-20200,Oliver Jackson,Consumer,Leicester,2017-07-23,Mobile + TV,16,Active,447700900200
CUST-20204,Chloe Dawson,Consumer,Blackpool,2023-02-18,TV + Broadband,21,Active,447700900204
CUST-20204,Bukayo Saka,Consumer,London,2023-02-18,TV + Broadband,24,Active,447700900204
```
### Simpe Solution
```python
import csv

with open("vmo2-customers.csv", "r", encoding="utf-8") as f:
    customer_list = list(csv.DictReader(f))


def find_customers(customers, region):
    targeted_customers = []
    for customer in customers:
        if customer["region"] == region and customer["customer_status"] == "Active":
            targeted_customers.append(customer)
    return targeted_customers


contact_list = find_customers(customer_list,  "Blackpool")

print(contact_list)
```


### Extended Solution
```python
import csv

with open("vmo2-customers.csv", encoding="utf-8") as f:
    customer_list = list(csv.DictReader(f))

# Define region as *args to potentially recieve multiple values
def find_customers(customers, *region):
    # Define empty list
    targeted_customers = []
    # Loop through each data entry
    for customer in customers:
        # NEW SYNTAX
        # If the value held on customer key of region is found in 'region' args tuple resolve as true
        # As well as customer having an active status
        if customer["region"] in region and customer["customer_status"] == "Active":
            # Create new object for found customer to clean data
            user = {
                "customer_id": customer["customer_id"],
                "name": customer["customer_name"],
                "location": customer["region"],
                "contact_number": customer["contact_number"]
            }
            # Append to list
            targeted_customers.append(user)
    # Return list of all customers found after loop        
    return targeted_customers

# Multiple arguments passed in on region *args
# Save returned list to variable called contact list
contact_list = find_customers(customer_list, "London", "Manchester", "Birmingham", "Brighton")

# Print initial message to display amount of customers needed to be contacted
print(f"There are {len(contact_list)} members to contact:")

# For each customer, print their data on a fresh line
for customer in contact_list:
    print(f"{customer["customer_id"]} - {customer["name"]}, {customer["contact_number"]} ({customer["location"]})")
```

## Packages and imports

```txt
.
├── main.py
└── network_tools
    ├── reboot.py
    └── monitor.py
```

**reboot.py**
```python
import random

def reboot_device(device):
    """
    Simulates rebooting a customer device.
    """
    print(f"Rebooting {device}...")
    number = random.randint(0, 10)
    if number > 2:
        print(f"{device} successfully rebooted.")
        return True
    else:
        print(f"{device} failed to reboot")
        return False
```

**monitor.py**
```python
import time

def test_connection(device):
    """
    Simulates testing connection to device.
    """
    print("Connecting...")
    time.sleep(1)

    print("Connecting...")
    time.sleep(1)

    print("Connecting...")
    time.sleep(1)

    print(f"Running connection test for {device}... Connection OK.")
```

**main.py**
```python
from network_tools.reboot import reboot_device
from network_tools.monitor import test_connection

reboot_succeeded = reboot_device("Router")

if reboot_succeeded == True:
    test_connection("Router")
```

## OOP

```python
class Customer:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed

    def describe(self): 
        return f"{self.name} has {self.speed} Mbps broadband."

emile_customer = Customer("Emile", 500)
print(emile_customer.describe())
```
