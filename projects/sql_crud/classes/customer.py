from classes.package import Package


class Customer:
    def __init__(self, customer_id, first_name, last_name, email, phone, package):
        self.customer_id = customer_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.package = package

    def __repr__(self):
        return (
            f"Customer({self.customer_id}, {self.first_name}, {self.last_name}, "
            f"{self.email}, {self.phone}, {self.package})"
        )

    @staticmethod
    def get_all(conn):
        cursor = conn.cursor()
        cursor.execute(
            """
            SELECT 
                c.customer_id,
                c.first_name,
                c.last_name,
                c.email,
                c.phone,
                p.package_id,
                p.package_name,
                p.price,
                p.contract_length
            FROM customers c
            JOIN packages p
                ON c.package_id = p.package_id
            """
        )

        rows = cursor.fetchall()
        customers = []

        for row in rows:
            package = Package(row[5], row[6], row[7], row[8])
            customer = Customer(row[0], row[1], row[2], row[3], row[4], package)
            customers.append(customer)

        return customers

    @staticmethod
    def get_one(conn, customer_id):
        cursor = conn.cursor()
        cursor.execute(
            """
            SELECT 
                c.customer_id,
                c.first_name,
                c.last_name,
                c.email,
                c.phone,
                p.package_id,
                p.package_name,
                p.price,
                p.contract_length
            FROM customers c
            JOIN packages p
                ON c.package_id = p.package_id
            WHERE c.customer_id = ?
            """,
            (customer_id,)
        )

        row = cursor.fetchone()

        if row:
            package = Package(row[5], row[6], row[7], row[8])
            return Customer(row[0], row[1], row[2], row[3], row[4], package)

    @staticmethod
    def get_one_by_email(conn, email: str):
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM customers WHERE email = ?", (email,))
        row = cursor.fetchone()

        if row:
            return True
        else:
            return False

    @staticmethod
    def create(conn, first_name: str, last_name: str, email: str, phone: str, package_id: int):
        email_exists = Customer.get_one_by_email(conn, email)

        if email_exists == False:
            cursor = conn.cursor()
            cursor.execute(
                """
                INSERT INTO customers (first_name, last_name, email, phone, package_id)
                VALUES (?, ?, ?, ?, ?)
                RETURNING customer_id, first_name, last_name, email, phone, package_id
                """,
                (first_name, last_name, email, phone, package_id)
            )

            row = cursor.fetchone()
            conn.commit()

            if row:
                package = Package.get_one(conn, row[5])
                return Customer(row[0], row[1], row[2], row[3], row[4], package)
        else:
            return "Data entry with same email already exists"

    def update(self, conn, customer_updates: dict):
        first_name = self.first_name
        last_name = self.last_name
        email = self.email
        phone = self.phone
        package_id = self.package.package_id

        if "first_name" in customer_updates and customer_updates["first_name"] is not None:
            first_name = customer_updates["first_name"]

        if "last_name" in customer_updates and customer_updates["last_name"] is not None:
            last_name = customer_updates["last_name"]

        if "email" in customer_updates and customer_updates["email"] is not None:
            email = customer_updates["email"]

        if "phone" in customer_updates and customer_updates["phone"] is not None:
            phone = customer_updates["phone"]

        if "package_id" in customer_updates and customer_updates["package_id"] is not None:
            package_id = customer_updates["package_id"]

        cursor = conn.cursor()
        cursor.execute(
            """
            UPDATE customers
            SET first_name = ?, last_name = ?, email = ?, phone = ?, package_id = ?
            WHERE customer_id = ?
            RETURNING customer_id, first_name, last_name, email, phone, package_id
            """,
            (first_name, last_name, email, phone, package_id, self.customer_id)
        )

        row = cursor.fetchone()
        conn.commit()

        if row:
            package = Package.get_one(conn, row[5])
            return Customer(row[0], row[1], row[2], row[3], row[4], package)

    def destroy(self, conn):
        cursor = conn.cursor()
        cursor.execute("DELETE FROM customers WHERE customer_id = ?", (self.customer_id,))
        conn.commit()
        print("Data deleted")
