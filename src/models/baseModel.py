import sqlite3

class BaseModel:
    def __init__(self, db_name):
        self.db_name = db_name
        self.connection = sqlite3.connect(db_name)  # Establish connection to the database
        self.connection.execute("PRAGMA foreign_keys = 1")  # Enable foreign key constraints
        self.cursor = self.connection.cursor()
    
    def commit(self):
        self.connection.commit()
    
    def close(self):
        self.connection.close()