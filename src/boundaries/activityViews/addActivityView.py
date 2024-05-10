from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import pyqtSignal
from datetime import datetime
class AddActivityView(QWidget):

    add_activity_signal = pyqtSignal(str, datetime, datetime, int)
    navigate_to_update = pyqtSignal(int)

    def __init__(self):
        super().__init__()
        self.setup_ui()
    
    def setup_ui(self):
        pass

    def set_activities(self, activity):
        pass