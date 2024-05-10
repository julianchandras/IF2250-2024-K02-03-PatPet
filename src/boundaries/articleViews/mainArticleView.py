from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import pyqtSignal 

class MainArticleView(QWidget):
    view_article_signal = pyqtSignal(int)
    def __init__(self):
        super().__init__()
        self.setup_ui()
    
    def setup_ui(self):
        pass

    def set_articles(self, articles):
        pass