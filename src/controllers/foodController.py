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

    def delete_pet(self, pet_id):
        # Confirm deletion
        if self.view.confirm_deletion():
            self.model.delete_pet(pet_id)
            self.load_pets()  # Refresh the view after deletion

    def show_pet_details(self, pet):
    # Open the PetDetailDialog with the provided pet details
        pet = self.model.get_specific_pet(pet)

    def filter_pet_by_food(self, food):
        filtered_pets = self.model.filter_pet_by_food(food)
        self.view.set_pets(filtered_pets)  # Update the view with the filtered list

    def get_update_data(self,data):
        pet = self.model.get_specific_pet(int(data))
        self.view.name_input.setText(pet[1])
        self.view.species_input.setText(pet[2])
        self.view.age_input.setText(str(pet[3]))
        self.view.medical_record_input.setText(pet[4])
        self.view.selected_image_data = pet[5]
