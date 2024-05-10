from models.baseModel import BaseModel

class PetModel(BaseModel):
    def __init__(self, db_name):
        super().__init__(db_name)  # Call the BaseModel constructor
        self.create_tables()  # Ensure tables are created

    ## Untuk ngebuat tabel
    def create_tables(self):
        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS pets (
                pet_id INTEGER PRIMARY KEY AUTOINCREMENT,
                pet_name TEXT NOT NULL,
                species TEXT NOT NULL,
                age INTEGER NOT NULL,
                medical_record TEXT NOT NULL,
                image BLOB NOT NULL
            )
            """
        )
        self.commit()  # Commit table creation

    ## Simply return semua
    def get_all_pets(self):
        self.cursor.execute("SELECT * FROM pets")
        rows = self.cursor.fetchall()  # Use self.cursor
        return rows


    ## Nambahin pet, image dalam BYTE
    def add_pet(self, pet_name, species, age, medical_record, image=None):
        self.cursor.execute(
            "INSERT INTO pets (pet_name, species, age, medical_record, image) VALUES (?, ?, ?, ?, ?)",
            (pet_name, species, age, medical_record, image),  # Corrected parameter names
        )
        self.commit()  # Commit after insertion

    ## Delete pet
    def delete_pet(self, pet_id):
        self.cursor.execute("DELETE FROM pets WHERE pet_id = ?", (str(pet_id),))  # Corrected parameter
        self.commit()  # Commit after deletion

    ## Update pet , inget param harus dipake semua walaupun yang berubah cuma 1
    def update_pet(self, pet_id, pet_name, species, age, medical_record, image=None):
        self.cursor.execute(
            "UPDATE pets SET pet_name = ?, species = ?, age = ?, medical_record = ?, image = ? WHERE pet_id = ?",
            (pet_name, species, age, medical_record, image, pet_id),  # Corrected parameter names
        )
        self.commit()  # Commit after update

    ## Get specific pet
    def get_specific_pet(self, pet_id):
        self.cursor.execute("SELECT * FROM pets WHERE pet_id = ?", (str(pet_id),))
        row = self.cursor.fetchone()
        return row

    
