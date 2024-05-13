from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QGridLayout,
    QLabel,
    QVBoxLayout,
    QPushButton,
    QHBoxLayout,
    QScrollArea,
)
from PyQt5.QtCore import Qt, QDate
import sys


class CustomSchedule(QWidget):
    def __init__(self):
        super().__init__()

        self.activities = {} # Activity data dictionary
        self.current_date = QDate.currentDate()  # Start with today's date
        
    
        # Create the main layout with a grid for the calendar
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        # Create navigation controls
        self.create_navigation_controls()

        # Create a scroll area for the calendar
        scroll_area = QScrollArea()
        self.layout.addWidget(scroll_area)

        # Create a container widget for the grid layout
        calendar_container = QWidget()
        self.calendar_grid = QGridLayout()
        calendar_container.setLayout(self.calendar_grid)

        # Add the calendar grid to the scroll area
        scroll_area.setWidget(calendar_container)
        scroll_area.setWidgetResizable(True)

        # Populate the calendar with days and activities
        self.update_calendar()

    def create_navigation_controls(self):
        # Create navigation buttons to move between months
        navigation_layout = QHBoxLayout()
        
        # Previous month button
        prev_button = QPushButton()
        prev_button.setStyleSheet("""
            QPushButton {
                image: url("img/icon_left.png");
                width: 40px; 
                height: 40px;
            }
        """)
        prev_button.clicked.connect(self.go_to_previous_month)
        navigation_layout.addWidget(prev_button)

        # Current month label
        self.current_month_label = QLabel()
        self.current_month_label.setAlignment(Qt.AlignCenter)
        self.current_month_label.setStyleSheet("""
            font-size: 30px;
            font-weight: bold;
        """)
        navigation_layout.addWidget(self.current_month_label, 1)  # Span across

        # Next month button
        next_button = QPushButton()
        next_button.setStyleSheet("""
            QPushButton {
                image: url("img/icon_right.png");
                width: 40px; 
                height: 40px;
            }
        """)
        next_button.clicked.connect(self.go_to_next_month)
        navigation_layout.addWidget(next_button)

        # Add the navigation layout to the main layout
        self.layout.addLayout(navigation_layout)

    def go_to_previous_month(self):
        self.current_date = self.current_date.addMonths(-1)
        self.update_calendar()

    def go_to_next_month(self):
        self.current_date = self.current_date.addMonths(1)
        self.update_calendar()

    def update_calendar(self):
        # Clear the existing calendar grid
        for i in reversed(range(self.calendar_grid.count())):
            self.calendar_grid.itemAt(i).widget().deleteLater()

        # Get the first day of the current month
        first_day = self.current_date.addDays(-self.current_date.day() + 1)

        # Update the current month label
        month_name = first_day.toString("MMMM yyyy")
        self.current_month_label.setText(month_name)

        # Start the grid with day names (Sunday to Saturday)
        day_names = [ "Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
        for i, day_name in enumerate(day_names):
            label = QLabel(day_name)
            label.setAlignment(Qt.AlignCenter)
            label.setStyleSheet("""
                QLabel {
                    font-size: 24px;
                    font-weight: bold;
                    background-color: #F2F2F2;
                    border-radius: 3px;
                    
                }
            """)
            self.calendar_grid.addWidget(label, 0, i)

        # Determine the starting position for the first day
        day_of_week = first_day.dayOfWeek() - 1  # 0-based index for the week
        row = 1  # Start from the first row (after day names)

        # Populate the days of the month
        day = first_day
        for i in range(1, self.current_date.daysInMonth() + 1):
            # Create a cell for each day
            cell_layout = QVBoxLayout()
            cell_layout.setAlignment(Qt.AlignTop)
            day_label = QLabel(str(i))
            day_label.setStyleSheet("""
                QLabel {
                    font-size: 20px;
                }
            """)
            day_label.setAlignment(Qt.AlignTop | Qt.AlignLeft)
            
            # Add the label to the cell layout
            cell_layout.addWidget(day_label)
            print("ACTIVTIES")
            print(self.activities)
            # Add activities for the day (if any)
            day_str = day.toString("yyyy-MM-dd")
            if day_str in self.activities:
                for activity in self.activities[day_str]:
                    start_time, end_time, animal,detail = activity
                    activity_button = QPushButton(f"{start_time} - {end_time} ({animal})\n{detail}")
                    activity_button.clicked.connect(self.handle_activity_click)
                    activity_button.setStyleSheet("""
                        QPushButton {
                            background-color: #F277AD;
                            font-size: 18px;
                            font-weight: bold;
                            border-radius: 8px;
                            padding: 5px;                                                                                  
                            color : white;
                            text-align: left;
                        }

                        QPushButton:hover {
                            background-color: #F8B8D4;                         
                        }
                    """) 
                    cell_layout.addWidget(activity_button)

            # Create a container widget to hold the layout
            cell_widget = QWidget()
            cell_widget.setLayout(cell_layout)

            # Set the background color for weekends
            if day_of_week in [6]:
                cell_widget.setStyleSheet("background-color: #FFF3EE;")

            # Add the cell widget to the grid
            self.calendar_grid.addWidget(cell_widget, row, day_of_week)

            # Move to the next day and determine the next grid position
            day_of_week += 1
            if day_of_week == 7:  # Reset to Sunday
                day_of_week = 0
                row += 1

            day = day.addDays(1)  # Move to the next day

    def set_activities(self,activities):
        self.activities = activities
        self.update_calendar()

    def handle_activity_click(self):
        
        # Handle the click event here
        sender = self.sender()  # Get the button that was clicked
        activity_info = sender.text()  # Get the text of the button
        print("Clicked:", activity_info)


