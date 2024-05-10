from PyQt5.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QPushButton,
    QTableWidget,
    QTableWidgetItem,
)
from PyQt5.QtCore import pyqtSignal

class MainView(QWidget):
    # Signals to navigate to other views
    add_pet_signal = pyqtSignal()  # Signal to switch to AddPetView
    view_pet_signal = pyqtSignal(int)  # Signal to switch to DetailPetView with pet ID
    filter_pet_signal = pyqtSignal(list)  # Signal to filter pets by food

    
    def __init__(self):
        super().__init__()
        self.setup_ui()  # Initialize the user interface
    
    def setup_ui(self):
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        # Button to add a new pet
        self.add_pet_button = QPushButton("Add Pet")
        self.add_pet_button.clicked.connect(self.add_pet)
        
        # Table to display pets
        self.pets_table = QTableWidget(0, 2)  # 2 columns: ID and Name
        self.pets_table.setHorizontalHeaderLabels(["ID", "Name"])
        self.pets_table.cellClicked.connect(self.view_pet)
        
        # Add widgets to layout
        layout.addWidget(self.add_pet_button)  # Button to add a new pet
        layout.addWidget(self.pets_table)  # Table to list pets
        
        self.setLayout(layout)

    def add_pet(self):
        self.add_pet_signal.emit()  # Emit signal to switch to AddPetView

    def view_pet(self, row):
        pet_id = int(self.pets_table.item(row, 0).text())  # Get pet ID from the table
        self.view_pet_signal.emit(pet_id)  # Emit signal to switch to DetailPetView

    def filter_pet(self):
        pets = []
        
        self.filter_pet_signal.emit(pets)

    def set_pets(self, pets):
        self.pets_table.setRowCount(len(pets))
        for row, pet in enumerate(pets):
            for col, field in enumerate(pet):
                item = QTableWidgetItem(str(field))
                self.pets_table.setItem(row, col, item)

    def set_activity(self, activities):
        self.activities_table.setRowCount(len(activities))
        for row, activity in enumerate(activities):
            for col, field in enumerate(activity):
                item = QTableWidgetItem(str(field))
                self.activities_table.setItem(row, col, item)
