from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QMessageBox
from models.petModel import PetModel  # Import the PetModel

class FoodController:
    def __init__(self, view, model):
        self.model = model 
        self.view = view

        # Connect signals from the view to controller methods
        self.view.add_pet_signal.connect(self.add_pet)
        self.view.update_pet_signal.connect(self.update_pet)
        self.view.delete_pet_signal.connect(self.delete_pet)
        self.view.get_specific_pet_signal.connect(self.show_pet_details)
        self.view.filter_pet_by_food_signal.connect(self.filter_pet_by_food)
        self.view.get_update_data.connect(self.get_update_data)

        # Load all pets initially
        self.load_pets()

    def load_pets(self):
        # Get all pets from the model and set them in the view
        pets = self.model.get_all_pets()
        self.view.set_pets(pets)

    def add_pet(self, pet_name, species, age, medical_record, image):
        self.model.add_pet(pet_name, species, age, medical_record, image)
        self.load_pets()  # Refresh the view after adding a pet

    def update_pet(self, pet_id, pet_name, species, age, medical_record, image):
        self.model.update_pet(pet_id, pet_name, species, age, medical_record, image)
        self.load_pets()  # Refresh the view after updating

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
