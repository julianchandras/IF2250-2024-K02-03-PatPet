from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import Qt

class ActivityCard(QWidget):
    def __init__(self, activity_name,time,pet,parent=None):
        super().__init__(parent)
        self.activity_name = activity_name
        self.time = time
        self.pet = pet
        self.initUI()
        
    def initUI(self):
        layout = QHBoxLayout()
        layout.setContentsMargins(0,0,0,0)

        self.card_content = QWidget(self)
        self.card_content_layout = QVBoxLayout(self.card_content)
        self.card_content.setFixedHeight(120)
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

        # activity_entry_box = QGroupBox(self)
        # activity_entry_box.setStyleSheet('border: none; background: white; border-radius: 8px;')
        # activity_entry_box.setFixedHeight(120)
        # activity_entry_layout = QVBoxLayout(activity_entry_box)

        activity_activity_name_label = QLabel(f"{self.activity_name}")
        activity_activity_name_label.setStyleSheet('font-size: 18px; font-weight: bold;')
        self.card_content_layout.addWidget(activity_activity_name_label)

        activity_time_label = QLabel(f"{self.time}")
        activity_time_label.setStyleSheet('font-size: 16px;')
        self.card_content_layout.addWidget(activity_time_label)

        activity_pet_label = QLabel(f"{self.pet}")
        activity_pet_label.setStyleSheet('font-size: 16px; background: #FFD66C')
        self.card_content_layout.addWidget(activity_pet_label)

        layout.addWidget(self.card_content)
        self.setLayout(layout)


