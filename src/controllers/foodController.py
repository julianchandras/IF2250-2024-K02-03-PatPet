from PyQt5.QtWidgets import QStackedWidget
from PyQt5.QtWidgets import QMessageBox
from models.foodModel import FoodModel  # Import the PetModel
from boundaries.foodViews.mainFoodView import MainFoodView  # Import the MainFoodView

class FoodController:
    def __init__(self, stacked_widget : QStackedWidget, food_model : FoodModel):
        self.stacked_widget = stacked_widget
        self.model = food_model

        self.view : MainFoodView = self.stacked_widget.widget(6)  # Main food view index 6
        self.add_hewan_view = self.stacked_widget.widget(3)  # Add hewan view index 3
        self.edit_hewan_view = self.stacked_widget.widget(4)
        
        self.view.add_food_signal.connect(self.add_food)
        self.view.update_food_signal.connect(self.update_food)
        self.view.delete_food_signal.connect(self.delete_food)
        self.view.refetch_foods_signal.connect(self.load_foods)
    
        # Load all pets initially
        self.load_foods()

    def load_foods(self):
        # Get all foods from the model and set them in the view
        foods = self.model.get_all_food()
        self.view.set_food(foods)

    def add_food(self, food_name):
        
        self.model.add_food(food_name)
        self.load_foods()  # Refresh the view after adding
        self.add_hewan_view.refetch_food()
        self.edit_hewan_view.refetch_food()


    def update_food(self, food_id, food_name):
        self.model.update_food(food_id, food_name)
        self.load_foods()
        self.add_hewan_view.refetch_food()
        self.edit_hewan_view.refetch_food()
        

    def delete_food(self, food_id):
        self.model.delete_food(food_id)
        self.load_foods()


    
