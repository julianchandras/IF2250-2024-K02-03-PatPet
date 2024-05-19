from PyQt5.QtWidgets import QLineEdit, QApplication, QVBoxLayout, QWidget
from utils.font import *
from utils.screensize import *

class CustomLineEdit(QLineEdit):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setStyleSheet("""
            QLineEdit {
                background-color: white;
                border: 2px solid #D4D4D4;
                border-radius: 10px;
                padding: 6px;

            }
        """)
        if (getHeight() > 1080):
            self.setFont(set_font("regular",12))
        else:
            self.setFont(set_font("regular",10))

    def paintEvent(self, event):
        super().paintEvent(event)



