import os
import sys
import pytest
root_dir = os.path.abspath(os.path.join(os.getcwd()))
sys.path.append(root_dir + '/src')
from datetime import date, timedelta
from src.models.foodModel import FoodModel
from src.models.petModel import PetModel

class TestActivityModel:
    @pytest.fixture
    def pet_model(self):
        # Assuming 'test.db' is a test database
        model = PetModel('database/test.db')
        foodmodel = FoodModel('database/test.db')
        
        yield model

        model.cursor.execute("DROP TABLE pet_food")
        model.cursor.execute("DROP TABLE foods")
        model.cursor.execute("DROP TABLE pets")
        model.commit()
        model.close()

    def test_add_pet(self, pet_model: PetModel):
        dummyImageData = open('img/meng.png', 'rb').read()
        pet_model.add_pet('Sumito', 'Babi', 18, 'Sehat', dummyImageData)
        pet_model.add_pet('Neo', 'Anjing', 18, 'Kanker telinga kanan', dummyImageData)

        rows = pet_model.get_all_pets()
        
        assert len(rows) == 2
        assert rows[0][1] == 'Sumito'
        assert rows[1][2] == 'Anjing'
        assert rows[0][3] == 18
        assert rows[1][4] == 'Kanker telinga kanan'

    def test_get_all_pets(self, pet_model: PetModel):
        dummyImageData = open('img/meng.png', 'rb').read()
        pet_model.add_pet('Quandale', 'Flamingo', 18, 'Sehat', dummyImageData)
        pet_model.add_pet('Dingle', 'Flamingo', 18, 'Kanker paruh', dummyImageData)
        pet_model.add_pet('Sucipto', 'Hiu', 5, 'Kanker paru paru', dummyImageData)
        pet_model.add_pet('Mulyono', 'Kucing', 3, 'Autisme kucing', dummyImageData) 

        rows = pet_model.get_all_pets()
        
        assert len(rows) == 4
        assert rows[0][1] == 'Quandale'
        assert rows[1][2] == 'Flamingo'
        assert rows[2][3] == 5
        assert rows[3][4] == 'Autisme kucing'

    def test_delete_pet(self, pet_model: PetModel):
        dummyImageData = open('img/meng.png', 'rb').read()
        pet_model.add_pet('Quandale', 'Flamingo', 18, 'Sehat', dummyImageData)
        pet_model.add_pet('Dingle', 'Flamingo', 18, 'Kanker paruh', dummyImageData)
        pet_model.add_pet('Sucipto', 'Hiu', 5, 'Kanker paru paru', dummyImageData)
        pet_model.add_pet('Mulyono', 'Kucing', 3, 'Autisme kucing', dummyImageData) 
        pet_model.delete_pet(1)

        rows = pet_model.get_all_pets()
        
        assert len(rows) == 3
        assert rows[0][1] == 'Dingle'
        assert rows[1][2] == 'Hiu'
        assert rows[2][3] == 3
        
    def test_update_pet(self, pet_model: PetModel):
        dummyImageData = open('img/meng.png', 'rb').read()
        pet_model.add_pet('Quandale', 'Flamingo', 18, 'Sehat', dummyImageData)
        pet_model.add_pet('Dingle', 'Flamingo', 18, 'Kanker paruh', dummyImageData)
        pet_model.add_pet('Sucipto', 'Hiu', 5, 'Kanker paru paru', dummyImageData)
        pet_model.update_pet(1, 'Turkish', 'Flamingo', 18, 'Schizophrenia flamingo akut', dummyImageData, food_list=[]) 
        rows = pet_model.get_all_pets()
        
        assert len(rows) == 3
        assert rows[0][1] == 'Turkish'
        assert rows[1][2] == 'Flamingo'
        assert rows[0][4] == 'Schizophrenia flamingo akut'

    def test_get_specific_pet(self, pet_model: PetModel):
        dummyImageData = open('img/meng.png', 'rb').read()
        pet_model.add_pet('Quandale', 'Flamingo', 18, 'Sehat', dummyImageData)
        pet_model.add_pet('Dingle', 'Flamingo', 18, 'Kanker paruh', dummyImageData)
        pet_model.add_pet('Sucipto', 'Hiu', 5, 'Kanker paru paru', dummyImageData)

        specific_pet_row = pet_model.get_specific_pet(3)

        assert specific_pet_row[0] == 3
        assert specific_pet_row[1] == 'Sucipto'
        assert specific_pet_row[2] == 'Hiu'
        assert specific_pet_row[3] == 5
        assert specific_pet_row[4] == 'Kanker paru paru'
