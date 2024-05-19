from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QPushButton
from PyQt5.QtCore import Qt

class CustomErrorDialog(QDialog):
    def __init__(self, message):
        super().__init__()
        self.setWindowTitle("Error")
        self.setWindowFlag(Qt.FramelessWindowHint)  # Remove window frame
        self.setAttribute(Qt.WA_TranslucentBackground)  # Set translucent background
        self.setStyleSheet(
            
            "QLabel {font-size: 16px; color: #721C24;}"
            "QPushButton {background-color: #DC3545; color: white; border: none; border-radius: 5px; padding: 8px 16px;}"
            "QPushButton:hover {background-color: #C82333;}"
            "QDialog {background-color: #F8D7DA; border-radius: 10px;}"
        )

        layout = QVBoxLayout()
        layout.setContentsMargins(10, 10, 10, 10)
        
        
        message_label = QLabel(message)
        message_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(message_label)

        ok_button = QPushButton("OK")
        ok_button.clicked.connect(self.accept)
        ok_button.setCursor(Qt.PointingHandCursor)  # Change cursor to pointing hand on hover
        ok_button.setFixedSize(100, 30)
        layout.addWidget(ok_button, alignment=Qt.AlignCenter)

        self.setLayout(layout)
