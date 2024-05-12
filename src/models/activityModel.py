from models.baseModel import BaseModel
from datetime import date


class ActivityModel(BaseModel):
    def __init__(self, db_name):
        super().__init__(db_name)  # Call the BaseModel constructor
        self.create_tables()  # Ensure tables are created

    def create_tables(self):
        try:
            self.cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS activity (
                    activity_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    activity_name TEXT,
                    activity_date DATE,
                    start_time TIME,
                    end_time TIME,
                    pet_id INTEGER,
                    FOREIGN KEY (pet_id) REFERENCES pets(pet_id) ON DELETE CASCADE
                )

                """

            )
            
            self.commit()  # Commit table creation
        except Exception as e:
            print("Error creating tables:", e)

    def get_all_activities(self):
        try:
            self.cursor.execute("SELECT activity_id,activity_name,activity_date,start_time,end_time,pet_id,pet_name,species FROM activity NATURAL JOIN pets")
            rows = self.cursor.fetchall()
           
            return rows
        
        except Exception as e:
            print("Error fetching activities:", e)
            return []

    def add_activity(self, activity_name, activity_date, start_time, end_time, pet_id):
        try:
            self.cursor.execute(
                "INSERT INTO activity (activity_name, activity_date, start_time, end_time, pet_id) VALUES (?, ?, ?, ?, ?)",
                (activity_name, activity_date,  start_time, end_time, pet_id),
            )
            self.commit()
        except Exception as e:
            print("Error adding activity:", e)

    def delete_activity(self, activity_id):
        try:
            self.cursor.execute("DELETE FROM activity WHERE activity_id = ?", (activity_id,))
            self.commit()
        except Exception as e:
            print("Error deleting activity:", e)

    def update_activity(self, activity_id, activity_name, activity_date, start_time, end_time, pet_id):
        try:
            self.cursor.execute(
                "UPDATE activity SET activity_name = ?,  activity_date = ?, start_time = ?, end_time = ?, pet_id = ? WHERE activity_id = ?",
                (activity_name,activity_date, start_time, end_time, pet_id, activity_id),
            )
            self.commit()
        except Exception as e:
            print("Error updating activity:", e)

    def get_todays_activity(self):
        try:
            today = date.today()
            self.cursor.execute("SELECT activity_id,activity_name,activity_date,start_time,end_time,pet_id,pet_name,species FROM activity NATURAL JOIN pets WHERE activity_date = ?", (today,))
            rows = self.cursor.fetchall()
            return rows
        except Exception as e:
            print("Error fetching today's activities:", e)
            return []
