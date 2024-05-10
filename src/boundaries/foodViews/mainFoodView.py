from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import pyqtSignal
class MainFoodView(QWidget):
    add_food_signal = pyqtSignal(str)
    update_food_signal = pyqtSignal(int, str)
    delete_food_signal = pyqtSignal(int)
    def __init__(self):
        super().__init__()
        self.setup_ui()
    
    def setup_ui(self):
        pass

    def set_food(self, foods):
        pass
