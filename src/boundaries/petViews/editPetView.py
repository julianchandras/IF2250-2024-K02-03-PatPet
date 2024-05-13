from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel, QFileDialog, QApplication,QGridLayout, QComboBox, QTextEdit
from PyQt5.QtCore import pyqtSignal,Qt
from PyQt5.QtGui import QPixmap, QCursor
from components.checkableCombobox import CheckableComboBox
from utils.font import get_font

class EditPetView(QWidget):
    # Signal to save the edited pet with additional image data
    save_pet_signal = pyqtSignal(int, str, str, int, str, bytes,list)  
    
    def __init__(self):
        super().__init__()
        self.selected_image_data = None  # To store the selected image data
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
        main_content_widget.setStyleSheet("background-color: #BFE8DE;")

        # Title widget with fixed height and bottom pink border
        title_widget = QWidget()
        title_layout = QVBoxLayout(title_widget)

        screen_height = QApplication.desktop().availableGeometry().height()
        title_widget.setFixedHeight(int(1/6 * screen_height))  # Adjust as needed
        title_widget.setStyleSheet("QWidget {background-color: white; border-bottom: 15px solid #1A646B;}")

        # Create the title label with specified styles
        title_label = QLabel("Edit Hewan")
        title_style = "border:none; color: #1A646B; font-size: 80px; font-weight: bold; padding-left: 30px"
        title_label.setFont(get_font("bold"))
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
        nama_label.setFont(get_font("bold"))
        form_layout.addWidget(nama_label, 0, 0, 1, 2)  # Span 2 columns

        # Apply input style to all QLineEdit instances
        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Masukkan Nama")
        self.name_input.setStyleSheet(input_style)
        self.name_input.setFont(get_font("regular"))
        form_layout.addWidget(self.name_input, 1, 0, 1, 2)

        species_label = QLabel("Jenis Hewan:")
        species_label.setStyleSheet(label_style)
        species_label.setFont(get_font("bold"))
        form_layout.addWidget(species_label, 2, 0)

        self.species_input = QLineEdit()
        self.species_input.setPlaceholderText("Masukkan Jenis Hewan")
        self.species_input.setStyleSheet(input_style)  # Apply input style
        self.species_input.setFont(get_font("reguler"))
        form_layout.addWidget(self.species_input, 3, 0)

        # Similarly, apply the label style to other labels
        umur_label = QLabel("Umur:")
        umur_label.setStyleSheet(label_style)
        umur_label.setFont(get_font("bold"))
        form_layout.addWidget(umur_label, 2, 1, Qt.AlignTop)  # Align to top

        self.age_input = QLineEdit()
        self.age_input.setPlaceholderText("Masukkan Umur")
        self.age_input.setFont(get_font("regular"))
        self.age_input.setStyleSheet(input_style)  # Apply input style
        form_layout.addWidget(self.age_input, 3, 1)

        riwayat_label = QLabel("Riwayat Penyakit:")
        riwayat_label.setFont(get_font("bold"))
        riwayat_label.setStyleSheet(label_style)
        form_layout.addWidget(riwayat_label, 4, 0)

        self.medical_record_input = QTextEdit()
        self.medical_record_input.setPlaceholderText("Masukkan Riwayat Penyakit")
        self.medical_record_input.setFont(get_font("regular"))
        self.medical_record_input.setStyleSheet(input_style)
        form_layout.addWidget(self.medical_record_input, 5, 0, 3, 1)

        # Adding combo box and other elements with correct styling
        makanan_label = QLabel("Daftar Makanan:")
        makanan_label.setStyleSheet(label_style)
        makanan_label.setFont(get_font("bold"))
        form_layout.addWidget(makanan_label, 4, 1)

        self.food_list_input = CheckableComboBox()
        self.food_list_input.setFont(get_font("regular"))
       
        form_layout.addWidget(self.food_list_input, 5, 1)

        # Add image label and upload button
        image_label = QLabel("Image:")
        image_label.setStyleSheet(label_style)
        image_label.setFont(get_font("bold"))
        form_layout.addWidget(image_label, 9, 0, 1, 2)

        self.image_label = QLabel("No Image Selected")
        self.image_label.setStyleSheet(label_style)
        self.image_label.setFont(get_font("regular"))
        form_layout.addWidget(self.image_label, 10, 0)

        self.upload_button = QPushButton("Upload Gambar")
        self.upload_button.setStyleSheet("""
            QPushButton {
                background-color: #1A646B;
                font-weight: bold;
                border-radius: 8px;
                padding: 20px 5px;
                color : white;
                font-size : 24px;
                
            }

            QPushButton:hover {
                background-color: #6E9DA1;
            }
        """)
        self.upload_button.setFont(get_font("regular"))
        self.upload_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.upload_button.clicked.connect(self.upload_image)
        form_layout.addWidget(self.upload_button, 11, 0)

        # Save button
        self.save_pet_button = QPushButton("Ubah Hewan")
        self.save_pet_button.clicked.connect(self.save_pet)
        self.save_pet_button.setStyleSheet("""
            QPushButton {
                background-color: #F277AD;
                font-weight: bold;
                border-radius: 8px;
                padding: 20px 5px;
                color : white;
                font-size: 26px;
            }

            QPushButton:hover {
                background-color: #F8B8D4;
            }
        """)
        self.save_pet_button.setFont(get_font("regular"))
        self.save_pet_button.setCursor(QCursor(Qt.PointingHandCursor))
        form_layout.addWidget(self.save_pet_button, 11, 1, 1, 2)  # Adjusting column span
        
        # Add the form layout to the form widget
        form_widget.setLayout(form_layout)

        # Add form_widget to main_content_layout
        main_content_layout.addWidget(form_widget)

        # Add main_content_widget to main_layout
        main_layout.addWidget(main_content_widget)

        # Set the main layout for AddPetView
        self.setLayout(main_layout)

    def set_pet_details(self, pet, foods):
        # Set the pet details in the input fields
        self.pet_id = pet[0]
        self.name_input.setText(pet[1])
        self.species_input.setText(pet[2])
        self.age_input.setText(str(pet[3]))
        self.medical_record_input.setPlainText(pet[4])
        
        # Load the image data into a QPixmap and display it
        pixmap = QPixmap()
        pixmap.loadFromData(pet[5])
        self.image_label.setPixmap(pixmap.scaled(int(self.screen_geometry.width() * 0.3), int(self.screen_geometry.width() * 0.175)))

        self.selected_image_data = pet[5]
        for food in foods:
            print(food)
            index = self.food_list_input.findText(food)
            
            if index >= 0:
                self.food_list_input.setCheckState(index, True)

        

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

        selected_foods = self.food_list_input.currentData()

    
        # Emit the signal to save the edited pet, including the image data if selected
        self.save_pet_signal.emit(
            self.pet_id,  # Pet ID passed to the view by the controller
            pet_name,
            species,
            age,
            medical_record,
            self.selected_image_data,  # Include the selected image data, if any
            selected_foods
        )

    def set_food(self, food_list):
        self.food_list_input.clear()
        # Set the food list in the combo box
        self.food_list_input.addItems(food_list)

    
   

