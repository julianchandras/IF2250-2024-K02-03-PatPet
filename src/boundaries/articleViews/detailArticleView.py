from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QGridLayout,QLabel, QFrame, QGraphicsDropShadowEffect, QScrollArea, QSizePolicy
from PyQt5.QtCore import Qt

class DetailArticleView(QWidget):
    def __init__(self):
        super().__init__()
        self.setup_ui()
    
    def setup_ui(self):
        page_layout = QVBoxLayout(self)
        page_layout.setAlignment(Qt.AlignLeft | Qt.AlignTop)

        title = QLabel("Artikel")
        title.setStyleSheet("font-size: 80px; color: #1A646B; font-style:extra-bold")
        title.setFixedHeight(100)

        line = QFrame()
        line.setFrameShape(QFrame.HLine)
        line.setStyleSheet("color: #1A646B")

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

        scroll_widget = QWidget()
        scroll_layout = QVBoxLayout(scroll_widget)

        text = QLabel("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam ut semper justo, a luctus massa. Quisque urna ipsum, faucibus vel elementum et, egestas id risus. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Vivamus laoreet risus quis metus sodales, nec tincidunt mauris efficitur. Integer dictum at elit vitae semper. Nulla eu blandit orci, sed viverra neque. Nam libero purus, euismod pulvinar imperdiet in, sodales et justo. Praesent consectetur dui leo, id sodales nisi molestie bibendum. Duis ultricies sed sapien vel imperdiet. Mauris sit amet tellus vel mauris laoreet congue. Ut pulvinar tellus quis sem luctus, non mollis enim suscipit. Nam ac vehicula massa. Quisque vulputate, massa ut consectetur elementum, leo felis suscipit tellus, vel scelerisque sem mauris ac quam. Donec in massa sem. Aenean consequat nisi ultrices est blandit convallis. Sed mollis ultricies urna, nec lacinia ex blandit id.\n\nMorbi lacus felis, interdum gravida risus non, lacinia vulputate velit. Proin non tortor quis ligula blandit cursus. Nam consectetur orci nisi, sit amet volutpat quam interdum tempor. Morbi quis lacus dui. Quisque in nibh vel nunc ullamcorper mattis. Aenean fermentum quam at sodales tempor. Donec luctus odio in diam placerat sollicitudin. Nam velit arcu, aliquam in augue a, fringilla facilisis turpis. Aliquam ultrices ex at leo vestibulum convallis. Etiam non laoreet tortor. Vivamus a sem vitae lorem imperdiet maximus. Cras velit nunc, tincidunt at mollis sit amet, lacinia eu magna. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae;\n\nVestibulum quam odio, pulvinar sed orci sed, venenatis euismod massa. Ut elit odio, vestibulum ac purus at, sodales dictum ex. Aenean posuere imperdiet mauris ut feugiat. Suspendisse pretium lacinia quam, eget tincidunt ipsum luctus et. Mauris fermentum enim sed metus suscipit porta. Mauris non ante viverra, bibendum mi at, ultrices lectus. Nullam at iaculis eros. Sed et odio vel neque faucibus cursus quis in nulla. Curabitur porta tempus arcu. Fusce eu eros et nunc consequat vulputate. Integer ac nunc vel odio euismod varius. Donec quam libero, tincidunt eu nunc sit amet, pellentesque volutpat magna. Praesent vitae condimentum tellus.\n\nMorbi pretium porta purus et sagittis. Proin vestibulum justo massa, eget laoreet nibh mattis sit amet. Donec eget leo nunc. Aliquam finibus maximus eros, vitae cursus erat lacinia et. Vestibulum vel velit magna. Aliquam erat volutpat. Vivamus quis tortor ex. Praesent eget ante laoreet, mollis ex et, tincidunt neque. Quisque iaculis lacus enim. Cras laoreet nisi eget nibh accumsan imperdiet. Integer interdum porta dui vitae molestie. Donec vitae nibh vitae lectus sodales ultricies at sit amet velit.\n\nDonec quis gravida neque, at placerat velit. Nunc magna sapien, vestibulum vel lectus cursus, pretium placerat orci. Vivamus mattis fermentum purus, et pretium tortor luctus id. Aliquam erat volutpat. Suspendisse dictum lectus ac tempus volutpat. Nunc malesuada, sem in condimentum suscipit, augue purus pretium diam, ut placerat nunc velit at odio. Quisque facilisis a tortor id mattis. Morbi sit amet sem non quam mollis finibus id vitae purus. Donec ut elementum lacus. Aliquam quis luctus turpis. Interdum et malesuada fames ac ante ipsum primis in faucibus. Sed vulputate ex id diam accumsan, in vulputate lectus tempus. Sed fermentum gravida magna et consequat. Sed hendrerit augue vitae nisi feugiat ultricies. Quisque eu dapibus mauris, vel egestas nisi. Integer luctus, sem et ornare mattis, tortor eros bibendum dui, at vulputate quam erat a dolor.\n\nIn in ex non felis accumsan euismod. Etiam euismod non ex sit amet lacinia. Quisque eget consectetur ligula. Maecenas justo justo, varius eget fringilla id, fringilla non eros. Vivamus id ligula neque. Fusce consectetur tellus sit amet eros vulputate convallis. Aliquam at justo fringilla, scelerisque nisl et, sollicitudin lorem. Vivamus sollicitudin, nulla pellentesque ornare varius, libero eros consequat tellus, a sollicitudin ipsum arcu eget erat. Donec ac sodales justo, ut posuere urna. Proin ultricies diam et justo suscipit imperdiet. Etiam in metus tincidunt, aliquet ligula ut, lacinia sapien.")
        text.setStyleSheet("font-size: 36px; color: #000000;")
        text.setWordWrap(True)

        scroll_layout.addWidget(text)
        scroll_widget.setLayout(scroll_layout)

        scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        scroll_area.setWidgetResizable(True)
        scroll_area.setWidget(scroll_widget)

        # Add the article_cards_layout to the page_layout
        page_layout.addWidget(title)
        page_layout.addWidget(line)

        # Add the scroll area to the main layout
        page_layout.addWidget(scroll_area)

        page_layout.setContentsMargins(150, 150, 150, 0)

        self.setLayout(page_layout)
