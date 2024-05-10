from PyQt5.QtWidgets import QStackedWidget
from PyQt5.QtGui import QPixmap

from boundaries.petViews.addPetView import AddPetView
from boundaries.petViews.detailPetView import DetailPetView
from boundaries.petViews.editPetView import EditPetView
from models.petModel import PetModel

class PetController:
    stacked_widget : QStackedWidget
    pet_model : PetModel
    add_pet_view : AddPetView
    edit_pet_view : EditPetView
    detail_pet_view : DetailPetView

    def __init__(self, stacked_widget : QStackedWidget, pet_model : PetModel):
    
        self.stacked_widget = stacked_widget
        self.pet_model = pet_model

        ## index 0 = main_pet_view
        ## index 1 = main article view
        ## index 2 = detail_article_view
        ## index 3 = add_pet_view
        ## index 4 = update_pet_view
        ## index 5 = detail_pet_view
        ## index 6 = main_food_view
        ## index 7 = add_activity_view
        ## index 8 = update_activity_view

        self.main_pet_view = self.stacked_widget.widget(0)  # Main pet view index 0
        self.add_pet_view  = self.stacked_widget.widget(3) 
        self.edit_pet_view = self.stacked_widget.widget(4)  
        self.detail_pet_view = self.stacked_widget.widget(5)  
    
        # Signal buat di add page
        self.add_pet_view.save_pet_signal.connect(self.save_pet)  # Ini untuk add pet dan save serta balikin ke main page

        # Signal buat di detail page
        self.detail_pet_view.edit_pet_signal.connect(self.show_edit_pet_view)  # Ini untuk navigasi ke edit_pet_view
        self.detail_pet_view.delete_pet_signal.connect(self.delete_pet)  # Delete the pet

        # Signal buat di edit page
        self.edit_pet_view.save_pet_signal.connect(self.save_pet_edits)  # Save pet edits and return to MainPetView
        
    def load_pets(self):
        pets = self.pet_model.get_all_pets()
        self.main_pet_view.set_pets(pets)

    def save_pet(self, pet_name, species, age, medical_record, image):
        self.pet_model.add_pet(pet_name, species, age, medical_record, image)  # Save pet to the model
        # Refresh the pet list
        self.load_pets()
        self.stacked_widget.setCurrentIndex(0)  # Return to MainPetView

    def show_edit_pet_view(self, pet_id):
        # Set the pet details in EditPetView and switch to it
        pet = self.pet_model.get_specific_pet(pet_id)
        self.edit_pet_view.set_pet_details(pet)
        self.stacked_widget.setCurrentIndex(4)  # Navigate to EditPetView

    def save_pet_edits(self, pet_id, pet_name, species, age, medical_record, image, food_list):
        self.pet_model.update_pet(pet_id, pet_name, species, age, medical_record, image)

        for food in food_list:
            self.pet_model.add_food(pet_id, food)

        self.load_pets()
        self.stacked_widget.setCurrentIndex(0)
    
    def delete_pet(self, pet_id):
        self.pet_model.delete_pet(pet_id)  # Delete pet from the model
        self.load_pets()  # Refresh the pet list
        self.stacked_widget.setCurrentIndex(0)  # Return to MainPetView



    