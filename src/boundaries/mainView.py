from PyQt5.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QApplication,
    QGroupBox,
    QLabel,
    QFrame,
    QGridLayout,
    QScrollArea
)
from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtGui import QCursor
from components.animalCard import AnimalCard
from components.activityCard import ActivityCard
from components.checkableCombobox import CheckableComboBox
from utils.font import *
from utils.screensize import *


class MainView(QWidget):
    # Signals to navigate to other views
    add_pet_signal = pyqtSignal()  # Signal to switch to AddPetView
    view_pet_signal = pyqtSignal(int)  # Signal to switch to DetailPetView with pet ID
    filter_pet_signal = pyqtSignal(list)  # Signal to filter pets by food

    def __init__(self):
        super().__init__()
        self.setup_ui()  # Initialize the user interface
    
    def setup_ui(self):
        screen_geometry = QApplication.desktop().availableGeometry()

        self.setWindowTitle('Detail Hewan')


        main_layout = QHBoxLayout()
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        # Main content
        main_content_widget = QWidget(self)
        main_content_layout = QVBoxLayout(main_content_widget)
        main_content_layout.setContentsMargins(
            int(getWidth() * 0.1), 
            int(getHeight() * 0.1), 
            int(getWidth() * 0.1), 
            int(getHeight() * 0.04),
        )
        main_content_widget.setStyleSheet('background-color: #F8F8F8;')
        
       
        header_box = QGroupBox(self)
        header_box.setStyleSheet('border: none')
        header_box.setFixedHeight(int(getHeight() * 0.075))
        header_layout = QHBoxLayout(header_box)

        home_label = QLabel('Beranda', self)
        home_label.setStyleSheet('color: #F277AD; font-weight: 900;')
        home_label.setFont(set_font("bold",24))
        header_layout.addWidget(home_label)  

        add_pet_button = QPushButton('Tambah Hewan', self)
        add_pet_button.setStyleSheet("""
            QPushButton {
                background-color: #F277AD;
                font-weight: bold;
                border-radius: 8px;
                color : white;
            }

            QPushButton:hover {
                background-color: #F8B8D4;
            }
        """)
        add_pet_button.setFont(set_font("regular",12))
        add_pet_button.setCursor(QCursor(Qt.PointingHandCursor))
        add_pet_button.clicked.connect(self.add_pet)
        add_pet_button.setFixedSize(int(getWidth() * 0.12),int(getHeight() * 0.0625))
        header_layout.addWidget(add_pet_button)

        main_content_layout.addWidget(header_box)

        line = QFrame()
        line.setFrameShape(QFrame.HLine)
        line.setFrameShadow(QFrame.Sunken)
        line.setStyleSheet("QFrame { background-color: #F277AD; }")
        line.setFixedWidth(int(getWidth() * 0.65))
        main_content_layout.addWidget(line)

        content_box = QWidget(self)
        content_box.setStyleSheet('border: 1px solid red;')
        content_layout = QHBoxLayout(content_box)
        content_layout.setAlignment(Qt.AlignTop | Qt.AlignLeft)
        content_layout.setContentsMargins(0,0,0,0)

        pet_list_box = QWidget(self)
        pet_list_box.setStyleSheet('border:none')
        pet_list_layout = QVBoxLayout(pet_list_box)
        pet_list_layout.setAlignment(Qt.AlignTop)
        pet_list_layout.setContentsMargins(0,0,0,0)
        pet_list_layout.setSpacing(0)

        pet_header_box = QGroupBox(self)
        pet_header_box.setStyleSheet('border:none;')
        pet_header_box.setFixedHeight(int(getHeight() * 0.075))
        pet_header_layout = QHBoxLayout(pet_header_box)
        pet_header_layout.setContentsMargins(0,0,0,0)
        pet_header_layout.setAlignment(Qt.AlignLeft)


        pet_title_label = QLabel('Daftar Hewanmu', self)
        pet_title_label.setStyleSheet('font-weight: bold; color: #1A646B; margin: 10px; margin-left: 0px;')
        pet_title_label.setFont(set_font("regular",16))
        pet_header_layout.addWidget(pet_title_label)

        self.filter_button = QPushButton('Filter', self)
        self.filter_button.setStyleSheet("""
            QPushButton {
                background-color: #1A646B;
                font-weight: bold;
                border-radius: 8px;
                padding: 20px 5px;
                color : white;
            }

            QPushButton:hover {
                background-color: #6E9DA1;
            }
        """)
        self.filter_button.setFont(set_font("regular",12))
        self.filter_button.setCursor(QCursor(Qt.PointingHandCursor))
        if (getHeight() > 1080):
            self.filter_button.setFixedSize(int(getWidth() * 0.05),int(getHeight() * 0.045))
        else:
            self.filter_button.setFixedSize(int(getWidth() * 0.05),int(getHeight() * 0.062))
        self.filter_button.clicked.connect(self.show_filter_menu)
        pet_header_layout.addWidget(self.filter_button)

        self.filter_combo_box = CheckableComboBox()
        self.filter_combo_box.setStyleSheet("""QComboBox { color: #1A646B; background-color: #F8F8F8; border: 2px solid #1A646B; border-radius: 5px; padding: 10px;}
                                            QComboBox::drop-down {
                                            border: 0px;
                                            }
                                            QComboBox::down-arrow {
                                                image: url(img/chevron-down.png);
                                                width: 30px;
                                                height: 30px;
                                                margin-right: 20px;
                                            }
                                            QLineEdit {
                                                background-color: #F8F8F8;

                                            }
                                            """)
        if (getHeight() > 1080):
            self.filter_combo_box.setFixedSize(int(getWidth() * 0.12), int(getHeight() * 0.05))
        else:
            self.filter_combo_box.currentTextChanged.connect(self.filter_pet)
        self.filter_combo_box.hide()
        
        
        pet_header_layout.addWidget(self.filter_combo_box)
    
        pet_list_layout.addWidget(pet_header_box)

        # Create the scroll area
        scroll_area_pet = QScrollArea()
        scroll_area_pet.setWidgetResizable(True)
        scroll_area_pet.setContentsMargins(0,0,0,0)
        scroll_area_pet.setFixedHeight(int(getHeight() * 0.7))
        # scroll_area_pet.setFixedWidth(int(getWidth() * 0.45))

        pet_content_list = QWidget()
        pet_content_list.setFixedWidth(int(getWidth() * 0.35))
        

        self.pet_content_list_layout = QGridLayout(pet_content_list)
        self.pet_content_list_layout.setSpacing(0)
        self.pet_content_list_layout.setContentsMargins(0,0,0,0)
        self.pet_content_list_layout.setAlignment(Qt.AlignTop)

        pet_content_list.setLayout(self.pet_content_list_layout)

        scroll_area_pet.setWidget(pet_content_list)
        scroll_area_pet.setStyleSheet('''
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
        ''')
        pet_list_layout.addWidget(scroll_area_pet)
        # pet_list_layout.addWidget(pet_content_list)


        content_layout.addWidget(pet_list_box)

        # Container utama aktivitas
        activity_box = QWidget(self)
        activity_box.setStyleSheet('border: none;')
        activity_box.setFixedWidth(int(getWidth() * 0.25))
        activity_layout = QVBoxLayout(activity_box)
        activity_layout.setAlignment(Qt.AlignTop)

        # Container aktivitas hari ini text
        activity_header_box = QGroupBox(self)
        activity_header_box.setStyleSheet('border: none;')
        activity_header_box.setFixedHeight(int(getHeight() * 0.085))
        activity_header_layout = QHBoxLayout(activity_header_box)
        activity_header_layout.setAlignment(Qt.AlignTop)

        activity_title_label = QLabel('Aktivitas Hari Ini', self)
        activity_title_label.setStyleSheet('font-weight: bold; color: #1A646B; margin: 10px; margin-left: 0px;')
        activity_title_label.setFont(set_font("regular",16))
        activity_header_layout.addWidget(activity_title_label)

        activity_layout.addWidget(activity_header_box)

        scroll_area_activity = QScrollArea()
        scroll_area_activity.setWidgetResizable(True)
        scroll_area_activity.setContentsMargins(0,0,0,0)
        scroll_area_activity.setFixedHeight(int(getWidth() * 0.375))

        # Container untuk tiap aktivitas
        activity_content_box = QWidget(self)
        activity_content_box.setStyleSheet('border: none; background: #FFD7E0; border-radius: 10px;')
        self.activity_content_layout = QVBoxLayout(activity_content_box)
        self.activity_content_layout.setAlignment(Qt.AlignTop)
        self.activity_content_layout.setSpacing(int(getHeight() * 0.01))
            
        activity_content_box.setLayout(self.activity_content_layout)
        scroll_area_activity.setWidget(activity_content_box)
        scroll_area_activity.setStyleSheet('''
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
        ''')
        activity_layout.addWidget(scroll_area_activity)

        content_layout.addWidget(activity_box)

        main_content_layout.addWidget(content_box)

        main_layout.addWidget(main_content_widget)

        self.setLayout(main_layout)

    def show_filter_menu(self):
        # Show the filter dropdown menu
        self.filter_combo_box.show()

    def hide_filter_menu(self):
        # Hide the filter dropdown menu
        self.filter_combo_box.hide()


    def add_pet(self):
        self.add_pet_signal.emit()  # Emit signal to switch to AddPetView

    def filter_pet(self):
        self.filter_pet_signal.emit(self.filter_combo_box.currentData())

    def set_pets(self, pets):
        layout = self.pet_content_list_layout
        self.clear_layout(layout)
        row = 0
        col = 0
        for data in pets:
            card = AnimalCard(pet_id = data[0], name=data[1], age=data[3], species=data[2], riwayat_penyakit=data[4], image_path=data[5])  # Create a CardWidget instance with the provided data
            self.pet_content_list_layout.addWidget(card, row, col)
            col += 1
            if (getHeight() > 1080):
                if col >= 3:  # After reaching the second column
                    col = 0  # Reset column index
                    row += 1  # Move to the next row//6
            else:
                if col == 2:  # After reaching the second column
                    col = 0  # Reset column index
                    row += 1  # Move to the next row//6
           
            card.clicked.connect(self.onAnimalCardClicked)

    def set_food(self,food):
        self.filter_combo_box.clear()
        self.filter_combo_box.addItems(food)
        
    def set_activities(self, activities):
        
        layout = self.activity_content_layout
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()
            else:
                sublayout = item.layout()
                if sublayout:
                    self.clear_layout(sublayout)

        for activity in activities:
            activity_card = ActivityCard(activity_name=activity[1], time=activity[3]+"-"+activity[4], pet=activity[6])
            self.activity_content_layout.addWidget(activity_card)

    def onAnimalCardClicked(self, pet_id):
        # Get the instance of the card that emitted the signal
        self.view_pet_signal.emit(pet_id)

    def onActivityCardClicked(self):
        clicked_card = self.sender()  # Get the instance of the card that emitted the signal
        # Access the properties of the clicked card and print them
        print("Activity Name:", clicked_card.activity_name)
        print("Time:", clicked_card.time)
        print("Pet:", clicked_card.pet)

    def clear_layout(self, layout):
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()
            else:
                self.clear_layout(item.layout())

    def clear_input(self):
        for index in range(self.filter_combo_box.count()):
            self.filter_combo_box.setCheckState(index, Qt.Unchecked)
        self.filter_combo_box.hide()
    
    