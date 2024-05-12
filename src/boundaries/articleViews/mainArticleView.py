from PyQt5.QtWidgets import QWidget, QVBoxLayout, QGridLayout, QLabel, QFrame, QGraphicsDropShadowEffect, QScrollArea, QSizePolicy
from PyQt5.QtCore import Qt, pyqtSignal

class MainArticleView(QWidget):
    view_article_signal = pyqtSignal(int)
    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        page_layout = QVBoxLayout(self)

        heading = QLabel("Artikel")
        heading.setStyleSheet("font-size: 80px; color: #F277AD")
        heading.setFixedHeight(80)

        line = QFrame()
        line.setFrameShape(QFrame.HLine)
        line.setStyleSheet("color: #F277AD")

        self.article_cards_layout = QGridLayout()
        self.article_cards_layout.setVerticalSpacing(20)
        self.article_cards_layout.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        self.article_cards_layout.setHorizontalSpacing(150)

        cards_widget = QWidget(self)
        cards_widget.setLayout(self.article_cards_layout)

        scroll_area = QScrollArea(self)

        scroll_area.setStyleSheet("""
            QScrollArea {
                border: none;
            }
            QScrollBar:vertical {
                background: transparent;
                width: 10px;
                margin: 0px 0px 0px 0px;
            }
            QScrollBar::handle:vertical {
                background: #888888;
                min-height: 20px;
                border-radius: 4px;
            }
            QScrollBar::handle:vertical:hover {
                background: #555555;
            }
            QScrollBar::add-line:vertical {
                background: transparent;
                height: 0px;
                subcontrol-position: bottom;
                subcontrol-origin: margin;
            }
            QScrollBar::sub-line:vertical {
                background: transparent;
                height: 0px;
                subcontrol-position: top;
                subcontrol-origin: margin;
            }
        """)

        scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        scroll_area.setWidgetResizable(True)
        scroll_area.setWidget(cards_widget)

        # Add the article_cards_layout to the page_layout
        page_layout.addWidget(heading)
        page_layout.addWidget(line)

        # Add the scroll area to the main layout
        page_layout.addWidget(scroll_area)
        page_layout.setContentsMargins(150,150,150,0)

        self.setLayout(page_layout)

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
        card = QWidget(self)
        card_layout = QVBoxLayout(card)

        MAX_TITLE_LENGTH = 60
        MAX_CONTENT_LENGTH = 335
        title_label = QLabel(self.title[:MAX_TITLE_LENGTH], self)
        title_label.setWordWrap(True)
        title_label.setStyleSheet("color: #1A646B; font-size: 50px; font-style: bold;")
        title_label.setFixedHeight(120)
        
        content_label = QLabel(self.content[:MAX_CONTENT_LENGTH] + "...", self)
        content_label.setWordWrap(True)
        content_label.setStyleSheet("color: #000000; font-size: 32px;")
        
        card_layout.addWidget(title_label)
        card_layout.addWidget(content_label)
        
        card.setFixedSize(935, 460)
        card.setContentsMargins(20,20,20,20)
        self.setStyleSheet("background-color: #FFFFFF; border-radius: 10px;")

        shadow = QGraphicsDropShadowEffect(self)
        shadow.setOffset(0, 4)
        shadow.setBlurRadius(4)
        self.setGraphicsEffect(shadow)

        self.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)

        self.mousePressEvent = self.emit_signal
    
    def emit_signal(self, event):
        self.my_signal.emit(self.article_index)