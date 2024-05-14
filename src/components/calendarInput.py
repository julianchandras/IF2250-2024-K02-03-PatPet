import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QLabel
from PyQt5.QtGui import QIcon
from components.customCalendar import CustomCalendar
from components.customQLine import CustomLineEdit
from utils.font import get_font

class CalendarInput(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        # Create line edit
        self.line_edit = CustomLineEdit()
        self.line_edit.setFixedHeight(50)
        self.line_edit.setPlaceholderText('Click to select date')
        self.line_edit.setFont(get_font("regular"))

        # Create button
        self.button = QPushButton()
        self.button.clicked.connect(self.show_calendar)

        icon = QIcon("img/calendar.svg")
        self.button.setIcon(icon)
        self.button.setStyleSheet("""
            QPushButton {
                background-color: #fff;
                border: 2px solid #D4D4D4;
                color: white;
                padding: 10px;
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
        # Get the geometry of the line edit and button
        line_edit_rect = self.line_edit.geometry()
        button_rect = self.button.geometry()

        # Calculate the position for the calendar
        calendar_x = self.line_edit.mapToGlobal(line_edit_rect.bottomLeft()).x() - 20 # Align with the left of the line edit
        calendar_y = self.line_edit.mapToGlobal(line_edit_rect.bottomLeft()).y() + self.line_edit.height() - 45 # Below the line edit, at its bottom
        calendar_width = line_edit_rect.width() + button_rect.width()  # Match the width of the line edit and button

        # Set the geometry of the calendar
        self.calendar.setGeometry(calendar_x, calendar_y, calendar_width, self.calendar.height())

        # Show the calendar
        self.calendar.show()


    def update_date(self):
        selected_date = self.calendar.selectedDate()
        self.line_edit.setText(selected_date.toString("yyyy-MM-dd"))

