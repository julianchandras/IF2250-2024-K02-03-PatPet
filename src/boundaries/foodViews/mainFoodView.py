import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QTableWidget, QTableWidgetItem, QGroupBox
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class MainFoodView(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        screen_geometry = QApplication.desktop().availableGeometry()

        main_layout = QHBoxLayout()
        main_layout.setContentsMargins(0, 0, 0, 0)

        sidebar_width = screen_geometry.width() // 6

        sidebar_widget = QWidget(self)
        sidebar_widget.setFixedWidth(sidebar_width)

        sidebar_layout = QVBoxLayout(sidebar_widget)

        sidebar_label = QLabel('Sidebar', self)
        sidebar_label.setStyleSheet('font-size: 48px; color: #1A646B; font-weight: bold')
        sidebar_label.setFont(QFont('Arial', 14))

        sidebar_layout.addWidget(sidebar_label)

        main_layout.addWidget(sidebar_widget)

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
        submit_button.clicked.connect(self.submitFoodName)
        submit_button.setFixedSize(100, 50)
        food_entry_box_layout.addWidget(submit_button)

        main_content_layout.addWidget(food_entry_box)

        food_list_label = QLabel('Daftar Makanan', self)
        food_list_label.setStyleSheet('font-size: 26px; font-weight: bold; color: #1A646B;')
        food_list_label.setContentsMargins(0, 18, 0, 6)
        main_content_layout.addWidget(food_list_label)

        self.food_table = QTableWidget(self)
        self.food_table.setColumnCount(3)
        self.food_table.setHorizontalHeaderLabels(['Nama Makanan', 'Daftar Hewan', 'Option'])
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

        self.food_animals_dict = {
            'Carrot': ['Rabbit'],
            'Apple': ['Horse', 'Monkey'],
            'Banana': ['Monkey'],
            'Fish': ['Bear', 'Eagle', 'Human'],
            'Bread': ['Human', 'Duck'],
            'Grass': ['Cow', 'Sheep', 'Horse']
        }
        
    def submitFoodName(self):
        food_name = self.food_name_input.text()
        if food_name:
            animals = self.food_animals_dict.get(food_name, [])
            animal_str = ", ".join(animals)

            row_position = self.food_table.rowCount()
            self.food_table.insertRow(row_position)
            self.food_table.setItem(row_position, 0, QTableWidgetItem(food_name))
            self.food_table.setItem(row_position, 1, QTableWidgetItem(animal_str))

        # Create a delete button for the row
        delete_button = QPushButton('Delete', self)
        delete_button.setStyleSheet('background-color: #F24E1E; font-size: 18px; color: white; padding: 10px; border-radius: 10px; margin: 150px;')
        delete_button.clicked.connect(lambda checked, row=row_position: self.deleteRow(row))
        self.food_table.setCellWidget(row_position, 2, delete_button)
        item = self.food_table.item(row_position, 1)
        item.setFlags(item.flags() & ~Qt.ItemIsEditable)

        self.food_name_input.clear()

    # Add a method to delete a row
    def deleteRow(self, row):
        self.food_table.removeRow(row)

