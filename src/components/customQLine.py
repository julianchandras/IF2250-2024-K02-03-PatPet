from PyQt5.QtWidgets import QLineEdit, QApplication, QVBoxLayout, QWidget
import sys

class CustomLineEdit(QLineEdit):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setStyleSheet("""
            QLineEdit {
                background-color: white;
                border: 2px solid #D4D4D4;
                border-radius: 10px;
                padding: 6px;
                font-size: 16px;
            }
        """)
    def paintEvent(self, event):
        super().paintEvent(event)

class TestWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        self.custom_line_edit = CustomLineEdit()
        layout.addWidget(self.custom_line_edit)
        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = TestWidget()
    widget.show()
    sys.exit(app.exec_())
