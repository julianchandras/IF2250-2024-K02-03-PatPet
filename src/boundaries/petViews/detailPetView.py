from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QPixmap

class DetailPetView(QWidget):
    edit_pet_signal = pyqtSignal(int)  # Signal to switch to EditPetView
    delete_pet_signal = pyqtSignal(int)  # Signal to delete the current pet
    
    def __init__(self):
        super().__init__()
        self.setup_ui()  # Initialize the user interface

    def setup_ui(self):
        layout = QVBoxLayout()
        
        # Labels to display pet details
        self.id_label = QLabel("Pet ID")
        self.name_label = QLabel("Pet Name")
        self.species_label = QLabel("Species")
        self.age_label = QLabel("Age")
        self.medical_record_label = QLabel("Medical Record")
        self.image_label = QLabel("Image")
        
        # Buttons to edit or delete the pet
        self.edit_button = QPushButton("Edit Pet")
        self.delete_button = QPushButton("Delete Pet")
        
        self.edit_button.clicked.connect(self.edit_pet)
        self.delete_button.clicked.connect(self.delete_pet)
        
        # Add widgets to layout
        layout.addWidget(self.id_label)
        layout.addWidget(self.name_label)
        layout.addWidget(self.species_label)
        layout.addWidget(self.age_label)
        layout.addWidget(self.medical_record_label)
        layout.addWidget(self.image_label)
        layout.addWidget(self.edit_button)
        layout.addWidget(self.delete_button)
        
        self.setLayout(layout)

    def edit_pet(self):
        # Emit signal to switch to EditPetView
        self.edit_pet_signal.emit(self.pet_id)

    def delete_pet(self):
        # Emit signal to delete the pet
        self.delete_pet_signal.emit(self.pet_id)

    def set_pet_details(self, pet):
        # Set pet details in labels
        self.pet_id = pet[0]
        self.id_label.setText(f"Pet ID: {self.pet_id}")
        self.name_label.setText(f"Pet Name: {pet[1]}")
        self.species_label.setText(f"Species: {pet[2]}")
        self.age_label.setText(f"Age: {pet[3]}")
        self.medical_record_label.setText(f"Medical Record: {pet[4]}")
        
        if pet[5]:
            pixmap = QPixmap()
            pixmap.loadFromData(pet[5])
            self.image_label.setPixmap(pixmap.scaled(100, 100))
        else:
            self.image_label.setText("No Image")
