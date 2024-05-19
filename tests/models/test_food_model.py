import os
import sys
import pytest

root_dir = os.path.abspath(os.path.join(os.getcwd()))
sys.path.append(root_dir + '/src')

from src.models.foodModel import FoodModel
from src.models.petModel import PetModel

class TestFoodModel:
    @pytest.fixture
    def food_model(self):
        # Assuming 'test.db' is a test database
        model = FoodModel('database/test.db')
        PetModel('database/test.db')

        yield model
        model.cursor.execute("DROP TABLE pet_food")
        model.cursor.execute("DROP TABLE foods")
        model.cursor.execute("DROP TABLE pets")
        model.commit()
        model.close()

    def test_add_food(self, food_model: FoodModel):
        food_model.add_food('Kibble')
        food_model.add_food('Wet Food')
        
        rows = food_model.get_all_food()
        
        assert len(rows) == 2
        assert rows[0][0] == 'Kibble'
        assert rows[1][0] == 'Wet Food'

    def test_get_all_food(self, food_model: FoodModel):
        food_model.add_food('Kibble')
        food_model.add_food('Wet Food')
        food_model.add_food('Treats')
        
        rows = food_model.get_all_food()
        
        assert len(rows) == 3
        assert rows[0][0] == 'Kibble'
        assert rows[1][0] == 'Wet Food'
        assert rows[2][0] == 'Treats'

    def test_delete_food(self, food_model: FoodModel):
        food_model.add_food('Kibble')
        food_model.add_food('Wet Food')
        food_model.add_food('Treats')
        food_model.delete_food(2)
        
        rows = food_model.get_all_food()
        
        assert len(rows) == 2
        assert rows[0][0] == 'Kibble'
        assert rows[1][0] == 'Treats'

    def test_update_food(self, food_model: FoodModel):
        food_model.add_food('Kibble')
        food_model.add_food('Wet Food')
        food_model.update_food(1, 'Dry Kibble')
        
        rows = food_model.get_all_food()
        
        assert len(rows) == 2
        assert rows[0][0] == 'Dry Kibble'
        assert rows[1][0] == 'Wet Food'

    def test_get_food_eater(self, food_model: FoodModel):
        # Assuming the PetModel and FoodModel are working together
        # and pets have been added with respective foods
        
        food_model.add_food('Kibble')
        food_model.add_food('Wet Food')

        # Provide a dummy image for the pet
        dummyImageData = open('img/meng.png', 'rb').read()
        
        food_model.cursor.execute(
            "INSERT INTO pets (pet_name, species, age, medical_record, image) VALUES (?, ?, ?, ?, ?)",
            ('Fido', 'Dog', 3, 'Healthy', dummyImageData)
        )
        food_model.commit()
        
        pet_id = food_model.cursor.lastrowid
        food_model.add_pet_food(pet_id, 1)
        
        food_eater = food_model.get_food_eater()
        
        assert 'Kibble' in food_eater
        assert 'Fido' in food_eater['Kibble'][1]

    def test_filter_pet_by_food(self, food_model: FoodModel):
        # Assuming the PetModel and FoodModel are working together
        # and pets have been added with respective foods
        
        food_model.add_food('Kibble')
        food_model.add_food('Wet Food')

        # Provide a dummy image for the pet
        dummyImageData = open('img/meng.png', 'rb').read()
        
        food_model.cursor.execute(
            "INSERT INTO pets (pet_name, species, age, medical_record, image) VALUES (?, ?, ?, ?, ?)",
            ('Fido', 'Dog', 3, 'Healthy', dummyImageData)
        )
        food_model.commit()
        
        pet_id = food_model.cursor.lastrowid
        food_model.add_pet_food(pet_id, 1)
        
        pets = food_model.filter_pet_by_food([1])
        
        assert len(pets) == 1
        assert pets[0][1] == 'Fido'

    def test_add_pet_food(self, food_model: FoodModel):
        # Assuming the PetModel and FoodModel are working together
        # and pets have been added
        
        food_model.add_food('Kibble')

        # Provide a dummy image for the pet
        dummyImageData = open('img/meng.png', 'rb').read()
        
        food_model.cursor.execute(
            "INSERT INTO pets (pet_name, species, age, medical_record, image) VALUES (?, ?, ?, ?, ?)",
            ('Fido', 'Dog', 3, 'Healthy', dummyImageData)
        )
        food_model.commit()
        
        pet_id = food_model.cursor.lastrowid
        food_model.add_pet_food(pet_id, 1)
        
        pet_foods = food_model.get_pet_foods(pet_id)
        
        assert 'Kibble' in pet_foods

    def test_update_pet_food(self, food_model: FoodModel):
        # Assuming the PetModel and FoodModel are working together
        # and pets have been added
        
        food_model.add_food('Kibble')
        food_model.add_food('Wet Food')

        # Provide a dummy image for the pet
        dummyImageData = open('img/meng.png', 'rb').read()
        
        food_model.cursor.execute(
            "INSERT INTO pets (pet_name, species, age, medical_record, image) VALUES (?, ?, ?, ?, ?)",
            ('Fido', 'Dog', 3, 'Healthy', dummyImageData)
        )
        food_model.commit()
        
        pet_id = food_model.cursor.lastrowid
        food_model.add_pet_food(pet_id, 1)
        
        food_model.update_pet_food(pet_id, [2])
        
        pet_foods = food_model.get_pet_foods(pet_id)
        
        assert 'Wet Food' in pet_foods
        assert 'Kibble' not in pet_foods
