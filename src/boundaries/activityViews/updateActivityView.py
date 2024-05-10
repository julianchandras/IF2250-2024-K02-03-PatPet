from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import pyqtSignal
from datetime import datetime
class UpdateActivityView(QWidget):
    update_activity_signal = pyqtSignal(int, str, datetime, datetime, int)
    delete_activity_signal = pyqtSignal(int)
    def __init__(self):
        super().__init__()
        self.setup_ui()
    
    def setup_ui(self):
        pass

    def set_activity_detail(self, activity):
        pass