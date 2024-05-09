import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QTableWidget, QTableWidgetItem, QGroupBox
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtCore import Qt

class DetailHewanPage(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        screen_geometry = QApplication.desktop().availableGeometry()

        self.setWindowTitle('Detail Hewan')
        self.showFullScreen()

        main_layout = QHBoxLayout()
        main_layout.setContentsMargins(0, 0, 0, 0)

        sidebar_widget = QWidget(self)
        sidebar_widget.setFixedWidth(screen_geometry.width() // 6)

        sidebar_layout = QVBoxLayout(sidebar_widget)
        sidebar_layout.setContentsMargins(0, 0, 0, 0)

        sidebar_label = QLabel('Sidebar', self)
        sidebar_label.setStyleSheet('font-size: 48px; background-color: #F99035; font-weight: bold')
        sidebar_label.setFont(QFont('Arial', 14))

        sidebar_layout.addWidget(sidebar_label)

        main_layout.addWidget(sidebar_widget)

        main_content_widget = QWidget(self)
        main_content_layout = QVBoxLayout(main_content_widget)
        main_content_layout.setContentsMargins(115, 42, 115, 0)
        main_content_widget.setStyleSheet('background-color: #F2F2F2;')


    
        main_layout.addWidget(main_content_widget)

        self.setLayout(main_layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    foodEntryPage = DetailHewanPage()
    foodEntryPage.show()
    sys.exit(app.exec_())
