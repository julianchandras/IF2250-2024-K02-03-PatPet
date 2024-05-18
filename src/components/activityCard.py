from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import Qt, pyqtSignal
from utils.font import *
from utils.screensize import *

class ActivityCard(QWidget):
    clicked = pyqtSignal()

    def __init__(self, activity_name, time, pet, parent=None):
        super().__init__(parent)
        self.activity_name = activity_name
        self.time = time
        self.pet = pet
        self.initUI()

    def initUI(self):
        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)

        self.card_content = QWidget(self)
        self.card_content_layout = QVBoxLayout(self.card_content)
        if (getHeight() > 1080):
            self.card_content.setFixedHeight(int(getHeight() * 0.12))
        else:
            self.card_content.setFixedHeight(int(getHeight() * 0.16))
        self.card_content_layout.setSpacing(5)
        self.card_content_layout.setAlignment(Qt.AlignTop)

        # Set style sheet for the card
        self.card_content.setStyleSheet('''
            QWidget {
                background-color: #ffffff;  
                border-radius: 10px;
                margin: 0px;
                color : #1A646B;
                border: none;
            }
        ''')

        activity_activity_name_label = QLabel(f"{self.activity_name}")
        activity_activity_name_label.setStyleSheet('font-weight: bold;')
        activity_activity_name_label.setFont(set_font("Bold",14))
        self.card_content_layout.addWidget(activity_activity_name_label)

        activity_time_label = QLabel(f"{self.time}")
        activity_time_label.setFont(set_font("regular",12))
        self.card_content_layout.addWidget(activity_time_label)

        activity_pet_label = QLabel(f"{self.pet}")
        activity_pet_label.setStyleSheet('background: #FFD66C; border-radius:8px;')
        activity_pet_label.setFont(set_font("regular",12))
        self.card_content_layout.addWidget(activity_pet_label)

        layout.addWidget(self.card_content)
        self.setLayout(layout)

    def mousePressEvent(self, event):
        self.clicked.emit()
        

    

    
