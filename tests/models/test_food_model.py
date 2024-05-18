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

    def test

    