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
from PyQt5.QtGui import QPixmap, QCursor
from PyQt5.QtCore import Qt, pyqtSignal
from utils.font import *
from utils.screensize import *

class DetailPetView(QWidget):
    edit_pet_signal = pyqtSignal(int)  # Signal to switch to EditPetView
    delete_pet_signal = pyqtSignal(int)  # Signal to delete the pet
    back_signal = pyqtSignal()
    
    def __init__(self):
        super().__init__()
        self.pet_id = None  # To store the current pet's ID
        self.initUI()

    def initUI(self):
        screen_geometry = QApplication.desktop().availableGeometry()


        main_layout = QHBoxLayout()
        main_layout.setContentsMargins(0, 0, 0, 0)
        # Main content
        main_content_widget = QWidget(self)
        main_content_layout = QVBoxLayout(main_content_widget)
        main_content_layout.setContentsMargins(
            int(getWidth() * 0.25),
            int(getHeight() * 0.05),
            int(getWidth() * 0.25),
            0,
        )
        main_content_layout.setSpacing(0)
        main_content_widget.setStyleSheet('background-color: #F2F2F2;')
        main_content_widget.setFixedHeight(getHeight())
        main_content_widget.setFixedWidth(int(getWidth() * 0.85))

    
        # Labels for pet details
        pic_width = 0
        pic_height = 0
        if getHeight() > 1080:
            pic_width = int(getWidth() * 0.33)
            pic_height = int(getHeight() * 0.4)
        else:
            pic_width = int(getWidth() * 0.2)
            pic_height = int(getHeight() * 0.3)

        animal_image_label = QLabel(self)
        animal_image_label.setObjectName("animalImageLabel")  # Set object name
        animal_image_label.setPixmap(
            QPixmap('img/meng.png').scaled(
                pic_width,
                pic_height,
                Qt.KeepAspectRatio,
            )
        )
        animal_image_label.setAlignment(Qt.AlignCenter)
        main_content_layout.addWidget(animal_image_label)

        # Group box for general information
        animal_general_box = QGroupBox(self)
        animal_general_box.setStyleSheet('border: none')
        animal_general_box.setFixedHeight(int(getHeight() * 0.1))
        animal_general_layout = QVBoxLayout(animal_general_box)

        title_label = QLabel('Pet Name', self)
        title_label.setObjectName('Pet Name')
        title_label.setStyleSheet('; color: #1A646B; font-weight: bold;')
        title_label.setFont(set_font("bold",24))
        animal_general_layout.addWidget(title_label)

        description_label = QLabel('Spesies | Umur: X Tahun', self)
        description_label.setObjectName('Spesies | Umur: X Tahun')
        description_label.setStyleSheet('color: #1A646B;')
        description_label.setFont(set_font("regular",12))
        animal_general_layout.addWidget(description_label)

        main_content_layout.addWidget(animal_general_box)

        # Medical history

        medical_history_box = QGroupBox(self)
        medical_history_box.setStyleSheet('border: none')
        medical_history_layout = QVBoxLayout(medical_history_box)
        medical_history_layout.setAlignment(Qt.AlignTop)

        mh_title_label = QLabel('Riwayat Penyakit', self)
        mh_title_label.setObjectName('Riwayat Penyakit')
        mh_title_label.setStyleSheet('font-weight: bold; color: #1A646B;')
        mh_title_label.setFont(set_font("bold",14))
        medical_history_layout.addWidget(mh_title_label)

        mh_label = QLabel('Deskripsi Penyakit', self)
        mh_label.setObjectName('Deskripsi Penyakit')
        mh_label.setStyleSheet('color: #1A646B;')
        mh_label.setFont(set_font("regular",12))
        mh_label.setMaximumWidth(int(getWidth() * 0.825))
        mh_label.setWordWrap(True)
        medical_history_layout.addWidget(mh_label)

        scroll_medical = QScrollArea()
        scroll_medical.setWidget(medical_history_box)
        scroll_medical.setWidgetResizable(True)
        scroll_medical.setFixedHeight(int(getHeight() * 0.225))
        scroll_medical.setStyleSheet(
            """
            QScrollArea {
                border: none; 
            }
            QScrollBar:vertical {
                border: none;
                background: #f0f0f0;
                width: 10px;
                margin: 0px 0px 0px 0px;
            }
            QScrollBar::handle:vertical {
                background: #c0c0c0;
                min-height: 20px;
            }
            QScrollBar::handle:vertical:hover {
                background: #a0a0a0;
            }
            QScrollBar::sub-line:vertical {
                border: none;
                background: none;
            }
            QScrollBar::add-line:vertical {
                border: none;
                background: none;
            }
            QScrollBar:horizontal {
                border: none;
                background: #f0f0f0;
                height: 10px;
                margin: 0px 0px 0px 0px;
            }
            QScrollBar::handle:horizontal {
                background: #c0c0c0;
                min-width: 20px;
            }
            QScrollBar::handle:horizontal:hover {
                background: #a0a0a0;
            }
            QScrollBar::sub-line:horizontal {
                border: none;
                background: none;
            }
            QScrollBar::add-line:horizontal {
                border: none;
                background: none;
            }
            """
        )
        # main_content_layout.addWidget(medical_history_box)
        main_content_layout.addWidget(scroll_medical)

        # Food list with scrollable area
        food_list_box = QGroupBox(self)
        food_list_box.setStyleSheet('border: none')
        food_list_layout = QVBoxLayout(food_list_box)
        food_list_layout.setAlignment(Qt.AlignTop)

        fl_title_label = QLabel('Daftar Makanan', self)
        fl_title_label.setStyleSheet('font-weight: bold; color: #1A646B;')
        fl_title_label.setFont(set_font("bold",14))
        fl_title_label.setFixedHeight(50)
        food_list_layout.addWidget(fl_title_label)

        self.fl_label = QLabel(self)
        self.fl_label.setStyleSheet('color: #1A646B;')
        self.fl_label.setFont(set_font("regular",12))

        scroll_area = QScrollArea()
        scroll_area.setWidget(self.fl_label)
        scroll_area.setWidgetResizable(True)
        scroll_area.setFixedHeight(int(getHeight() * 0.2))
        scroll_area.setStyleSheet(
            """
            QScrollArea {
                border: none; 
            }
            QScrollBar:vertical {
                border: none;
                background: #f0f0f0;
                width: 10px;
                margin: 0px 0px 0px 0px;
            }
            QScrollBar::handle:vertical {
                background: #c0c0c0;
                min-height: 20px;
            }
            QScrollBar::handle:vertical:hover {
                background: #a0a0a0;
            }
            QScrollBar::sub-line:vertical {
                border: none;
                background: none;
            }
            QScrollBar::add-line:vertical {
                border: none;
                background: none;
            }
            QScrollBar:horizontal {
                border: none;
                background: #f0f0f0;
                height: 10px;
                margin: 0px 0px 0px 0px;
            }
            QScrollBar::handle:horizontal {
                background: #c0c0c0;
                min-width: 20px;
            }
            QScrollBar::handle:horizontal:hover {
                background: #a0a0a0;
            }
            QScrollBar::sub-line:horizontal {
                border: none;
                background: none;
            }
            QScrollBar::add-line:horizontal {
                border: none;
                background: none;
            }
            """
        )
        food_list_layout.addWidget(scroll_area)
    
        main_content_layout.addWidget(food_list_box)

        # Edit and delete buttons
        button_box = QGroupBox(self)
        button_box.setStyleSheet('border: none;')
        button_box.setFixedSize(460, 80)
        button_layout = QHBoxLayout(button_box)
        button_layout.setAlignment(Qt.AlignTop)
        button_layout.setContentsMargins(0,0,0,0)

        change_profile_button = QPushButton('Ubah Profil', self)
        change_profile_button.setStyleSheet("""
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
        change_profile_button.setFont(set_font("regular",12))
        change_profile_button.setCursor(QCursor(Qt.PointingHandCursor))
        change_profile_button.setFixedSize(int(getWidth()*0.1), int(getHeight() * 0.065))
        change_profile_button.clicked.connect(self.edit_pet)  # Connect to edit method
        button_layout.addWidget(change_profile_button)

        delete_animal_button = QPushButton('Hapus Hewan', self)
        delete_animal_button.setStyleSheet("""
            QPushButton {
                background-color: #F277AD;
                font-weight: bold;
                border-radius: 8px;
                padding: 20px 5px;
                color : white;
                font-size: 24px;
            }

            QPushButton:hover {
                background-color: #F8B8D4;
            }
        """)
        delete_animal_button.setFont(set_font("regular",12))
        delete_animal_button.setCursor(QCursor(Qt.PointingHandCursor))
        delete_animal_button.setFixedSize(int(getWidth()*0.1), int(getHeight() * 0.065))
        delete_animal_button.clicked.connect(self.delete_pet)  # Connect to delete method
        button_layout.addWidget(delete_animal_button)

        if (getHeight() > 1080):
            delete_animal_button.setFixedSize(220, 70)    
            change_profile_button.setFixedSize(220, 70)

        main_content_layout.addWidget(button_box)

        back_button = QPushButton('Kembali Ke Beranda', self)
        back_button.setStyleSheet("""
            QPushButton {
                border : 3px solid #F277AD;
                font-weight: bold;
                border-radius: 8px;
                color : #F277AD;
            }

            QPushButton:hover {
                background-color: #F8B8D4;
                border : 3px solid #F277AD;
            }
        """)
        back_button.setFont(set_font("bold",12))
        back_button.setFixedSize(int(getWidth() * 0.4), int(getHeight() * 0.06))  
        back_button.setCursor(QCursor(Qt.PointingHandCursor))
        back_button.clicked.connect(self.back_home)
        main_content_layout.addWidget(back_button)

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

    def set_pet_details(self, pet,foods):
        """
        Set pet details in labels.
        pet is a tuple (pet_id, name, species, age, medical_record, image_data)
        """
        self.pet_id = pet[0]
        # Set general information
        title_label = self.findChild(QLabel, 'Pet Name')
        description_label = self.findChild(QLabel, 'Spesies | Umur: X Tahun')

        if title_label:
            title_label.setText(f"{pet[1]}")
        
        if description_label:
            description_label.setText(f"{pet[2]} | Umur: {pet[3]} bulan")

        # Set medical history
        mh_label = self.findChild(QLabel, 'Deskripsi Penyakit')
        if mh_label:
            mh_label.setText(pet[4])

        # Set pet image
        screen_geometry = QApplication.desktop().availableGeometry()
        
        animal_image_label = self.findChild(QLabel, "animalImageLabel")  # Find the label by object name
        if pet[5]:
            pixmap = QPixmap()
            pixmap.loadFromData(pet[5])
            animal_image_label.setPixmap(pixmap.scaled(
                int(getWidth() * 0.33),
                int(getHeight() * 0.4),
                Qt.KeepAspectRatio,
            ))
        else:
            animal_image_label.setText("No Image")

        food_list = "<ul>"
        for food in foods:
            food_list += f"<li>{food}</li>"
        food_list += "</ul>"
        self.fl_label.setText(food_list)
    
    def back_home(self):
        self.back_signal.emit()


