from PyQt5.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QApplication,
    QGroupBox,
    QLabel,
    QFrame,
    QComboBox,
    QGridLayout,
    QScrollArea

)
from PyQt5.QtCore import pyqtSignal, Qt
from components.animalCard import AnimalCard
from components.activityCard import ActivityCard


class MainView(QWidget):
    # Signals to navigate to other views
    add_pet_signal = pyqtSignal()  # Signal to switch to AddPetView
    view_pet_signal = pyqtSignal(int)  # Signal to switch to DetailPetView with pet ID
    filter_pet_signal = pyqtSignal(list)  # Signal to filter pets by food
    filter_by = []

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
            int(screen_geometry.width() * 0.1), 
            int(screen_geometry.height() * 0.1), 
            int(screen_geometry.width() * 0.1), 
            0,
        )
        main_content_widget.setStyleSheet('background-color: #F8F8F8;')
        # main_content_widget.setFixedHeight(int(screen_geometry.height() + 100) )
        main_content_layout.setAlignment(Qt.AlignTop)

        header_box = QGroupBox(self)
        header_box.setStyleSheet('border: none')
        header_box.setFixedHeight(100)
        header_layout = QHBoxLayout(header_box)

        home_label = QLabel('Beranda', self)
        home_label.setStyleSheet('font-size: 48px; color: #F277AD; font-weight: bold;')
        header_layout.addWidget(home_label)  

        add_pet_button = QPushButton('Tambah Hewan', self)
        add_pet_button.setStyleSheet('background-color: #F277AD; font-size: 18px; color: white; padding: 17px 13px; border: none; border-radius: 5px;')
        add_pet_button.clicked.connect(self.add_pet)
        add_pet_button.setFixedSize(160, 60)
        header_layout.addWidget(add_pet_button)

        main_content_layout.addWidget(header_box)

        line = QFrame()
        line.setFrameShape(QFrame.HLine)
        line.setFrameShadow(QFrame.Sunken)
        line.setStyleSheet("QFrame { background-color: #F277AD; }")
        line.setFixedWidth(int(screen_geometry.width() * 0.65))
        main_content_layout.addWidget(line)

        content_box = QWidget(self)
        content_box.setStyleSheet('border: none;')
        content_layout = QHBoxLayout(content_box)
        # content_box.setFixedHeight(int(screen_geometry.height() * 0.80))
        content_layout.setAlignment(Qt.AlignTop)

        pet_list_box = QWidget(self)
        pet_list_box.setStyleSheet('border:none;')
        # pet_list_box.setFixedWidth(int(screen_geometry.width() * 0.4))
        pet_list_layout = QVBoxLayout(pet_list_box)
        pet_list_layout.setAlignment(Qt.AlignTop)
        pet_list_layout.setContentsMargins(0,0,0,0)
        pet_list_layout.setSpacing(0)

        pet_header_box = QGroupBox(self)
        pet_header_box.setStyleSheet('border:none;')
        pet_header_box.setFixedHeight(100)
        pet_header_layout = QHBoxLayout(pet_header_box)
        pet_header_layout.setAlignment(Qt.AlignLeft)


        pet_title_label = QLabel('Daftar Hewanmu', self)
        pet_title_label.setStyleSheet('font-size: 26px; font-weight: bold; color: #1A646B; margin: 10px; margin-left: 0px;')
        pet_header_layout.addWidget(pet_title_label)

        self.filter_button = QPushButton('Filter', self)
        self.filter_button.setStyleSheet('background-color: #1A646B; font-size: 18px; color: white; padding: 17px 13px; border: none; border-radius: 5px;')
        self.filter_button.setFixedSize(80, 50)
        self.filter_button.clicked.connect(self.show_filter_menu)
        pet_header_layout.addWidget(self.filter_button)

        self.filter_combo_box = QComboBox(self)
        self.filter_combo_box.setStyleSheet('font-size: 18px; color: #1A646B; background-color: #F8F8F8; border: 2px solid #1A646B; border-radius: 5px; padding: 10px;')
        self.filter_combo_box.addItems(["Tahu", "Tempe", "Telur"])
        self.filter_combo_box.hide()
        self.filter_combo_box.activated[str].connect(self.on_filter)
        pet_header_layout.addWidget(self.filter_combo_box)
    
        pet_list_layout.addWidget(pet_header_box)

        # Create the scroll area
        scroll_area_pet = QScrollArea()
        scroll_area_pet.setWidgetResizable(True)
        scroll_area_pet.setContentsMargins(0,0,0,0)
        scroll_area_pet.setFixedHeight(int(screen_geometry.width() * 0.45))

        pet_content_list = QWidget()
        pet_content_list.setFixedWidth(int(screen_geometry.width() * 0.4))
        

        pet_content_list_layout = QGridLayout(pet_content_list)
        pet_content_list_layout.setSpacing(0)
        pet_content_list_layout.setContentsMargins(0,0,0,0)
        pet_content_list_layout.setAlignment(Qt.AlignTop)

        
        card_data = [
            {"name": "John Doe","species":"angjing" , "age": 30, "riwayat_penyakit": "Lorem ipsum dolor sit amet", "image_path": "img/meng.png"},
            {"name": "Jane Smith","species":"angjing" , "age": 25, "riwayat_penyakit": "Consectetur adipiscing elit", "image_path": "img/meng.png"},
            {"name": "Alice Johnson","species":"angjing" , "age": 35, "riwayat_penyakit": "Sed do eiusmod tempor incididunt", "image_path": "img/meng.png"},
            {"name": "John Doe","species":"angjing" , "age": 30, "riwayat_penyakit": "Lorem ipsum dolor sit amet", "image_path": "img/meng.png"},
            {"name": "Jane Smith","species":"angjing" , "age": 25, "riwayat_penyakit": "Consectetur adipiscing elit", "image_path": "img/meng.png"},
            {"name": "Alice Johnson","species":"angjing" , "age": 35, "riwayat_penyakit": "Sed do eiusmod tempor incididunt", "image_path": "img/meng.png"},
            {"name": "John Doe","species":"angjing" , "age": 30, "riwayat_penyakit": "Lorem ipsum dolor sit amet", "image_path": "img/meng.png"},
            {"name": "Jane Smith","species":"angjing" , "age": 25, "riwayat_penyakit": "Consectetur adipiscing elit", "image_path": "img/meng.png"},
            {"name": "Alice Johnson","species":"angjing" , "age": 35, "riwayat_penyakit": "Sed do eiusmod tempor incididunt", "image_path": "img/meng.png"},
            {"name": "John Doe","species":"angjing" , "age": 30, "riwayat_penyakit": "Lorem ipsum dolor sit amet", "image_path": "img/meng.png"},
            {"name": "Jane Smith","species":"angjing" , "age": 25, "riwayat_penyakit": "Consectetur adipiscing elit", "image_path": "img/meng.png"},
            {"name": "Alice Johnson","species":"angjing" , "age": 35, "riwayat_penyakit": "Sed do eiusmod tempor incididunt", "image_path": "img/meng.png"},
            {"name": "John Doe","species":"angjing" , "age": 30, "riwayat_penyakit": "Lorem ipsum dolor sit amet", "image_path": "img/meng.png"},
            {"name": "Jane Smith","species":"angjing" , "age": 25, "riwayat_penyakit": "Consectetur adipiscing elit", "image_path": "img/meng.png"},
            {"name": "Alice Johnson","species":"angjing" , "age": 35, "riwayat_penyakit": "Sed do eiusmod tempor incididunt", "image_path": "img/meng.png"},
            {"name": "John Doe","species":"angjing" , "age": 30, "riwayat_penyakit": "Lorem ipsum dolor sit amet", "image_path": "img/meng.png"},
            {"name": "Jane Smith","species":"angjing" , "age": 25, "riwayat_penyakit": "Consectetur adipiscing elit", "image_path": "img/meng.png"},
            {"name": "Alice Johnson","species":"angjing" , "age": 35, "riwayat_penyakit": "Sed do eiusmod tempor incididunt", "image_path": "img/meng.png"}
        ]

        row = 0
        col = 0
        for data in card_data:
            card = AnimalCard(**data)  # Create a CardWidget instance with the provided data
            pet_content_list_layout.addWidget(card, row, col)
            col += 1
            if col >= 3:  # After reaching the second column
                col = 0  # Reset column index
                row += 1  # Move to the next row//6
            card.clicked.connect(self.onAnimalCardClicked)

        pet_content_list.setLayout(pet_content_list_layout)

        scroll_area_pet.setWidget(pet_content_list)
        scroll_area_pet.setStyleSheet('''
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
        activity_box.setFixedWidth(int(screen_geometry.width() * 0.2))
        activity_layout = QVBoxLayout(activity_box)
        activity_layout.setAlignment(Qt.AlignTop)

        # Container aktivitas hari ini text
        activity_header_box = QGroupBox(self)
        activity_header_box.setStyleSheet('border: none;')
        activity_header_box.setFixedHeight(95)
        activity_header_layout = QHBoxLayout(activity_header_box)

        activity_title_label = QLabel('Aktivitas Hari Ini', self)
        activity_title_label.setStyleSheet('font-size: 26px; font-weight: bold; color: #1A646B; margin-top:0px;')
        activity_header_layout.addWidget(activity_title_label)

        activity_layout.addWidget(activity_header_box)

        scroll_area_activity = QScrollArea()
        scroll_area_activity.setWidgetResizable(True)
        scroll_area_activity.setContentsMargins(0,0,0,0)
        scroll_area_activity.setFixedHeight(int(screen_geometry.width() * 0.45))

        # Container untuk tiap aktivitas
        activity_content_box = QWidget(self)
        activity_content_box.setStyleSheet('border: none; background: #FFD7E0; border-radius: 10px;')
        activity_content_layout = QVBoxLayout(activity_content_box)
        activity_content_layout.setAlignment(Qt.AlignTop)
        activity_content_layout.setSpacing(20)
        activity_data_list = [
            {"activity_name": "Jalan ke Taman Oink", "time": "16.00-17.00", "pet": "Neo Woof"},
            {"activity_name": "Play fetch", "time": "17.30-18.30", "pet": "Buddy"},
            {"activity_name": "Jalan ke Taman Oink", "time": "16.00-17.00", "pet": "Neo Woof"},
            {"activity_name": "Play fetch", "time": "17.30-18.30", "pet": "Buddy"},
            {"activity_name": "Jalan ke Taman Oink", "time": "16.00-17.00", "pet": "Neo Woof"},
            {"activity_name": "Play fetch", "time": "17.30-18.30", "pet": "Buddy"},
            {"activity_name": "Jalan ke Taman Oink", "time": "16.00-17.00", "pet": "Neo Woof"},
            {"activity_name": "Play fetch", "time": "17.30-18.30", "pet": "Buddy"},
            {"activity_name": "Jalan ke Taman Oink", "time": "16.00-17.00", "pet": "Neo Woof"},
            {"activity_name": "Play fetch", "time": "17.30-18.30", "pet": "Buddy"},
            {"activity_name": "Jalan ke Taman Oink", "time": "16.00-17.00", "pet": "Neo Woof"},
            {"activity_name": "Play fetch", "time": "17.30-18.30", "pet": "Buddy"},
            {"activity_name": "Jalan ke Taman Oink", "time": "16.00-17.00", "pet": "Neo Woof"},
            {"activity_name": "Play fetch", "time": "17.30-18.30", "pet": "Buddy"},
            {"activity_name": "Jalan ke Taman Oink", "time": "16.00-17.00", "pet": "Neo Woof"},
            {"activity_name": "Play fetch", "time": "17.30-18.30", "pet": "Buddy"},
            {"activity_name": "Jalan ke Taman Oink", "time": "16.00-17.00", "pet": "Neo Woof"},
            {"activity_name": "Play fetch", "time": "17.30-18.30", "pet": "Buddy"},
            {"activity_name": "Jalan ke Taman Oink", "time": "16.00-17.00", "pet": "Neo Woof"},
            {"activity_name": "Play fetch", "time": "17.30-18.30", "pet": "Buddy"},
            {"activity_name": "Jalan ke Taman Oink", "time": "16.00-17.00", "pet": "Neo Woof"},
            {"activity_name": "Play fetch", "time": "17.30-18.30", "pet": "Buddy"},
            {"activity_name": "Jalan ke Taman Oink", "time": "16.00-17.00", "pet": "Neo Woof"},
            {"activity_name": "Play fetch", "time": "17.30-18.30", "pet": "Buddy"},
            {"activity_name": "Jalan ke Taman Oink", "time": "16.00-17.00", "pet": "Neo Woof"},
            {"activity_name": "Play fetch", "time": "17.30-18.30", "pet": "Buddy"},
            {"activity_name": "Jalan ke Taman Oink", "time": "16.00-17.00", "pet": "Neo Woof"},
            {"activity_name": "Play fetch", "time": "17.30-18.30", "pet": "Buddy"},
            {"activity_name": "Jalan ke Taman Oink", "time": "16.00-17.00", "pet": "Neo Woof"},
            {"activity_name": "Play fetch", "time": "17.30-18.30", "pet": "Buddy"},
        ]

        for activity in activity_data_list:
            
            activity_entry_card = ActivityCard(**activity)
            activity_content_layout.addWidget(activity_entry_card)
            activity_entry_card.clicked.connect(self.onActivityCardClicked)
            


        activity_content_box.setLayout(activity_content_layout)
        scroll_area_activity.setWidget(activity_content_box)
        scroll_area_activity.setStyleSheet('''
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

    def on_filter(self, text):
        if text in self.filter_by:
            self.filter_by.remove(text)
        else:
            self.filter_by.append(text)

        self.update_combo_box()

    def update_combo_box(self):
        font = self.filter_combo_box.font()
        font.setBold(False)
        for i in range(self.filter_combo_box.count()):
            if self.filter_combo_box.itemText(i) in self.filter_by:
                font.setBold(True)
                self.filter_combo_box.setItemData(i, font, Qt.FontRole)
            else:
                font.setBold(False)
                self.filter_combo_box.setItemData(i, font, Qt.FontRole)




        # # Button to add a new pet
        # self.add_pet_button = QPushButton("Add Pet")
        # self.add_pet_button.clicked.connect(self.add_pet)
        
        # # Table to display pets
        # self.pets_table = QTableWidget(0, 2)  # 2 columns: ID and Name
        # self.pets_table.setHorizontalHeaderLabels(["ID", "Name"])
        # self.pets_table.cellClicked.connect(self.view_pet)
        
        # # Add widgets to layout
        # layout.addWidget(self.add_pet_button)  # Button to add a new pet
        # layout.addWidget(self.pets_table)  # Table to list pets
        
        # self.setLayout(layout)

    def add_pet(self):
        self.add_pet_signal.emit()  # Emit signal to switch to AddPetView

    def view_pet(self, row):
        pet_id = int(self.pets_table.item(row, 0).text())  # Get pet ID from the table
        self.view_pet_signal.emit(pet_id)  # Emit signal to switch to DetailPetView

    def filter_pet(self):
        pass
        # pets = []
        
        # self.filter_pet_signal.emit(pets)

    def set_pets(self, pets):
        pass
        # self.pets_table.setRowCount(len(pets))
        # for row, pet in enumerate(pets):
        #     for col, field in enumerate(pet):
        #         item = QTableWidgetItem(str(field))
        #         self.pets_table.setItem(row, col, item)

    def set_activity(self, activities):
        pass
        # self.activities_table.setRowCount(len(activities))
        # for row, activity in enumerate(activities):
        #     for col, field in enumerate(activity):
        #         item = QTableWidgetItem(str(field))
        #         self.activities_table.setItem(row, col, item)
    # Assuming you have an instance of ActivityCard called activity_card

    def onAnimalCardClicked(self):
        clicked_card = self.sender()  # Get the instance of the card that emitted the signal
        
        # Access the properties of the clicked card and print them
        print("Name:", clicked_card.name)
        print("Species:", clicked_card.species)
        print("Age:", clicked_card.age)
        print("Riwayat Penyakit:", clicked_card.riwayat_penyakit)

    def onActivityCardClicked(self):
        clicked_card = self.sender()  # Get the instance of the card that emitted the signal
        
        # Access the properties of the clicked card and print them
        print("Activity Name:", clicked_card.activity_name)
        print("Time:", clicked_card.time)
        print("Pet:", clicked_card.pet)