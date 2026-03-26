class Package:
    def __init__(self, package_id, package_name, price, contract_length):
        self.package_id = package_id
        self.package_name = package_name
        self.price = price
        self.contract_length = contract_length

    def __repr__(self):
        return f"Package({self.package_id}, {self.package_name}, £{self.price}, {self.contract_length})"

    @staticmethod
    def get_all(conn):
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM packages")
        rows = cursor.fetchall()
        packages = []
        for row in rows:
            package = Package(*row)
            packages.append(package)
        return packages

    @staticmethod
    def get_one(conn, package_id):
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM packages WHERE package_id = ?", (package_id,))
        row = cursor.fetchone()
        if row:
            return Package(*row)

    @staticmethod
    def get_one_by_name(conn, package_name):
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM packages WHERE package_name = ?", (package_name,))
        row = cursor.fetchone()
        if row:
            return True
        else: 
            return False
            
    @staticmethod
    def create(conn, package_name, price, contract_length):
        name_exists = Package.get_one_by_name(conn, package_name)
        if name_exists == False:
            cursor = conn.cursor()
            cursor.execute(
                """
                INSERT INTO packages (package_name, price, contract_length)
                VALUES (?, ?, ?) RETURNING *
                """,
                (package_name, price, contract_length)
            )
            row = cursor.fetchone()
            conn.commit()
            if row:
               return Package(*row)
        else: 
            return("Data entry with same name already exists")


    def update(self, conn, package_updates):
        package_name = self.package_name
        price = self.price
        contract_length = self.contract_length

        if package_updates["package_name"]:
            package_name = package_updates["package_name"]
        if package_updates["price"]:
            price = package_updates["price"]
        if package_updates["contract_length"]:
            contract_length = package_updates["contract_length"]



        cursor = conn.cursor()
        cursor.execute(
            """
            UPDATE packages
            SET package_name = ?, price = ?, contract_length = ?
            WHERE package_id = ?
            RETURNING *
            """, (package_name, price, contract_length, self.package_id)
        )

        row = cursor.fetchone()
        conn.commit()

        if row:
            return Package(*row)
        

    def destroy(self, conn):
        cursor = conn.cursor()
        cursor.execute("DELETE FROM packages WHERE package_id = ?", (self.package_id,))
        conn.commit()
        print("Data deleted")




