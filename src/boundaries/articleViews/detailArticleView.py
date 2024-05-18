from PyQt5.QtWidgets import QApplication,QWidget, QVBoxLayout, QFrame, QScrollArea, QLabel, QTextEdit, QPushButton
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QCursor
from utils.font import *
from utils.screensize import *

class DetailArticleView(QWidget):
    back_signal = pyqtSignal()
    def __init__(self):
        super().__init__()
        self.init_ui()
    
    def init_ui(self):
        screen_geometry = QApplication.desktop().availableGeometry()
        page_layout = QVBoxLayout(self)
        page_layout.setAlignment(Qt.AlignLeft | Qt.AlignTop)

        self.title_label = QLabel()
        self.title_label.setStyleSheet("color: #1A646B; font-weight:900")
        self.title_label.setFixedHeight(int(getHeight() * 0.075))
        self.title_label.setFont(set_font("bold",24))
        
        line = QFrame()
        line.setFrameShape(QFrame.HLine)
        line.setFrameShadow(QFrame.Sunken)
        line.setStyleSheet("QFrame { background-color: #1A646B; }")
        line.setFixedWidth(int(getWidth() * 0.65))
        scroll_area = QScrollArea()

        scroll_area.setStyleSheet("""
            QScrollArea {
                border: none;
            }
            QScrollBar:vertical {
                border: none;
                background: #f0f0f0;
                width: 10px;
                margin: 0px 0px 0px 0px;
            }
            QScrollBar::handle:vertical {
                background: #c0c0c0;
                min-height: 20px;
            }
            QScrollBar::handle:vertical:hover {
                background: #a0a0a0;
            }
            QScrollBar::sub-line:vertical {
                border: none;
                background: none;
            }
            QScrollBar::add-line:vertical {
                border: none;
                background: none;
            }
            QScrollBar:horizontal {
                border: none;
                background: #f0f0f0;
                height: 10px;
                margin: 0px 0px 0px 0px;
            }
            QScrollBar::handle:horizontal {
                background: #c0c0c0;
                min-width: 20px;
            }
            QScrollBar::handle:horizontal:hover {
                background: #a0a0a0;
            }
            QScrollBar::sub-line:horizontal {
                border: none;
                background: none;
            }
            QScrollBar::add-line:horizontal {
                border: none;
                background: none;
            }
        """)

        scroll_widget = QWidget()
        scroll_layout = QVBoxLayout(scroll_widget)
        scroll_layout.setAlignment(Qt.AlignTop)

        
        self.content_label = QTextEdit()
        self.content_label.setStyleSheet("color: #000000; font-weight:400; background:transparent; border:none;")

        self.content_label.setFont(set_font("regular",12))
        self.content_label.setReadOnly(True)

        scroll_layout.addWidget(self.content_label)
        scroll_widget.setLayout(scroll_layout)

        scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        scroll_area.setFixedHeight(int(getHeight() * 0.775))
        scroll_area.setWidgetResizable(True)

        scroll_area.setWidget(scroll_widget)
        back_button = QPushButton('Kembali Ke Artikel', self)
        back_button.setStyleSheet("""
            QPushButton {
                border : 3px solid #F277AD;
                font-weight: bold;
                border-radius: 8px;
                color : #F277AD;
            }

            QPushButton:hover {
                background-color: #F8B8D4;
                border : 3px solid #F277AD;
            }
        """)
        back_button.setFont(set_font("bold",14))
        back_button.setCursor(QCursor(Qt.PointingHandCursor))
        back_button.setFixedSize(int(getWidth() * 0.65), int(getHeight() * 0.06))
        back_button.clicked.connect(self.back_article)
        # Add the article_cards_layout to the page_layout
        page_layout.addWidget(self.title_label)
        page_layout.addWidget(line)

        # Add the scroll area to the main layout
        page_layout.addWidget(scroll_area)
        page_layout.addWidget(back_button)
        page_layout.setContentsMargins(int(getWidth()*0.05), int(getHeight()*0.05), int(getWidth()*0.05), int(getHeight()*0.05))

        self.setLayout(page_layout)

    def set_article_details(self, article):
        self.title_label.setText(article[1])
        self.content_label.setPlainText(article[2])
        self.content_label.setAlignment(Qt.AlignJustify)
        self.content_label.setFixedWidth(int(getWidth() * 0.65))

    def back_article(self):
        self.back_signal.emit()


