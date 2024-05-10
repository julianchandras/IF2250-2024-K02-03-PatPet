from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QStackedWidget
from boundaries.mainView import MainView

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

        # Signal di main pet page
        self.main_view.add_pet_signal.connect(self.show_add_pet_view)  # Ini untuk navigasi ke add_pet_view
        self.main_view.view_pet_signal.connect(self.navigate_to_detail)  # Ini untuk navigasi ke detail_pet_view
        self.main_view.filter_signal.connect(self.handle_filter)

        self.load_pets()
    
    def load_pets(self):
        pets = self.pet_model.get_all_pets()
        self.main_view.set_pets(pets)

    def show_activity_today(self):
        activities = self.activity_model.get_all_activities()
        self.main_view.set_activities(activities)

    def handle_filter(self, foods):
        filtered_pets = self.pet_model.filter_pet_by_food(foods)
        self.main_view.set_pets(filtered_pets)

    def navigate_to_detail(self, pet_id):
        # Fetch pet details and switch to DetailPetView
        pet = self.pet_model.get_specific_pet(pet_id)
        self.detail_pet_view.set_pet_details(pet)
        self.stacked_widget.setCurrentIndex(5)  # Navigate to DetailPetView

    def show_add_pet_view(self):
        # Switch to the AddPetView
        self.stacked_widget.setCurrentIndex(3)