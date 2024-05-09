from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QPushButton, QFileDialog, QLabel, QComboBox, QFormLayout
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QPixmap

class AddPetView(QWidget):
    save_pet_signal = pyqtSignal(str, str, int, str, bytes)  # Signal to save a new pet
    
    def __init__(self):
        super().__init__()
        self.setup_ui()  # Initialize the user interface

    def setup_ui(self):

        # Create a form layout to pair labels with their corresponding input fields
        form_layout = QFormLayout()

        # Labels and input fields
        self.name_label = QLabel("Nama")
        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Masukkan Nama")

        self.species_label = QLabel("Jenis Hewan")
        self.species_input = QLineEdit()
        self.species_input.setPlaceholderText("Masukkan Jenis Hewan")

        self.age_label = QLabel("Umur")
        self.age_input = QLineEdit()
        self.age_input.setPlaceholderText("Masukkan Umur")

        self.medical_record_label = QLabel("Riwayat Penyakit")
        self.medical_record_input = QLineEdit()
        self.medical_record_input.setPlaceholderText("Masukkan Riwayat Penyakit")

        self.food_list_label = QLabel("Daftar Makanan")
        self.food_list_input = QComboBox()
        self.food_list_input.addItems(["Tempe", "Tahu", "Susu", "Daging", "Ikan"])

        # Add labels and corresponding inputs to the form layout
        form_layout.addRow(self.name_label, self.name_input)
        form_layout.addRow(self.species_label, self.species_input)
        form_layout.addRow(self.age_label, self.age_input)
        form_layout.addRow(self.medical_record_label, self.medical_record_input)
        form_layout.addRow(self.food_list_label, self.food_list_input)

        # Label for displaying the selected image
        self.image_label = QLabel("No Image Selected")
        form_layout.addRow(self.image_label)
        

        # Button for uploading images
        self.upload_button = QPushButton("Upload Image")
        self.upload_button.clicked.connect(self.upload_image)

        # Button for saving the new pet
        self.save_pet_button = QPushButton("Save Pet")
        self.save_pet_button.clicked.connect(self.save_pet)

        # Create a vertical layout and add the form layout and other widgets
        layout = QVBoxLayout()
        layout.addLayout(form_layout)  # Add the form layout to the main layout
        layout.addWidget(self.upload_button)
        layout.addWidget(self.save_pet_button)

        self.setLayout(layout)

    def upload_image(self):
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileName(
            self, "Select Image", "", "Image Files (*.png *.jpg *.jpeg)", options=options
        )
        if file_path:
            self.image_label.setText(f"Selected: {file_path}")
            self.image_label.setPixmap(QPixmap(file_path).scaled(100, 100))
            with open(file_path, "rb") as image_file:
                self.selected_image_data = image_file.read()

    def save_pet(self):
        pet_name = self.name_input.text()
        species = self.species_input.text()
        age = int(self.age_input.text())
        medical_record = self.medical_record_input.text()
        image = getattr(self, 'selected_image_data', None)
        
        self.save_pet_signal.emit(pet_name, species, age, medical_record, image)  # Emit signal to save pet
