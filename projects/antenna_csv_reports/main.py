from db.db import connect, run_sql_file
from db.db_utilities import today_string, add_antenna, add_record
from classes.antenna import Antenna
from classes.record import Record
from assign_job import find_closest_engineer, fetch_weather

connection = connect("app.db")
run_sql_file(connection, "./db/schema.sql")

add_antenna(connection, today_string)
add_record(connection, today_string)

records = Record.lowest_average_signal_health(connection, 1, 1)
antenna = Antenna.get_one(connection, records[0][0])


engineer = find_closest_engineer(antenna)
weather = fetch_weather(antenna)

if weather["temp_c"] >= 5 and weather["windspeed"] <= 30:
    print(f"{engineer["name"]} is the closest engineer able to work at the {antenna.site_name} in {antenna.local_area}")
