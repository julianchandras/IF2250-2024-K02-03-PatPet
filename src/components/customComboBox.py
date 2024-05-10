import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QComboBox, QListView

class CustomComboBox(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.combo_box = QComboBox()
        self.combo_box.setView(QListView())  # Set QListView as the dropdown view
    
        self.combo_box.addItems([])
        self.combo_box.setStyleSheet("""
            QComboBox {
                padding: 5px;
                border: 1px solid #ccc;
                border-radius: 5px;
                background-color: #f2f2f2;
                selection-background-color: #e0e0e0;
            }
            QComboBox::drop-down {
                width: 20px;
                border: none;
                border-radius : 10px;
            }
            QComboBox::down-arrow {
                image: url("drop_down.png");
            }
            QListView {
                border: 1px solid #ccc; /* Add this line */
                border-top: none;
                border-radius: 10px;
            }
            QListView::item {
                background-color : #fff;
                border : none;
                border-radius : 10px;
                height: 30px;
                padding: 5px;
            }
            QListView::item:selected {
                color : #F277AD;
                background-color: #FFD7E0;
            }
    """)


        layout.addWidget(self.combo_box)

        self.setLayout(layout)


    def addItems(self, items):
        self.combo_box.addItems(items)

