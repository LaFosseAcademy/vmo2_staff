class Antenna:
    def __init__(self, antenna_id, site_name, borough, local_area, postcode, latitude, longitude, install_date, technology_mix, antenna_type, height_m, owner, backhaul_type):
        self.antenna_id = antenna_id
        self.site_name = site_name
        self.borough = borough
        self.local_area = local_area
        self.postcode = postcode
        self.latitude = latitude
        self.longitude = longitude
        self.install_date = install_date
        self.technology_mix = technology_mix
        self.antenna_type = antenna_type
        self.height_m = height_m
        self.owner = owner
        self.backhaul_type = backhaul_type
        
    def __repr__(self):
        return f"Antenna: {self.antenna_id}, {self.site_name}, {self.borough}, {self.local_area} longitude: {self.longitude}, latitude: {self.latitude}"
        
    @staticmethod    
    def get_one(conn, antenna_id):        
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM antenna WHERE antenna_id = ?", (antenna_id,))      
        row = cursor.fetchone()

        if row is None:
            return None

        return Antenna(*row)
