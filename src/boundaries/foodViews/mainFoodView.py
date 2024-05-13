
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QTableWidget, QTableWidgetItem, QGroupBox, QFrame
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QCursor
from utils.font import get_font

class MainFoodView(QWidget):
    
    add_food_signal = pyqtSignal(str)
    update_food_signal = pyqtSignal(int, str)
    delete_food_signal = pyqtSignal(int)

    def __init__(self):
        super().__init__()
        self.original_food_data = {}
        self.initUI()


    def initUI(self):
        screen_geometry = QApplication.desktop().availableGeometry()

        main_layout = QHBoxLayout()
        main_layout.setContentsMargins(0, 0, 0, 0)

        main_content_widget = QWidget(self)
        main_content_layout = QVBoxLayout(main_content_widget)
        main_content_layout.setContentsMargins(115, 42, 115, 42)
        main_content_widget.setStyleSheet('background-color: #FFEAB4; border:none;')

        title_label = QLabel('Daftar Makanan', self)
        title_label.setStyleSheet('font-size: 72px; color: #1A646B; font-weight: bold;')
        title_label.setFont(get_font("bold"))
        title_label.setContentsMargins(0, 0, 0, 28)
        main_content_layout.addWidget(title_label)

        line_frame = QFrame(self)
        line_frame.setFrameShape(QFrame.HLine)
        line_frame.setFrameShadow(QFrame.Sunken)
        line_frame.setLineWidth(2)
        line_frame.setMidLineWidth(4)
        line_frame.setStyleSheet("border: 2px solid #1A646B;")
        line_frame.setContentsMargins(0, 0, 0, 30)

        main_content_layout.addWidget(line_frame)

        add_food_label = QLabel('Tambah Makanan', self)
        add_food_label.setStyleSheet('font-size: 48px; font-weight: bold; color: #1A646B;')
        add_food_label.setFont(get_font("bold"))
        add_food_label.setContentsMargins(0, 0, 0, 11)
        main_content_layout.addWidget(add_food_label)

        food_entry_box = QGroupBox('', self)
        food_entry_box.setStyleSheet("background-color: white; border-radius: 8px; border:none;")
        food_entry_box_layout = QVBoxLayout(food_entry_box)
        food_entry_box_layout.setContentsMargins(24, 30, 24, 20)

        food_name_label = QLabel('Nama Makanan', self)
        food_name_label.setStyleSheet('font-size: 32px; font-weight: bold; color: #0F172A;')
        food_name_label.setFont(get_font("bold"))
        food_name_label.setContentsMargins(0, 0, 0, 6)
        food_entry_box_layout.addWidget(food_name_label)

        self.food_name_input = QLineEdit(self)
        self.food_name_input.setStyleSheet('padding: 8px; font-size: 24px; border: 1px solid #ccc; border-radius: 5px;')
        self.food_name_input.setPlaceholderText("Masukkan nama makanan")
        self.food_name_input.setFont(get_font("regular"))
        self.food_name_input.setContentsMargins(0, 0, 0, 6)
        food_entry_box_layout.addWidget(self.food_name_input)

        submit_button = QPushButton('Tambah', self)
        submit_button.setStyleSheet("""
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
        submit_button.setFont(get_font("regular"))
        submit_button.setCursor(QCursor(Qt.PointingHandCursor))
        submit_button.clicked.connect(self.add_food)
        submit_button.setFixedSize(140, 70)
        food_entry_box_layout.addWidget(submit_button)

        main_content_layout.addWidget(food_entry_box)

        food_list_label = QLabel('Daftar Makanan', self)
        food_list_label.setStyleSheet('font-size: 32px; font-weight: bold; color: #1A646B;')
        food_list_label.setFont(get_font("regular"))
        food_list_label.setContentsMargins(0, 10, 0, 0)
        main_content_layout.addWidget(food_list_label)

        note_label = QLabel("Tekan nama makanan untuk mengubah")
        note_label.setStyleSheet('font-size: 24px; color: #1A646B;')
        note_label.setFont(get_font("regular"))
        main_content_layout.addWidget(note_label)

        self.food_table = QTableWidget(self)
        self.food_table.setFont(get_font("regular"))
        self.food_table.setColumnCount(3)
        self.food_table.setHorizontalHeaderLabels(['Nama Makanan', 'Daftar Hewan', 'Options'])
        self.food_table.horizontalHeader().setFont(get_font("bold"))
        self.food_table.setStyleSheet('''
            QTableWidget {
                font-size: 26px;
                border-radius: 5px;
                background-color: white;
            }
            QTableWidget QHeaderView::section {
                background-color: #D9D9D9;
                color: #1A646B;
                font-size: 32px;
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
        self.food_table.setFixedWidth(int((screen_geometry.width() * 0.755)))
        self.food_table.setFixedHeight(int((screen_geometry.width() * 0.385)))
        self.food_table.verticalHeader().setDefaultSectionSize(95)
        self.food_table.horizontalHeader().setDefaultSectionSize(int((screen_geometry.width() * 0.755) // 3))
        self.food_table.verticalHeader().setVisible(False)
        main_content_layout.addWidget(self.food_table)
    
        main_layout.addWidget(main_content_widget)

        self.setLayout(main_layout)
        self.food_table.viewport().setCursor(Qt.PointingHandCursor)


    # Add a method to delete a row
    def deleteRow(self, row):
        self.food_table.removeRow(row)

    def set_food(self, food):
        # Set row count based on the number of items in the dictionary
        self.food_table.setRowCount(len(food))

        self.original_food_data = food.copy()

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
            option_widget.setStyleSheet("background-color :#D4D4D4; ")

            # Create the buttons and connect them to the signals
            update_button = QPushButton("Simpan Update", self)
            # update_button.setStyleSheet("background-color: #1A646B; font-size: 18px; color: white; padding: 10px; border-radius: 10px;")
            update_button.setStyleSheet("""
            QPushButton {
                background-color: #1A646B;
                font-weight: bold;
                border-radius: 8px;
                padding: 15px 5px;
                color : white;
                font-size : 20px;
                
            }

            QPushButton:hover {
                background-color: #6E9DA1;
            }
        """)
            update_button.setFont(get_font("regular"))
            update_button.setCursor(QCursor(Qt.PointingHandCursor))
            update_button.setFixedHeight(55)
            update_button.clicked.connect(lambda checked, row=i, id=food_id: self.update_food_signal.emit(id, self.food_table.item(row, 0).text()))
            option_layout.addWidget(update_button)

            delete_button = QPushButton("Hapus", self)
            delete_button.setStyleSheet("""
                QPushButton {
                    background-color: #F277AD;
                    font-weight: bold;
                    border-radius: 8px;
                    padding: 15px 5px;
                    color : white;
                    font-size : 20px;
                    
                }

                QPushButton:hover {
                    background-color: #F8B8D4;
                }
            """)
            delete_button.setFont(get_font("regular"))
            delete_button.setCursor(QCursor(Qt.PointingHandCursor))
            delete_button.setFixedHeight(55)
            delete_button.clicked.connect(lambda checked, id=food_id: self.delete_food_signal.emit(id))
            option_layout.addWidget(delete_button)

            option_widget.setLayout(option_layout)  # Set the layout for the widget

            # Add the option widget to the table
            self.food_table.setCellWidget(i, 2, option_widget)

            # Make the food ID cell not editable
            item = self.food_table.item(i, 1)
            if item:
                item.setFlags(item.flags() & ~Qt.ItemIsEditable)

    def revert_food(self):
        self.set_food(self.original_food_data)

    def add_food(self):
        food_name = self.food_name_input.text()
        if food_name:
            self.add_food_signal.emit(food_name)
            self.food_name_input.clear()
    
    def clear_input(self):
        self.food_name_input.clear()


