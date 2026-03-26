import sqlite3

def connect(db_name):
    connection = sqlite3.connect(db_name)
    return connection

def run_sql_file(conn, filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        sql = f.read()
    conn.executescript(sql)
    conn.commit()
