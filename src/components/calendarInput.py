import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QLabel
from PyQt5.QtGui import QIcon
from customCalendar import CustomCalendar
from customQLine import CustomLineEdit

class CalendarInput(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        # Create line edit
        self.line_edit = CustomLineEdit()
        self.line_edit.setPlaceholderText('Click to select date')

        # Create button
        self.button = QPushButton()
        self.button.clicked.connect(self.show_calendar)

        icon = QIcon("calendar.svg")
        self.button.setIcon(icon)
        self.button.setStyleSheet("""
            QPushButton {
                background-color: #fff;
                border: 2px solid #D4D4D4;
                color: white;
                padding: 6px;
                border-radius: 10px;
            }

            QPushButton:hover {
                background-color: #D4D4D4; /* Darker green */
            }

            QPushButton:pressed {
                background-color: #D4D4D4; /* Green when pressed */
            }
        """)
        
        self.button.setFixedSize(100, 50)

        # Create calendar widget
        self.calendar = CustomCalendar()
        self.calendar.setWindowFlags(self.calendar.windowFlags() | Qt.Popup)
        self.calendar.clicked.connect(self.update_date)

        # Hide calendar initially
        self.calendar.hide()

        # Create layout
        layout = QVBoxLayout()

        # Create horizontal layout for QLineEdit and QPushButton
        row_layout = QHBoxLayout()
        row_layout.addWidget(self.line_edit)
        row_layout.addWidget(self.button)

        # Add label and row layout to the main layout
        layout.addLayout(row_layout)

        # Set layout
        self.setLayout(layout)

        # Connect signals
        self.line_edit.mousePressEvent = self.show_calendar
        self.button.clicked.connect(self.show_calendar)

    def show_calendar(self, event=None):
        self.calendar.show()

    def update_date(self):
        selected_date = self.calendar.selectedDate()
        self.line_edit.setText(selected_date.toString("yyyy-MM-dd"))

