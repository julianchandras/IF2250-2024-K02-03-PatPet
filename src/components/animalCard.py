import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QSizePolicy,QFrame
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

class CardWidget(QWidget):
    def __init__(self, name, species, age, riwayat_penyakit, image_path, parent=None):
        super().__init__(parent)
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
        self.card_content.setFixedSize(350, 400)
        
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
        pixmap = QPixmap(self.image_path)
        if not pixmap.isNull():  # Check if pixmap is valid
            pixmap = pixmap.scaledToWidth(350)  # Adjust the width to match the card content width
            self.image_label.setPixmap(pixmap)
            self.image_label.setAlignment(Qt.AlignCenter)
            self.image_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
            self.image_label.setStyleSheet("border-radius: 25px;")
            self.card_content_layout.addWidget(self.image_label)
        
            # Create QLabel for name
            self.name_label = QLabel(f"{self.name}")
            self.name_label.setStyleSheet("""
                background-color: transparent; 
                margin-left: 10px; 
                margin-top: 10px;
                margin-bottom: 15px;  /* Set top margin to 0 */
                padding: 0px;     /* Set padding to 0 */
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
            line_frame.setFixedWidth(325)
            line_frame.setContentsMargins(0, 0, 0, 30)

            line_layout = QHBoxLayout()
            line_layout.addWidget(line_frame)
            line_layout.setAlignment(Qt.AlignCenter)


            self.card_content_layout.addLayout(line_layout)

            self.species_age_label = QLabel(f"{self.species} | {self.age}")
            self.species_age_label.setStyleSheet("background-color: transparent;margin-left: 10px;margin-bottom: 15px;padding: 0px; margin-top:10px")
            self.card_content_layout.addWidget(self.species_age_label)

            riwayat_title_label = QLabel("Riwayat Kesehatan")
            riwayat_title_label.setStyleSheet("""
                background-color: transparent;
                margin-left: 10px;
                margin-bottom: 15px;
                padding: 0px;
                font-size: 24px;
                font-weight: bold;
            """)
            self.card_content_layout.addWidget(riwayat_title_label)
            
            # Create QLabel for additional info
            self.info = QLabel(f"{self.riwayat_penyakit}")
            self.info.setStyleSheet("background-color: transparent;margin-left: 10px;margin-bottom: 15px;padding: 0px;") 
            self.card_content_layout.addWidget(self.info)

        else:
            print("Error: Unable to load image.")

        # Add the card content to the main layout
        layout.addWidget(self.card_content)
        self.setLayout(layout)


# if __name__ == "__main__":
#     app = QApplication(sys.argv)
    
#     # Create a main window
#     window = QWidget()
#     window.setWindowTitle("Multiple Cards Example")
    
#     # Create a vertical layout to hold the cards
#     layout = QVBoxLayout()
    
#     # Create and add multiple card widgets
#     card_data = [
#         {"name": "John Doe","species":"angjing" , "age": 30, "riwayat_penyakit": "Lorem ipsum dolor sit amet", "image_path": "img/meng.png"},
#         {"name": "Jane Smith","species":"angjing" , "age": 25, "riwayat_penyakit": "Consectetur adipiscing elit", "image_path": "img/meng.png"},
#         {"name": "Alice Johnson","species":"angjing" , "age": 35, "riwayat_penyakit": "Sed do eiusmod tempor incididunt", "image_path": "img/meng.png"}
#     ]
    
#     for data in card_data:
#         card = CardWidget(**data)  # Create a CardWidget instance with the provided data
#         layout.addWidget(card)  # Add the card to the layout
    
#     # Set the layout of the main window
#     window.setLayout(layout)
    
#     # Display the main window
#     window.show()
    
#     sys.exit(app.exec_())
