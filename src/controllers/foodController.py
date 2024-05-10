from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QStackedWidget
from PyQt5.QtWidgets import QMessageBox
from models.foodModel import FoodModel  # Import the PetModel
from boundaries.foodViews.mainFoodView import MainFoodView  # Import the MainFoodView

class FoodController:
    def __init__(self, stacked_widget : QStackedWidget, food_model : FoodModel):
        self.stacked_widget = stacked_widget
        self.model = food_model

        self.view : MainFoodView = self.stacked_widget.widget(6)  # Main food view index 6
    
        # Load all pets initially
        self.load_foods()

    def load_foods(self):
        # Get all foods from the model and set them in the view
        foods = self.model.get_all_food()
        self.view.set_food(foods)

    def add_food(self, food_name):
        self.model.add_food(food_name)
        self.load_foods()  # Refresh the view after adding

    def update_food(self, food_id, food_name):
        self.model.update_food(food_id, food_name)
        self.load_foods()

    def delete_food(self, food_id):
        self.model.delete_food(food_id)
        self.load_foods()


    
