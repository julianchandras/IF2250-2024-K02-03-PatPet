from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel, QFileDialog
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QPixmap

class EditPetView(QWidget):
    # Signal to save the edited pet with additional image data
    save_pet_signal = pyqtSignal(int, str, str, int, str, bytes)  
    
    def __init__(self):
        super().__init__()
        self.selected_image_data = None  # To store the selected image data
        self.setup_ui()  # Initialize the user interface
        

    def setup_ui(self):
        layout = QVBoxLayout()
        
        # Input fields for pet details
        self.name_input = QLineEdit("Pet name")
        self.species_input = QLineEdit("Species")
        self.age_input = QLineEdit("10")
        self.medical_record_input = QLineEdit("Medical record")

        # Image upload
        self.image_label = QLabel("No Image Selected")
    
        self.upload_button = QPushButton("Upload Image")
        self.upload_button.clicked.connect(self.upload_image)  # Connect to upload image function
        
        # Save button to save changes
        self.save_button = QPushButton("Save Changes")
        self.save_button.clicked.connect(self.save_pet)  # Connect to save_pet function
        
        # Add widgets to the layout
        layout.addWidget(self.name_input)
        layout.addWidget(self.species_input)
        layout.addWidget(self.age_input)
        layout.addWidget(self.medical_record_input)
        layout.addWidget(self.image_label)
        layout.addWidget(self.upload_button)  # Add upload button to layout
        layout.addWidget(self.save_button)  # Add save button to layout
        
        self.setLayout(layout)  # Set the layout for the view

    def upload_image(self):
        options = QFileDialog.Options()  # Options for file dialog
        file_path, _ = QFileDialog.getOpenFileName(
            self, "Select Image", "", "Image Files (*.png *.jpg *.jpeg)", options=options
        )
        
        if file_path:
            self.image_label.setText(f"Selected: {file_path}")  # Display the selected file path
            self.image_label.setPixmap(QPixmap(file_path).scaled(100, 100))  # Display the image
            # Read the image data for saving
            with open(file_path, "rb") as image_file:
                self.selected_image_data = image_file.read()

    def save_pet(self):
        pet_name = self.name_input.text()
        species = self.species_input.text()
        age = int(self.age_input.text())
        medical_record = self.medical_record_input.text()
    
        # Emit the signal to save the edited pet, including the image data if selected
        self.save_pet_signal.emit(
            self.pet_id,  # Pet ID passed to the view by the controller
            pet_name,
            species,
            age,
            medical_record,
            self.selected_image_data  # Include the selected image data, if any
        )
