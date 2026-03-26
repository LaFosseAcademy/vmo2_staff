PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS antenna (
    antenna_id TEXT PRIMARY KEY,
    site_name TEXT NOT NULL,
    borough TEXT NOT NULL,
    local_area TEXT NOT NULL,
    postcode TEXT NOT NULL,
    latitude REAL NOT NULL,
    longitude REAL NOT NULL,
    install_date TEXT NOT NULL,
    technology_mix TEXT NOT NULL,
    antenna_type TEXT NOT NULL,
    height_m REAL NOT NULL,
    owner TEXT NOT NULL,
    backhaul_type TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS record (
    record_id INTEGER PRIMARY KEY AUTOINCREMENT,
    antenna_id TEXT NOT NULL,
    report_date TEXT NOT NULL,
    last_inspection_date TEXT,
    next_maintenance_due TEXT,
    operational_status TEXT NOT NULL,
    power_state TEXT NOT NULL,
    azimuth_deg INTEGER NOT NULL,
    signal_health_score INTEGER NOT NULL,
    FOREIGN KEY (antenna_id) REFERENCES antenna(antenna_id)
);
