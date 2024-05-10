from PyQt5.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QGroupBox,
    QScrollArea,
    QApplication
)
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtCore import Qt, pyqtSignal

class DetailPetView(QWidget):
    edit_pet_signal = pyqtSignal(int)  # Signal to switch to EditPetView
    delete_pet_signal = pyqtSignal(int)  # Signal to delete the pet
    
    def __init__(self):
        super().__init__()
        self.pet_id = None  # To store the current pet's ID
        self.initUI()

    def initUI(self):
        screen_geometry = QApplication.desktop().availableGeometry()

        self.setWindowTitle('Detail Hewan')
        self.showFullScreen()

        main_layout = QHBoxLayout()
        main_layout.setContentsMargins(0, 0, 0, 0)

        # Main content
        main_content_widget = QWidget(self)
        main_content_layout = QVBoxLayout(main_content_widget)
        main_content_layout.setContentsMargins(
            int(screen_geometry.width() * 0.25),
            int(screen_geometry.height() * 0.05),
            int(screen_geometry.width() * 0.25),
            0,
        )
        main_content_widget.setStyleSheet('background-color: #F2F2F2;')
        main_content_widget.setFixedHeight(screen_geometry.height())

        # Labels for pet details
        animal_image_label = QLabel(self)
        animal_image_label.setPixmap(
            QPixmap('img/meng.png').scaled(
                int(screen_geometry.width() * 0.33),
                int(screen_geometry.height()),
                Qt.KeepAspectRatio,
            )
        )
        animal_image_label.setAlignment(Qt.AlignCenter)
        main_content_layout.addWidget(animal_image_label)

        # Group box for general information
        animal_general_box = QGroupBox(self)
        animal_general_box.setStyleSheet('border: none')
        animal_general_box.setFixedHeight(150)
        animal_general_layout = QVBoxLayout(animal_general_box)

        title_label = QLabel('Neo Woof', self)
        title_label.setStyleSheet('font-size: 48px; color: #1A646B; font-weight: bold;')
        animal_general_layout.addWidget(title_label)

        description_label = QLabel('Anjing | Umur : 2 bulan', self)
        description_label.setStyleSheet('font-size: 32px; color: #1A646B;')
        animal_general_layout.addWidget(description_label)

        main_content_layout.addWidget(animal_general_box)

        # Medical history
        medical_history_box = QGroupBox(self)
        medical_history_box.setStyleSheet('border: none')
        medical_history_box.setFixedHeight(100)
        medical_history_layout = QVBoxLayout(medical_history_box)

        mh_title_label = QLabel('Riwayat Penyakit', self)
        mh_title_label.setStyleSheet('font-size: 24px; font-weight: bold; color: #1A646B;')
        medical_history_layout.addWidget(mh_title_label)

        mh_label = QLabel('Kanker, kaki patah, patah hati', self)
        mh_label.setStyleSheet('font-size: 24px; color: #1A646B;')
        medical_history_layout.addWidget(mh_label)

        main_content_layout.addWidget(medical_history_box)

        # Food list with scrollable area
        food_list_box = QGroupBox(self)
        food_list_box.setStyleSheet('border: none')
        food_list_layout = QVBoxLayout(food_list_box)

        fl_title_label = QLabel('Daftar Makanan', self)
        fl_title_label.setStyleSheet('font-size: 24px; font-weight: bold; color: #1A646B;')
        fl_title_label.setFixedHeight(50)
        food_list_layout.addWidget(fl_title_label)

        fl_label = QLabel(self)
        fl_label.setText(
            "<ul>"
            "<li>Tempe</li>"
            "<li>Telur</li>"
            "<li>Tahu</li>"
            "</ul>"
        )
        fl_label.setStyleSheet('font-size: 24px; color: #1A646B;')
        
        scroll_area = QScrollArea()
        scroll_area.setWidget(fl_label)
        scroll_area.setWidgetResizable(True)
        scroll_area.setFixedHeight(150)
        scroll_area.setStyleSheet(
            """
            QScrollBar:vertical {
                border: none;
                background: white;
                width: 10px;
                margin: 0px 0px 0px 0px;
            }
            QScrollBar::handle:vertical {
                background: #1A646B;
                min-height: 20px;
                border-radius: 5px;
            }
            QScrollBar::add-line:vertical {
                background: none;
            }
            QScrollBar::sub-line:vertical {
                background: none;
            }
            """
        )
        food_list_layout.addWidget(scroll_area)

        main_content_layout.addWidget(food_list_box)

        # Edit and delete buttons
        button_box = QGroupBox(self)
        button_box.setStyleSheet('border: none')
        button_box.setFixedSize(300, 70)
        button_layout = QHBoxLayout(button_box)

        change_profile_button = QPushButton('Ubah Profil', self)
        change_profile_button.setStyleSheet('background-color: #1A646B; font-size: 18px; color: white; padding: 17px 13px; border: none; border-radius: 5px;')
        change_profile_button.setFixedSize(120, 50)
        change_profile_button.clicked.connect(self.edit_pet)  # Connect to edit method
        button_layout.addWidget(change_profile_button)

        delete_animal_button = QPushButton('Hapus Hewan', self)
        delete_animal_button.setStyleSheet('background-color: #F277AD; font-size: 18px; color: white; padding: 17px 13px; border: none; border-radius: 5px;')
        delete_animal_button.setFixedSize(150, 50)
        delete_animal_button.clicked.connect(self.delete_pet)  # Connect to delete method
        button_layout.addWidget(delete_animal_button)

        main_content_layout.addWidget(button_box)

        main_layout.addWidget(main_content_widget)

        self.setLayout(main_layout)

    def edit_pet(self):
        # Emit signal to switch to EditPetView
        if self.pet_id is not None:
            self.edit_pet_signal.emit(self.pet_id)

    def delete_pet(self):
        # Emit signal to delete the pet
        if self.pet_id is not None:
            self.delete_pet_signal.emit(self.pet_id)

    def set_pet_details(self, pet):
        """
        Set pet details in labels.
        pet is a tuple (pet_id, name, species, age, medical_record, image_data)
        """
        self.pet_id = pet[0]
        # Set general information
        title_label = self.findChild(QLabel, 'Neo Woof')
        description_label = self.findChild(QLabel, 'Anjing | Umur : 2 bulan')

        if title_label:
            title_label.setText(f"{pet[1]}")
        
        if description_label:
            description_label.setText(f"{pet[2]} | Umur: {pet[3]} bulan")

        # Set medical history
        mh_label = self.findChild(QLabel, 'Kanker, kaki patah, patah hati')
        if mh_label:
            mh_label.setText(pet[4])

        # Set pet image
        animal_image_label = self.findChild(QLabel, 'Meng.png')  # Update the image label
        if pet[5]:
            pixmap = QPixmap()
            pixmap.loadFromData(pet[5])
            animal_image_label.setPixmap(pixmap.scaled(200, 200, Qt.KeepAspectRatio))
        else:
            animal_image_label.setText("No Image")

