from PyQt5.QtWidgets import QWidget, QVBoxLayout, QGridLayout, QLabel, QFrame, QGraphicsDropShadowEffect, QScrollArea, QSizePolicy, QApplication, QHBoxLayout
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QColor, QCursor

from utils.font import get_font
class MainArticleView(QWidget):
    view_article_signal = pyqtSignal(int)
    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        screen_geometry = QApplication.desktop().availableGeometry()

        main_layout = QHBoxLayout()
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        main_content_widget = QWidget(self)
        main_content_layout = QVBoxLayout(main_content_widget)
        main_content_layout.setContentsMargins(
            int(screen_geometry.width() * 0.1), 
            int(screen_geometry.height() * 0.1), 
            int(screen_geometry.width() * 0.1), 
            0,
        )
        main_content_widget.setStyleSheet('background-color: #F8F8F8;')

        heading = QLabel("Artikel")
        heading.setStyleSheet('font-size: 72px; color: #F277AD; font-weight:900;')
        heading.setFont(get_font("bold"))
        heading.setFixedHeight(int(screen_geometry.height() * 0.075))

        main_content_layout.addWidget(heading)

        line = QFrame()
        line.setFrameShape(QFrame.HLine)
        line.setFrameShadow(QFrame.Sunken)
        line.setStyleSheet("QFrame { background-color: #F277AD; margin:0px; }")
        line.setFixedWidth(int(screen_geometry.width() * 0.7))
        line.setContentsMargins(0,0,0,0)
        main_content_layout.addWidget(line)

        self.article_cards_layout = QGridLayout()
        self.article_cards_layout.setVerticalSpacing(20)
        self.article_cards_layout.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        self.article_cards_layout.setHorizontalSpacing(50)

        cards_widget = QWidget(self)
        cards_widget.setLayout(self.article_cards_layout)

        scroll_area = QScrollArea(self)

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

        scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        scroll_area.setFixedHeight(int(screen_geometry.height() * 0.8))
        scroll_area.setWidgetResizable(True)
        scroll_area.setWidget(cards_widget)


        # Add the scroll area to the main layout
        main_content_layout.addWidget(scroll_area)
        main_content_layout.setContentsMargins(150,150,150,0)

        self.setLayout(main_content_layout)

    def set_articles(self,articles):
        num_of_articles = len(articles)
        for i in range(num_of_articles):
            card = ArticleCard(articles[i], self)
            card.setFixedSize(975,500)
            card.my_signal.connect(self.view_article_signal)
            self.article_cards_layout.addWidget(card, i // 2, i % 2)


class ArticleCard(QWidget):
    my_signal = pyqtSignal(int)
    def __init__(self,article,parent):
        super().__init__()
        self.article_index = article[0]
        self.title = article[1]
        self.content = article[2]
        self.parent = parent
        self.setup_ui()

    def setup_ui(self):
        screen_geometry = QApplication.desktop().availableGeometry()

        card = QWidget(self)
        card_layout = QVBoxLayout(card)
        card_layout.setContentsMargins(0,0,0,0)
        card_layout.setSpacing(0)

        MAX_TITLE_LENGTH = 60
        MAX_CONTENT_LENGTH = 315
        title_label = QLabel(self.title[:MAX_TITLE_LENGTH], self)
        title_label.setWordWrap(True)
        title_label.setStyleSheet("color: #1A646B; font-size: 40px; font-style: bold; font-weight:900")
        title_label.setFont(get_font("bold"))
        title_label.setFixedHeight(int(screen_geometry.height() * 0.075))
        
        content_label = QLabel(self.content[:MAX_CONTENT_LENGTH] + "...", self)
        content_label.setFont(get_font("regular"))
        content_label.setWordWrap(True)
        content_label.setStyleSheet("color: #000000; font-size: 32px;")
        
        card_layout.addWidget(title_label)
        card_layout.addWidget(content_label)
        
        card.setFixedSize(935, 460)
        card.setContentsMargins(20,20,20,20)
        self.setStyleSheet("background-color: #FFFFFF; border-radius: 20px;")

        shadow = QGraphicsDropShadowEffect(self)
        shadow.setOffset(0, 4)
        shadow.setBlurRadius(50)
        shadow.setColor(QColor(0, 0, 0, 10))
        self.setGraphicsEffect(shadow)

        self.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)

        self.mousePressEvent = self.emit_signal
    
    def emit_signal(self, event):
        self.my_signal.emit(self.article_index)

    def enterEvent(self, event):
        QApplication.setOverrideCursor(QCursor(Qt.PointingHandCursor))
    
    def leaveEvent(self, event):
        QApplication.restoreOverrideCursor()