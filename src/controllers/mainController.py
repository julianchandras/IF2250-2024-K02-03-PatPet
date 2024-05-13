from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QStackedWidget
from boundaries.mainView import MainView
from boundaries.petViews.detailPetView import DetailPetView

from models.petModel import PetModel
from models.foodModel import FoodModel
from models.activityModel import ActivityModel


class MainController:
    def __init__(self, stacked_widget: QStackedWidget, food_model : FoodModel, pet_model : PetModel, activity_model : ActivityModel):
        
        self.stacked_widget : QStackedWidget  = stacked_widget
        self.food_model : FoodModel = food_model
        self.pet_model : PetModel= pet_model
        self.activity_model : ActivityModel = activity_model

        self.main_view : MainView = self.stacked_widget.widget(0)  # Main view index 0
    
        self.add_pet_view = self.stacked_widget.widget(3)  # Add pet view index 3
        self.detail_pet_view : DetailPetView= self.stacked_widget.widget(5)  # Detail pet view index 5

        # Signal di main pet page
        self.main_view.add_pet_signal.connect(self.show_add_pet_view)  # Ini untuk navigasi ke add_pet_view
        self.main_view.view_pet_signal.connect(self.navigate_to_detail)  # Ini untuk navigasi ke detail_pet_view
        self.main_view.filter_pet_signal.connect(self.handle_filter)

        # Show activity dan 

    def handle_filter(self, foods):
        filtered_pets = self.food_model.filter_pet_by_food(foods)
        
        self.main_view.set_pets(filtered_pets)

    def navigate_to_detail(self, pet_id):
        # Fetch pet details and switch to DetailPetView
        pet = self.pet_model.get_specific_pet(pet_id)
        foods = self.food_model.get_pet_foods(pet_id)
        self.detail_pet_view.set_pet_details(pet,foods)
        self.stacked_widget.setCurrentIndex(5)  # Navigate to DetailPetView

    def show_add_pet_view(self):
        # Switch to the AddPetView
        self.stacked_widget.setCurrentIndex(3)