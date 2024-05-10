from PyQt5.QtWidgets import QStackedWidget
from PyQt5.QtGui import QPixmap
from boundaries.petViews.mainPetView import MainPetView
from boundaries.petViews.addPetView import AddPetView
from boundaries.petViews.detailPetView import DetailPetView
from boundaries.petViews.editPetView import EditPetView
from models.petModel import PetModel

class PetController:
    def __init__(self, stacked_widget : QStackedWidget, pet_model : PetModel):
    
        self.stacked_widget = stacked_widget
        self.pet_model = pet_model

        ## index 0 = main_pet_view
        ## index 1 = add_pet_view
        ## index 2 = detail_pet_view
        ## index 3 = edit_pet_view
        self.main_pet_view = self.stacked_widget.widget(0)  # Index 0: MainPetView
        self.add_pet_view = self.stacked_widget.widget(1)  # Index 1: AddPetView
        self.detail_pet_view = self.stacked_widget.widget(2)  # Index 2: DetailPetView
        self.edit_pet_view = self.stacked_widget.widget(3)  # Index 3: EditPetView
        
        
        # Signal di main pet page
        self.main_pet_view.add_pet_signal.connect(self.show_add_pet_view)  # Ini untuk navigasi ke add_pet_view
        self.main_pet_view.view_pet_signal.connect(self.show_detail_pet_view)  # Ini untuk navigasi ke detail_pet_view

        # Signal buat di add page
        self.add_pet_view.save_pet_signal.connect(self.save_pet)  # Ini untuk add pet dan save serta balikin ke main page

        # Signal buat di detail page
        self.detail_pet_view.edit_pet_signal.connect(self.show_edit_pet_view)  # Ini untuk navigasi ke edit_pet_view
        self.detail_pet_view.delete_pet_signal.connect(self.delete_pet)  # Delete the pet

        # Signal buat di edit page
        self.edit_pet_view.save_pet_signal.connect(self.save_pet_edits)  # Save pet edits and return to MainPetView
        
        # Load the initial pet list
        self.load_pets()  # Populate the main pet list

    def load_pets(self):
        pets = self.pet_model.get_all_pets()
        self.main_pet_view.set_pets(pets)

    def show_add_pet_view(self):
        # Switch to the AddPetView
        self.stacked_widget.setCurrentIndex(1)

    def save_pet(self, pet_name, species, age, medical_record, image):
        self.pet_model.add_pet(pet_name, species, age, medical_record, image)  # Save pet to the model
        self.load_pets()  # Refresh the pet list
        self.stacked_widget.setCurrentIndex(0)  # Return to MainPetView

    def show_detail_pet_view(self, pet_id):
        # Fetch pet details and switch to DetailPetView
        pet = self.pet_model.get_specific_pet(pet_id)
        self.detail_pet_view.set_pet_details(pet)
        self.stacked_widget.setCurrentIndex(2)  # Navigate to DetailPetView
    
    def show_edit_pet_view(self, pet_id):
        # Set the pet details in EditPetView and switch to it
        pet = self.pet_model.get_specific_pet(pet_id)
        self.edit_pet_view.name_input.setText(pet[1])
        self.edit_pet_view.species_input.setText(pet[2])
        self.edit_pet_view.age_input.setText(str(pet[3]))
        self.edit_pet_view.medical_record_input.setPlainText(pet[4])

        pixmap = QPixmap()
        pixmap.loadFromData(pet[5])
        self.edit_pet_view.image_label.setPixmap(pixmap.scaled(800, 600))
        self.edit_pet_view.pet_id = pet_id  # Pass the pet ID for saving changes
        self.edit_pet_view.selected_image_data = pet[5]
        self.stacked_widget.setCurrentIndex(3)  # Navigate to EditPetView

    def save_pet_edits(self, pet_id, pet_name, species, age, medical_record, image):
        self.pet_model.update_pet(pet_id, pet_name, species, age, medical_record, image)
        self.load_pets()
        self.stacked_widget.setCurrentIndex(0)
    
    def delete_pet(self, pet_id):
        self.pet_model.delete_pet(pet_id)  # Delete pet from the model
        self.load_pets()  # Refresh the pet list
        self.stacked_widget.setCurrentIndex(0)  # Return to MainPetView
