from PyQt5.QtWidgets import QStackedWidget
from PyQt5.QtWidgets import QMessageBox
from models.foodModel import FoodModel  # Import the PetModel
from boundaries.foodViews.mainFoodView import MainFoodView  # Import the MainFoodView
from boundaries.mainView import MainView
from boundaries.petViews.addPetView import AddPetView
from boundaries.petViews.editPetView import EditPetView
from boundaries.petViews.detailPetView import DetailPetView

class FoodController:
    def __init__(self, stacked_widget : QStackedWidget, food_model : FoodModel):
        self.stacked_widget = stacked_widget
        self.food_model : FoodModel = food_model

        self.main_view : MainView = self.stacked_widget.widget(0)  # Main view index 0
        self.main_food_view : MainFoodView = self.stacked_widget.widget(6)  # Main food view index 6
        self.add_hewan_view : AddPetView = self.stacked_widget.widget(3)  # Add hewan view index 3
        self.edit_hewan_view : EditPetView = self.stacked_widget.widget(4)
        self.detail_hewan_view : DetailPetView = self.stacked_widget.widget(5)

        self.main_food_view.add_food_signal.connect(self.add_food)
        self.main_food_view.update_food_signal.connect(self.update_food)
        self.main_food_view.delete_food_signal.connect(self.delete_food)
        # Load all foods initially
        self.load_foods()

    def load_foods(self):
        # Get all foods from the model and set them in the view
        foods = self.food_model.get_all_food()
        food_eater_list = self.food_model.get_food_eater()
        self.main_food_view.set_food(food_eater_list)
        self.add_hewan_view.set_food(foods)
        self.main_view.set_food(foods)
        self.edit_hewan_view.set_food(foods)
        
    def add_food(self, food_name):
        self.food_model.add_food(food_name)
        self.load_foods()  # Refresh the view after adding

    def update_food(self, food_id, food_name):
        self.food_model.update_food(food_id, food_name)
        self.load_foods()

    def delete_food(self, food_id):
        self.food_model.delete_food(food_id)
        self.load_foods()


    
