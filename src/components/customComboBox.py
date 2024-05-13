import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QComboBox, QListView

class CustomComboBox(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.combo_box = QComboBox()
        self.combo_box.setEditText("Select an option")
        self.combo_box.setView(QListView())  # Set QListView as the dropdown view
    
        self.combo_box.setStyleSheet("""
            QComboBox {
                padding: 5px;
                border: 1px solid #ccc;
                border-radius: 5px;
                background-color: #f2f2f2;
                selection-background-color: #e0e0e0;
            }
            QComboBox::drop-down {
                border: 0px;
            }
            QComboBox::down-arrow {
                image: url("img/chevron-down.png");
                width: 30px;
                height: 30px;
                margin-right: 20px;
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

    def addItem(self, display_text, value):
        self.combo_box.addItem(display_text, value)

    def addItems(self, items):
        self.combo_box.clear()
        for item in items:
            display_text = item[0]
            value = item[1]
            self.addItem(display_text, value)

    def clearSelection(self):
        self.combo_box.setCurrentIndex(-1)

    def setDefaultText(self, text):
        self.combo_box.setEditText(text)


