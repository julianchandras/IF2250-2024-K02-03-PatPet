from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QPushButton, QFileDialog, QLabel, QGridLayout, QApplication, QTextEdit
from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtGui import QPixmap
from components.checkableCombobox import CheckableComboBox


class AddPetView(QWidget):
    save_pet_signal = pyqtSignal(str, str, int, str, bytes, list)  # Signal to save a new pet

    def __init__(self):
        super().__init__()
        self.setup_ui()  # Initialize the user interface

    def setup_ui(self):
        self.screen_geometry = QApplication.desktop().availableGeometry()

        
        # Main layout with no margins and spacing
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        # Main content widget with pink background
        main_content_widget = QWidget(self)
        main_content_layout = QVBoxLayout(main_content_widget)
        main_content_layout.setContentsMargins(96, 46, 96, 46)
        main_content_widget.setStyleSheet("background-color: #FFD7E0;")

        # Title widget with fixed height and bottom pink border
        title_widget = QWidget()
        title_layout = QVBoxLayout(title_widget)

        title_widget.setFixedHeight(int(1/6 * self.screen_geometry.height()))  # Adjust as needed
        title_widget.setStyleSheet("QWidget {background-color: white; border-bottom: 8px solid #F277AD;}")

        # Create the title label with specified styles
        title_label = QLabel("Tambah Hewan")
        title_style = "border:none; color: #F277AD; font-size: 80px; font-weight: bold; padding-left: 30px"
        title_label.setStyleSheet(title_style)
        title_layout.addWidget(title_label)

        # Add the title widget to the main content layout
        main_content_layout.addWidget(title_widget)

        # Form widget with white background
        form_widget = QWidget()
        form_widget.setStyleSheet("background-color: white;")

        # Form layout for arranging form elements
        form_layout = QGridLayout()
        form_layout.setAlignment(Qt.AlignTop)  # Align to the top
        form_layout.setSpacing(30)  # Adjust spacing between elements
        form_layout.setContentsMargins(80, 80, 80, 80)  # Adjust margins as needed

        # Define label and input styles
        label_style = "font-size: 32px; font-weight: bold; color: black;"  # Label style
        input_style = "border: 2px solid gray; border-radius: 10px; padding: 10px;"  # LineEdit style

        # Apply label style to all QLabel instances
        nama_label = QLabel("Nama")
        nama_label.setStyleSheet(label_style)
        form_layout.addWidget(nama_label, 0, 0, 1, 2)  # Span 2 columns

        # Apply input style to all QLineEdit instances
        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Masukkan Nama")
        self.name_input.setStyleSheet(input_style)
        form_layout.addWidget(self.name_input, 1, 0, 1, 2)

        species_label = QLabel("Jenis Hewan:")
        species_label.setStyleSheet(label_style)
        form_layout.addWidget(species_label, 2, 0)

        self.species_input = QLineEdit()
        self.species_input.setPlaceholderText("Masukkan Jenis Hewan")
        self.species_input.setStyleSheet(input_style)  # Apply input style
        form_layout.addWidget(self.species_input, 3, 0)

        # Similarly, apply the label style to other labels
        umur_label = QLabel("Umur:")
        umur_label.setStyleSheet(label_style)
        form_layout.addWidget(umur_label, 2, 1, Qt.AlignTop)  # Align to top

        self.age_input = QLineEdit()
        self.age_input.setPlaceholderText("Masukkan Umur")
        self.age_input.setStyleSheet(input_style)  # Apply input style
        form_layout.addWidget(self.age_input, 3, 1)

        riwayat_label = QLabel("Riwayat Penyakit:")
        riwayat_label.setStyleSheet(label_style)
        form_layout.addWidget(riwayat_label, 4, 0)

        self.medical_record_input = QTextEdit()
        self.medical_record_input.setPlaceholderText("Masukkan Riwayat Penyakit")
        self.medical_record_input.setStyleSheet(input_style)
        form_layout.addWidget(self.medical_record_input, 5, 0, 3, 1)

        # Adding combo box and other elements with correct styling
        # Adding combo box and other elements with correct styling
        makanan_label = QLabel("Daftar Makanan:")
        makanan_label.setStyleSheet(label_style)
        form_layout.addWidget(makanan_label, 4, 1)

        # Using the CheckableComboBox for multi-selection
        self.food_list_input = CheckableComboBox()
       
        form_layout.addWidget(self.food_list_input, 5, 1)


        # Add image label and upload button
        image_label = QLabel("Image:")
        image_label.setStyleSheet(label_style)
        form_layout.addWidget(image_label, 9, 0, 1, 2)

        self.image_label = QLabel("No Image Selected")
        self.image_label.setStyleSheet(label_style)
        form_layout.addWidget(self.image_label, 10, 0)

        self.upload_button = QPushButton("Upload Image")
        self.upload_button.clicked.connect(self.upload_image)
        form_layout.addWidget(self.upload_button, 11, 0)

        # Save button
        self.save_pet_button = QPushButton("Save Pet")
        self.save_pet_button.clicked.connect(self.save_pet)
        form_layout.addWidget(self.save_pet_button, 11, 1, 1, 2)  # Adjusting column span
        
        # Add the form layout to the form widget
        form_widget.setLayout(form_layout)

        # Add form_widget to main_content_layout
        main_content_layout.addWidget(form_widget)

        # Add main_content_widget to main_layout
        main_layout.addWidget(main_content_widget)

        # Set the main layout for AddPetView
        self.setLayout(main_layout)

    def upload_image(self):
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileName(
            self, "Select Image", "", "Image Files (*.png *.jpg *.jpeg)", options=options
        )

        
        if file_path:
            self.image_label.setText(f"Selected: {file_path}")
            self.image_label.setPixmap(QPixmap(file_path).scaled(int(self.screen_geometry.width() * 0.3), int(self.screen_geometry.width() * 0.175)))
            with open(file_path, "rb") as image_file:
                self.selected_image_data = image_file.read()

    def save_pet(self):
        pet_name = self.name_input.text()
        species = self.species_input.text()
        age = int(self.age_input.text())
        medical_record = self.medical_record_input.toPlainText()
        image = getattr(self, 'selected_image_data', None)

        selected_foods = self.food_list_input.currentData()
        self.save_pet_signal.emit(pet_name, species, age, medical_record, image, selected_foods)  # Emit signal to save pet

    def set_food(self, food_list):
        self.food_list_input.clear()
        self.food_list_input.addItems(food_list)

    def clear_input(self):
        self.name_input.clear()
        self.species_input.clear()
        self.age_input.clear()
        self.medical_record_input.clear()
        self.image_label.setText("No Image Selected")
        self.selected_image_data = None
        for index in range(self.food_list_input.count()):
            self.food_list_input.setCheckState(index, Qt.Unchecked)

