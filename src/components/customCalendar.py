import sys

from PyQt5.QtCore import pyqtSignal, QDate
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QCalendarWidget

class CustomCalendar(QWidget):

    clicked = pyqtSignal(QDate)
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        layout.setContentsMargins(0,0,0,0)
        layout.setSpacing(0)

        # Create custom calendar widget
        self.calendar = QCalendarWidget()

        # Apply stylesheets for customization
        self.calendar.setStyleSheet(""" 
            QCalendarWidget QToolButton {
                height: 60px;
                width: 150px;
                color: black;
                font-size: 24px;
                icon-size: 56px, 56px;
                background-color:#D4D4D4;
            }
                                    
            QCalendarWidget QMenu {
                width: 150px;
                left: 20px;
                color: black;
                font-size: 18px;
                background-color: #D4D4D4;
            }
                                    
            QCalendarWidget QSpinBox { 
                width: 150px; 
                font-size:24px; 
                color: black; 
                background-color: #D4D4D4; 
                selection-background-color: #D4D4D4;
                selection-color: #000;
            }
            QCalendarWidget QSpinBox::up-button { subcontrol-origin: border;  subcontrol-position: top right;  width:35px; }
            QCalendarWidget QSpinBox::down-button {subcontrol-origin: border; subcontrol-position: bottom right;  width:35px;}
            QCalendarWidget QSpinBox::up-arrow { width:45px;  height:45px; }
            QCalendarWidget QSpinBox::down-arrow { width:45px;  height:45px; }
            
            /* header row */
            QCalendarWidget QWidget { alternate-background-color: #FFEAB4; }
            
            /* normal days */
            QCalendarWidget QAbstractItemView:enabled 
            {
                font-size:24px;  
                color: black;  
                background-color: white;  
                selection-background-color: #FFD7E0; 
                selection-color: rgb(0, 0, 0);
            }                          
            /* days in other months */
            /* navigation bar */
            QCalendarWidget QWidget#qt_calendar_navigationbar
            { 
                background-color: #D4D4D4; 
            }

            QCalendarWidget QAbstractItemView:disabled 
            { 
            color: #D4D4D4; 
            }

            #qt_calendar_prevmonth,
            #qt_calendar_nextmonth {
                border: none;
                qproperty-icon: none;
                background-color: transparent;        
            }
                                    
            #qt_calendar_prevmonth{
                padding-left: 15px;
                margin-left: 5px;
                image: url("img/icon_left.png");
                width: 30px; 
                height: 30px; 
            }
                                    
            #qt_calendar_nextmonth {
                padding-right: 15px;
                margin-right: 5px;
                image: url("img/icon_right.png");
                width: 30px; 
                height: 30px;
            }
            

        """)
        self.calendar.clicked.connect(self.emit_clicked_signal)
        layout.addWidget(self.calendar)
        self.setLayout(layout)
    
    def emit_clicked_signal(self, date):
        # Emit the custom clicked signal with the selected date
        self.clicked.emit(date)
       

    def selectedDate(self):
        # Return the selected date
        return self.calendar.selectedDate()
    
    def setSelectedDate(self,date):
        self.calendar.setSelectedDate(date)
    
    def clearSelectedDate(self):
        self.calendar.clearFocus()
        

    
