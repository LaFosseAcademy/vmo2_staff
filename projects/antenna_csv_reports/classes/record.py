class Record:
    def __init__(self, record_id, antenna_id, report_date, last_inspection_date, next_maintenance_due, operational_status, power_state, azimuth_deg, signal_health_scre):
        self.record_id = record_id
        self.antenna_id = antenna_id
        self.report_date = report_date
        self.last_inspection_date = last_inspection_date
        self.next_maintenance_due = next_maintenance_due
        self.operational_status = operational_status
        self.power_state = power_state
        self.azimuth_deg = azimuth_deg
        self.signal_health_score = self.signal_health_score


    @staticmethod
    def lowest_average_signal_health(conn, limit = None, period= None):
        cursor = conn.cursor()
        
        if limit is None:
            cursor.execute("SELECT COUNT(*) FROM antenna")
            limit = cursor.fetchone()[0]
        
        if period is None:
            cursor.execute(
                """
                SELECT antenna_id, ROUND(AVG(signal_health_score),2)
                FROM record
                GROUP BY antenna_id
                ORDER BY AVG(signal_health_score) ASC
                LIMIT ?
                """,
                (limit, )
            )
        else:
            cursor.execute(
                """
                SELECT antenna_id, ROUND(AVG(signal_health_score),2)
                FROM record
                WHERE date(report_date) >= date('now', ?)
                GROUP BY antenna_id
                ORDER BY AVG(signal_health_score) ASC
                LIMIT ?
                """,
                (f"-{period-1} days", limit)
            )
        
        return cursor.fetchall()
