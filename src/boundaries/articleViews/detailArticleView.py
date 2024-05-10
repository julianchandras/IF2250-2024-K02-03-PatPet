from PyQt5.QtWidgets import QWidget, QVBoxLayout, QFrame, QScrollArea, QLabel
from PyQt5.QtCore import Qt

class DetailArticleView(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
    
    def init_ui(self):
        page_layout = QVBoxLayout(self)
        page_layout.setAlignment(Qt.AlignLeft | Qt.AlignTop)

        self.title_label = QLabel()
        self.title_label.setStyleSheet("font-size: 80px; color: #1A646B; font-style: extra-bold")
        self.title_label.setFixedHeight(100)

        line = QFrame()
        line.setFrameShape(QFrame.HLine)
        line.setStyleSheet("color: #1A646B")

        scroll_area = QScrollArea()

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

        scroll_widget = QWidget()
        scroll_layout = QVBoxLayout(scroll_widget)
        scroll_layout.setAlignment(Qt.AlignTop)

        self.content_label = QLabel()
        self.content_label.setStyleSheet("font-size: 36px; color: #000000;")
        self.content_label.setWordWrap(True)

        scroll_layout.addWidget(self.content_label)
        scroll_widget.setLayout(scroll_layout)

        scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        scroll_area.setWidgetResizable(True)
        scroll_area.setWidget(scroll_widget)

        # Add the article_cards_layout to the page_layout
        page_layout.addWidget(self.title_label)
        page_layout.addWidget(line)

        # Add the scroll area to the main layout
        page_layout.addWidget(scroll_area)

        page_layout.setContentsMargins(150, 150, 150, 0)

        self.setLayout(page_layout)

    def set_article_details(self, article):
        self.title_label.setText(article[1])
        self.content_label.setText(article[2])
