from db.db import connect, run_sql_file
from classes.package import Package

connection = connect("app.db")
run_sql_file(connection, "./db/schema.sql")
run_sql_file(connection, "./db/seed.sql")

packages = Package.get_all(connection)
print(packages)

connection.close()
