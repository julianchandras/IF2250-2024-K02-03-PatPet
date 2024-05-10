from models.baseModel import BaseModel

class ActivityModel(BaseModel):
    def __init__(self, db_name):
        super().__init__(db_name)  # Call the BaseModel constructor
        self.create_tables()  # Ensure tables are created

    def create_tables(self):
        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS activity (
                activity_id INTEGER PRIMARY KEY AUTOINCREMENT,
                activity_name TEXT,
                start_date DATE,
                end_date DATE,
                start_time TIME,
                end_time TIME,
                pet_id INTEGER,
                FOREIGN KEY (pet_id) REFERENCES pets(pet_id)
            )
            """
        )

        self.commit()  # Commit table creatio

    def get_all_activities(self):
        self.cursor.execute("SELECT * FROM activity")
        rows = self.cursor.fetchall()  # Use self.cursor
        return rows

    def add_activity(self, activity_name, start_date, end_date,start_time,end_time, pet_id):
        self.cursor.execute(
            "INSERT INTO activity (activity_name, start_date, end_date, start_time, end_time, pet_id) VALUES (?, ?, ?, ?, ?, ?)",
            (activity_name, start_date, end_date,start_time,end_time, pet_id),

        )
        self.commit()  # Commit after insertion

    def delete_activity(self, activity_id):
        self.cursor.execute("DELETE FROM activity WHERE activity_id = ?", (activity_id,))
        self.commit()  # Commit after deletion

    def update_activity(self, activity_id, activity_name, start_date, end_date,start_time,end_time, pet_id):
        self.cursor.execute(
            "UPDATE activity SET activity_name = ?, start_date = ?, end_date = ?, start_time = ?, end_time = ? , pet_id = ? WHERE activity_id = ?",
            (activity_name, start_date, end_date, start_time, end_time, pet_id, activity_id),
        )
        self.commit()  # Commit after update

    def get_todays_activity(self):
        self.cursor.execute("SELECT * FROM activity WHERE start_date = DATE('now')")
        rows = self.cursor.fetchall()
        return rows
    
