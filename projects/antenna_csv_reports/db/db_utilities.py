import csv
import datetime

today = datetime.datetime.now()
today_string = today.strftime("%Y-%m-%d") 

def add_antenna(conn, date):
    with open(f"./reports/{date}_antenna_report.csv", "r", encoding="utf-8") as f:
        antennas = list(csv.DictReader(f))

    new_antennas = []
    cursor = conn.cursor()
    for antenna in antennas:
        cursor.execute("SELECT antenna_id FROM antenna WHERE antenna_id = ?", (antenna["antenna_id"],))
        row = cursor.fetchone()
        if not row:
            new_antennas.append((antenna["antenna_id"], antenna["site_name"], antenna["borough"], antenna["local_area"], antenna["postcode"], float(antenna["latitude"]), float(antenna["longitude"]), antenna["install_date"], antenna["technology_mix"], antenna["antenna_type"], float(antenna["height_m"]), antenna["owner"], antenna["backhaul_type"]))

    # NEW CODE        
    if len(new_antennas) == 0:
        print("No new Antenna location data to add")
    else:
        print("Added new Antenna location data")   
        cursor.executemany("INSERT INTO antenna (antenna_id, site_name, borough, local_area, postcode, latitude, longitude, install_date, technology_mix, antenna_type, height_m, owner, backhaul_type) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", new_antennas)
        conn.commit()
        
        
def add_record(conn, date):

    cursor = conn.cursor()   
    cursor.execute("SELECT report_date FROM record WHERE report_date = ?", (date,))
    row = cursor.fetchone()
    
    if row:
        print("Daily log already uploaded")
    else: 
        with open(f"./reports/{date}_antenna_report.csv", "r", encoding="utf-8") as f:
            daily_report = list(csv.DictReader(f))

        new_records = []
        for record in daily_report:
            new_records.append((record["antenna_id"], record["report_date"], record["last_inspection_date"], record["next_maintenance_due"], record["operational_status"], record["power_state"], record["azimuth_deg"], record["signal_health_score"]))

        cursor.executemany("INSERT INTO record (antenna_id, report_date, last_inspection_date, next_maintenance_due, operational_status, power_state, azimuth_deg, signal_health_score) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", new_records)
        print("Daily log data uploaded")
        conn.commit()
