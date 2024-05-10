from models.baseModel import BaseModel

class FoodModel(BaseModel):
    def __init__(self, db_name):
        super().__init__(db_name)  # Call the BaseModel constructor
        self.create_tables()  # Ensure tables are created

    def create_tables(self):
        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS foods (
                food_id INTEGER PRIMARY KEY AUTOINCREMENT,
                food_name TEXT NOT NULL
            )
            """
        )

        self.commit()  # Commit table creation

        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS pet_food (
                pet_id INTEGER,
                food_id INTEGER,
                FOREIGN KEY (food_id) REFERENCES foods(food_id)
                FOREIGN KEY (pet_id) REFERENCES pets(pet_id)
                PRIMARY KEY (pet_id, food_id)
            )
            """
        )

        self.commit()  # Commit table creation

    def get_all_food(self):
        self.cursor.execute("SELECT * FROM foods")
        rows = self.cursor.fetchall()  # Use self.cursor
        return rows

    def add_food(self, food_name):
        self.cursor.execute(
            "INSERT INTO foods (food_name) VALUES (?)",
            (food_name),  # Corrected parameter names
        )
        self.commit()  # Commit after insertion

    def delete_food(self, food_id):
        self.cursor.execute("DELETE FROM foods WHERE food_id = ?", (food_id))  # Corrected parameter
        self.commit()  # Commit after deletion

    def update_food(self, food_id, food_name):
        self.cursor.execute(
            "UPDATE foods SET food_name = ? WHERE food_id = ?",
            (str(food_id),  # Corrected parameter names
        ))
        self.commit()  # Commit after update

    def filter_pet_by_food(self, food_list):
        # Check if the list is empty
        if not food_list:
            self.cursor.execute("SELECT * FROM pets")
            rows = self.cursor.fetchall()
            return  rows  # If there's nothing to filter by, return everything

        # Create placeholders based on the length of the list
        placeholders = ", ".join("?" * len(food_list))  # Resulting in a string like "?, ?, ?"

        # Construct the SQL query with the placeholders
        query = f"""
            SELECT pets.pet_name, pets.species, pets.age, pets.medical_record, pets.image
            FROM pets
            JOIN pet_food ON pets.pet_id = pet_food.pet_id
            JOIN foods ON pet_food.food_id = foods.food_id
            WHERE foods.food_name IN ({placeholders})
        """

        # Execute the query with the list of food names
        self.cursor.execute(query, tuple(food_list))  # Convert the list to a tuple for SQLite
        rows = self.cursor.fetchall()  # Fetch all matching rows
        return rows  # Return the results


    def add_pet_food(self, pet_id, food_id):
        for food in food_id:
            self.cursor.execute(
                "INSERT INTO pet_food (pet_id, food_id) VALUES (?, ?)",
                (str(pet_id), food),
            )
        self.commit()
    
    def get_pet_foods(self, pet_id):
        query = """
        SELECT foods.food_name
        FROM pet_food
        INNER JOIN pets ON pet_food.pet_id = pets.pet_id
        INNER JOIN foods ON pet_food.food_id = foods.food_id
        WHERE pets.pet_id = ?
        """
        self.cursor.execute(query, (str(pet_id),))
        rows = self.cursor.fetchall()
        return rows
