from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QSizePolicy, QFrame, QGraphicsDropShadowEffect
from PyQt5.QtGui import QPixmap, QCursor, QColor
from PyQt5.QtCore import Qt, pyqtSignal
from utils.font import get_font

class AnimalCard(QWidget):
    clicked = pyqtSignal(int)
    
    def __init__(self, pet_id, name, species, age, riwayat_penyakit, image_path, parent=None):
        super().__init__(parent)
        self.pet_id = pet_id
        self.name = name
        self.species = species
        self.age = age
        self.riwayat_penyakit = riwayat_penyakit
        self.image_path = image_path
        
        self.initUI()
        
    def initUI(self):
        layout = QHBoxLayout()

        # Card Content
        self.card_content = QWidget(self)
        self.card_content_layout = QVBoxLayout(self.card_content)
        self.card_content_layout.setContentsMargins(0, 0, 0, 0)
        self.card_content_layout.setSpacing(0)
        self.card_content_layout.setAlignment(Qt.AlignTop)
        self.card_content.setFixedSize(325, 375)
        
        # Set style sheet for the card
        self.card_content.setStyleSheet('''
            QWidget {
                background-color: #ffffff;  
                border-radius: 25px;
                margin: 0px;
                color : #1A646B;
            }
        ''')

        # Create QLabel for image
        self.image_label = QLabel()
        pixmap = QPixmap()
        pixmap.loadFromData(self.image_path)
        if not pixmap.isNull():  # Check if pixmap is valid
            pixmap = pixmap.scaledToWidth(325)  # Adjust the width to match the card content width
            self.image_label.setPixmap(pixmap)
            self.image_label.setAlignment(Qt.AlignCenter)
            self.image_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
            self.image_label.setStyleSheet("border-radius: 25px;")
            self.card_content_layout.addWidget(self.image_label)
            self.card_content_layout.setSpacing(0)
        
            # Create QLabel for name
            self.name_label = QLabel(f"{self.name}")
            self.name_label.setFont(get_font("bold"))
            self.name_label.setStyleSheet("""
                background-color: transparent; 
                margin-left: 10px; 
                margin-top: 10px;
                margin-bottom: 5px;
                padding: 0px;    
                font-size: 28px;
                font-weight: bold;
            """)  
            self.card_content_layout.addWidget(self.name_label)
            
            line_frame = QFrame(self)
            line_frame.setFrameShape(QFrame.HLine)
            line_frame.setFrameShadow(QFrame.Sunken)
            line_frame.setLineWidth(2)
            line_frame.setMidLineWidth(4)
            line_frame.setStyleSheet("border: 2px solid #D4D4D4;")
            line_frame.setFixedWidth(320)
            line_frame.setContentsMargins(0, 0, 0, 10)

            line_layout = QHBoxLayout()
            line_layout.addWidget(line_frame)
            line_layout.setAlignment(Qt.AlignCenter)

            self.card_content_layout.addLayout(line_layout)

            self.species_age_label = QLabel(f"{self.species} | {self.age}")
            self.species_age_label.setStyleSheet("background-color: transparent;margin-left: 10px;padding: 0px; margin-top:10px")
            self.species_age_label.setFont(get_font("regular"))
            self.card_content_layout.addWidget(self.species_age_label)

            riwayat_title_label = QLabel("Riwayat Kesehatan")
            riwayat_title_label.setFont(get_font("bold"))
            riwayat_title_label.setStyleSheet("""
                background-color: transparent;
                margin-left: 10px;
                padding: 0px;
                font-size: 24px;
                font-weight: bold;
            """)
            self.card_content_layout.addWidget(riwayat_title_label)
            
            # Create QLabel for additional info
            if len(self.riwayat_penyakit) > 25:
                self.riwayat_penyakit = self.riwayat_penyakit[:25] + "..." 

            self.info = QLabel(f"{self.riwayat_penyakit}")
            self.info.setStyleSheet("background-color: transparent;margin-left: 10px; margin-bottom:20px;padding: 0px;") 
            self.info.setFont(get_font("regular"))

            shadow = QGraphicsDropShadowEffect(self)
            shadow.setOffset(0, 4)
            shadow.setBlurRadius(50)
            shadow.setColor(QColor(0, 0, 0, 15))
            self.setGraphicsEffect(shadow)
            self.card_content_layout.addWidget(self.info)

        else:
            print("Error: Unable to load image.")

        # Add the card content to the main layout
        layout.addWidget(self.card_content)
        self.setLayout(layout)
        
    def mousePressEvent(self, event):
        self.clicked.emit(self.pet_id)
    
    def enterEvent(self, event):
        QApplication.setOverrideCursor(QCursor(Qt.PointingHandCursor))
    
    def leaveEvent(self, event):
        QApplication.restoreOverrideCursor()