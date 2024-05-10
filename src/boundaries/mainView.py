from PyQt5.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QTableWidget,
    QTableWidgetItem,
    QApplication,
    QGroupBox,
    QLabel,
    QFrame,
    QComboBox,
    QListWidget,
    QStyledItemDelegate,
    QStyle,
    QAbstractItemView
)
from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtGui import QFont

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
        self.showFullScreen()

        main_layout = QHBoxLayout()
        main_layout.setContentsMargins(0, 0, 0, 0)

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
        main_content_widget.setFixedHeight(screen_geometry.height())

        header_box = QGroupBox(self)
        header_box.setStyleSheet('border: none')
        header_box.setFixedHeight(100)
        header_layout = QHBoxLayout(header_box)

        home_label = QLabel('Beranda', self)
        home_label.setStyleSheet('font-size: 48px; color: #F277AD; font-weight: bold;')
        header_layout.addWidget(home_label)  

        add_pet_button = QPushButton('Tambah Hewan', self)
        add_pet_button.setStyleSheet('background-color: #F277AD; font-size: 18px; color: white; padding: 17px 13px; border: none; border-radius: 5px;')
        add_pet_button.setFixedSize(160, 60)
        header_layout.addWidget(add_pet_button)

        main_content_layout.addWidget(header_box)

        line = QFrame()
        line.setFrameShape(QFrame.HLine)
        line.setFrameShadow(QFrame.Sunken)
        line.setStyleSheet("QFrame { background-color: #F277AD; }")
        line.setFixedWidth(int(screen_geometry.width() * 0.65))
        main_content_layout.addWidget(line)

        content_box = QGroupBox(self)
        content_box.setStyleSheet('border: none;')
        content_layout = QHBoxLayout(content_box)

        pet_list_box = QGroupBox(self)
        pet_list_box.setStyleSheet('border: none;')
        pet_list_box.setFixedWidth(int(screen_geometry.width() * 0.45))
        pet_list_layout = QVBoxLayout(pet_list_box)

        pet_header_box = QGroupBox(self)
        pet_header_box.setStyleSheet('border: none;')
        pet_header_box.setFixedHeight(100)
        pet_header_layout = QHBoxLayout(pet_header_box)

        pet_title_label = QLabel('Daftar Hewanmu', self)
        pet_title_label.setStyleSheet('font-size: 26px; font-weight: bold; color: #1A646B')
        pet_header_layout.addWidget(pet_title_label)

        self.filter_button = QPushButton('Filter', self)
        self.filter_button.setStyleSheet('background-color: #1A646B; font-size: 18px; color: white; padding: 17px 13px; border: none; border-radius: 5px;')
        self.filter_button.setFixedSize(80, 50)
        self.filter_button.clicked.connect(self.show_filter_menu)
        pet_header_layout.addWidget(self.filter_button)

        self.filter_combo_box = QComboBox(self)
        self.filter_combo_box.setStyleSheet('font-size: 18px; color: #1A646B; background-color: #F8F8F8; border: 2px solid #1A646B; border-radius: 5px; padding: 5px;')
        self.filter_combo_box.addItems(["Tahu", "Tempe", "Telur"])
        self.filter_combo_box.hide()
        self.filter_combo_box.activated[str].connect(self.on_filter)
        pet_header_layout.addWidget(self.filter_combo_box)
    
        pet_list_layout.addWidget(pet_header_box)

        content_layout.addWidget(pet_list_box)

        activity_box = QGroupBox(self)
        activity_box.setStyleSheet('border: none;')
        activity_box.setFixedWidth(int(screen_geometry.width() * 0.2))
        activity_layout = QVBoxLayout(activity_box)

        activity_header_box = QGroupBox(self)
        activity_header_box.setStyleSheet('border: none;')
        activity_header_box.setFixedHeight(50)
        activity_header_layout = QHBoxLayout(activity_header_box)

        activity_title_label = QLabel('Aktivitas Hari Ini', self)
        activity_title_label.setStyleSheet('font-size: 26px; font-weight: bold; color: #1A646B')
        activity_header_layout.addWidget(activity_title_label)

        activity_layout.addWidget(activity_header_box)

        activity_content_box = QGroupBox(self)
        activity_content_box.setStyleSheet('border: none; background: #FFD7E0; border-radius: 8px;')
        activity_content_layout = QVBoxLayout(activity_content_box)

        for i in range(3):
            activity_entry_box = QGroupBox(self)
            activity_entry_box.setStyleSheet('border: none; background: white; border-radius: 8px;')
            activity_entry_box.setFixedHeight(120)
            activity_entry_layout = QVBoxLayout(activity_entry_box)

            activity_name_label = QLabel('Jalan ke Taman Oink', self)
            activity_name_label.setStyleSheet('font-size: 18px; font-weight: bold;')
            activity_entry_layout.addWidget(activity_name_label)

            activity_time_label = QLabel('16.00-17.00', self)
            activity_time_label.setStyleSheet('font-size: 16px;')
            activity_entry_layout.addWidget(activity_time_label)

            activity_pet_label = QLabel('Neo Woof', self)
            activity_pet_label.setStyleSheet('font-size: 16px; background: #FFD66C')
            activity_entry_layout.addWidget(activity_pet_label)

            activity_content_layout.addWidget(activity_entry_box)

        activity_layout.addWidget(activity_content_box)

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

    # def add_pet(self):
    #     self.add_pet_signal.emit()  # Emit signal to switch to AddPetView

    # def view_pet(self, row):
    #     pet_id = int(self.pets_table.item(row, 0).text())  # Get pet ID from the table
    #     self.view_pet_signal.emit(pet_id)  # Emit signal to switch to DetailPetView

    # def filter_pet(self):
    #     pets = []
        
    #     self.filter_pet_signal.emit(pets)

    # def set_pets(self, pets):
    #     self.pets_table.setRowCount(len(pets))
    #     for row, pet in enumerate(pets):
    #         for col, field in enumerate(pet):
    #             item = QTableWidgetItem(str(field))
    #             self.pets_table.setItem(row, col, item)

    # def set_activity(self, activities):
    #     self.activities_table.setRowCount(len(activities))
    #     for row, activity in enumerate(activities):
    #         for col, field in enumerate(activity):
    #             item = QTableWidgetItem(str(field))
    #             self.activities_table.setItem(row, col, item)
