INSERT INTO packages (package_name, price, contract_length) VALUES
('Basic Plan', 19.99, 6),
('Standard Plan', 39.99, 12),
('Premium Plan', 59.99, 12),
('Volt Plan', 99.99, 24);

INSERT INTO customers (first_name, last_name, email, phone, package_id) VALUES
('Alice', 'Smith', 'alice.smith@email.com', '+44 7700 900101', 1),
('Bob', 'Johnson', 'bob.johnson@email.com', '+44 7700 900102', 2),
('Charlie', 'Brown', 'charlie.brown@email.com', '+44 7700 900103', 2),
('Diana', 'Miller', 'diana.miller@email.com', '+44 7700 900104', 3),
('Ethan', 'Davis', 'ethan.davis@email.com', '+44 7700 900105', 1),
('Fiona', 'Garcia', 'fiona.garcia@email.com', '+44 7700 900106', 4),
('George', 'Wilson', 'george.wilson@email.com', '+44 7700 900107', 3),
('Simon', 'Clemson', 'simon.clemson@email.com', '+44 7700 900108', 1),
('Sean', 'Bean', 'sean.bean@email.com', '+44 7700 900109', 4);
