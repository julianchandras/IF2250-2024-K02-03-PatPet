import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QTableWidget, QTableWidgetItem, QGroupBox
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from PyQt5.QtCore import pyqtSignal
class MainFoodView(QWidget):
    add_food_signal = pyqtSignal(str)
    update_food_signal = pyqtSignal(int, str)
    delete_food_signal = pyqtSignal(int)

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        screen_geometry = QApplication.desktop().availableGeometry()

        main_layout = QHBoxLayout()
        main_layout.setContentsMargins(0, 0, 0, 0)

        main_content_widget = QWidget(self)
        main_content_layout = QVBoxLayout(main_content_widget)
        main_content_layout.setContentsMargins(115, 42, 115, 0)
        main_content_widget.setStyleSheet('background-color: #FFEAB4;')

        title_label = QLabel('Daftar Makanan', self)
        title_label.setStyleSheet('font-size: 48px; color: #1A646B; font-weight: bold;')
        title_label.setContentsMargins(0, 0, 0, 28)
        main_content_layout.addWidget(title_label)

        add_food_label = QLabel('Tambah Makanan', self)
        add_food_label.setStyleSheet('font-size: 26px; font-weight: bold; color: #1A646B;')
        add_food_label.setContentsMargins(0, 0, 0, 11)
        main_content_layout.addWidget(add_food_label)

        food_entry_box = QGroupBox('', self)
        food_entry_box.setStyleSheet("background-color: white; border-radius: 8px;")
        food_entry_box_layout = QVBoxLayout(food_entry_box)
        food_entry_box_layout.setContentsMargins(24, 30, 24, 20)

        food_name_label = QLabel('Nama Makanan', self)
        food_name_label.setStyleSheet('font-size: 18px; font-weight: bold; color: #0F172A;')
        food_name_label.setContentsMargins(0, 0, 0, 6)
        food_entry_box_layout.addWidget(food_name_label)

        self.food_name_input = QLineEdit(self)
        self.food_name_input.setStyleSheet('padding: 8px; font-size: 18px; border: 1px solid #ccc; border-radius: 5px;')
        self.food_name_input.setPlaceholderText("Masukkan nama makanan")
        self.food_name_input.setContentsMargins(0, 0, 0, 6)
        food_entry_box_layout.addWidget(self.food_name_input)

        submit_button = QPushButton('Tambah', self)
        submit_button.setStyleSheet('background-color: #1A646B; font-size: 18px; color: white; padding: 17px 13px; border: none; border-radius: 5px;')
        submit_button.clicked.connect(self.add_food)
        submit_button.setFixedSize(100, 50)
        food_entry_box_layout.addWidget(submit_button)

        main_content_layout.addWidget(food_entry_box)

        food_list_label = QLabel('Daftar Makanan', self)
        food_list_label.setStyleSheet('font-size: 26px; font-weight: bold; color: #1A646B;')
        food_list_label.setContentsMargins(0, 18, 0, 6)
        main_content_layout.addWidget(food_list_label)

        self.food_table = QTableWidget(self)
        self.food_table.setColumnCount(3)
        self.food_table.setHorizontalHeaderLabels(['Nama Makanan', 'Daftar Hewan', 'Options'])
        self.food_table.setStyleSheet('''
            QTableWidget {
                font-size: 20px;
                border-radius: 5px;
                background-color: white;
            }
            QTableWidget QHeaderView::section {
                background-color: #D9D9D9;
                color: #1A646B;
                font-size: 20px;
                font-weight: bold;
                padding: 8px; 
                width: 432px;
                height: 74px;
                border-radius: 11px;
            }
            QTableWidget::item {
                background-color: #D9D9D9;
                color: #1A646B;
                padding: 16px; 
                margin: 5px 0px 0px 0px;
            }
        ''')
        self.food_table.setFixedWidth(int((screen_geometry.width() * 0.7)))
        self.food_table.verticalHeader().setDefaultSectionSize(74) 
        self.food_table.verticalHeader().setVisible(False)

        self.food_table.resizeColumnsToContents()
        main_content_layout.addWidget(self.food_table)
    
        main_layout.addWidget(main_content_widget)

        self.setLayout(main_layout)


    # Add a method to delete a row
    def deleteRow(self, row):
        self.food_table.removeRow(row)

    def set_food(self, food):
        # Set row count based on the number of items in the dictionary
        self.food_table.setRowCount(len(food))

        # Loop through the food dictionary and populate the table
        for i, (food_name, food_data) in enumerate(food.items()):
            # Set the food name and food ID
            food_id = food_data[0]  # First element of the tuple is the ID
            food_eater = ", ".join(food_data[1])  # Second element is a list of animals
            
            # Create a table item for the food name and list of animals
            self.food_table.setItem(i, 0, QTableWidgetItem(food_name))  # Set food name
            self.food_table.setItem(i, 1, QTableWidgetItem(food_eater))  # Set list of animals

            # Create a widget to contain the buttons
            option_widget = QWidget(self)  # Create a container widget
            option_layout = QHBoxLayout(option_widget)  # Create a horizontal layout
            option_layout.setContentsMargins(0, 0, 0, 0)  # Optional: Reduce margins
            option_layout.setSpacing(10)  # Optional: Set spacing between buttons

            # Create the buttons and connect them to the signals
            update_button = QPushButton("Update", self)
            update_button.setStyleSheet("background-color: #1A646B; font-size: 18px; color: white; padding: 10px; border-radius: 10px;")
            update_button.clicked.connect(lambda checked, row=i, id=food_id: self.update_food_signal.emit(id, self.food_table.item(row, 0).text()))
            option_layout.addWidget(update_button)

            delete_button = QPushButton("Delete", self)
            delete_button.setStyleSheet("background-color: #F24E1E; font-size: 18px; color: white; padding: 10px; border-radius: 10px;")
            delete_button.clicked.connect(lambda checked, id=food_id: self.delete_food_signal.emit(id))
            option_layout.addWidget(delete_button)

            option_widget.setLayout(option_layout)  # Set the layout for the widget

            # Add the option widget to the table
            self.food_table.setCellWidget(i, 2, option_widget)

            # Make the food ID cell not editable
            item = self.food_table.item(i, 1)
            if item:
                item.setFlags(item.flags() & ~Qt.ItemIsEditable)

    def add_food(self):
        food_name = self.food_name_input.text()
        if food_name:
            self.add_food_signal.emit(food_name)
            self.food_name_input.clear()
    
    def update_food(self, id):
        food_name = self.food_name_input.text()
        if food_name:
            self.update_food_signal.emit(id, food_name)
            self.food_name_input.clear()

