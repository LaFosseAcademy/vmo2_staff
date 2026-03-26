PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS packages (
    package_id INTEGER PRIMARY KEY,
    package_name TEXT NOT NULL,
    price REAL NOT NULL,
    contract_length INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS customers (
    customer_id INTEGER PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT NOT NULL,
    phone TEXT NOT NULL, 
    package_id INTEGER NOT NULL,
    FOREIGN KEY(package_id) REFERENCES packages(package_id)
);


