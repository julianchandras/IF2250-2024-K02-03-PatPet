from PyQt5.QtWidgets import QWidget, QVBoxLayout, QGridLayout, QLabel, QFrame, QGraphicsDropShadowEffect, QScrollArea, QSizePolicy
from PyQt5.QtCore import Qt

class MainArticleView(QWidget):
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

        article_cards_layout = QGridLayout()
        article_cards_layout.setVerticalSpacing(20)
        article_cards_layout.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        article_cards_layout.setHorizontalSpacing(150)

        for i in range(4):
            card = ArticleCard(self)
            card.setFixedSize(975,500)
            article_cards_layout.addWidget(card, i // 2, i % 2)

        cards_widget = QWidget(self)
        cards_widget.setLayout(article_cards_layout)

        scroll_area = QScrollArea(self)
        # scroll_area.setStyleSheet("border: none;")

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

class ArticleCard(QWidget):
    def __init__(self,parent):
        super().__init__()
        self.setup_ui(parent)

    def setup_ui(self,parent):
        card = QWidget(self)
        card_layout = QVBoxLayout(card)

        title = QLabel("Judul random dengan panjang yang lumayan agar 2 baris")
        title.setWordWrap(True)
        title.setStyleSheet("color: #1A646B; font-size: 50px; font-style: bold;")
        title.setFixedHeight(120)
        
        text = QLabel("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed non risus. Suspendisse lectus tortor, dignissim sit amet, adipiscing nec, ultricies sed, dolor. Cras elementum ultrices diam. Maecenas ligula massa, varius a, semper...", self)
        text.setWordWrap(True)
        text.setStyleSheet("color: #000000; font-size: 32px;")
        
        card_layout.addWidget(title)
        card_layout.addWidget(text)
        
        card.setFixedSize(935, 460)
        card.setContentsMargins(20,20,20,20)
        self.setStyleSheet("background-color: #FFFFFF; border-radius: 10px;")

        shadow = QGraphicsDropShadowEffect(parent)
        shadow.setOffset(0, 4)
        shadow.setBlurRadius(4)
        self.setGraphicsEffect(shadow)

        self.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
