
from PyQt5.QtWidgets import (
    QApplication,
    QVBoxLayout,
   
    QPushButton,
    QWidget,
)
class Sidebar(QWidget):
    def __init__(self):
        super().__init__()
        # Calculate the sidebar width as 1/6 of the primary screen's width
        if (QApplication.desktop() is not None):
            screen_geometry = QApplication.desktop().availableGeometry() # type: ignore
        
        screen_width = screen_geometry.width()
        sidebar_width = screen_width // 6  # Integer division to ensure a whole number
        self.setup_ui(sidebar_width)

    def setup_ui(self, width):
        layout = QVBoxLayout()  # Vertical layout for the sidebar
        
        # Set a fixed width for the sidebar based on the calculated 1/6 screen width
        self.setFixedWidth(width)
        
        # Navigation buttons
        main_button = QPushButton("Main View")
        add_button = QPushButton("Add Pet")
        detail_button = QPushButton("Detail View")
        edit_button = QPushButton("Edit View")

        # Connect buttons to change views in QStackedWidget
        main_button.clicked.connect(lambda: self.change_view(0))
        add_button.clicked.connect(lambda: self.change_view(1))
        detail_button.clicked.connect(lambda: self.change_view(2))
        edit_button.clicked.connect(lambda: self.change_view(3))
        
        # Add buttons to the sidebar layout
        layout.addWidget(main_button)
        layout.addWidget(add_button)
        layout.addWidget(detail_button)
        layout.addWidget(edit_button)

        self.setLayout(layout)  # Set the sidebar layout

    def change_view(self, index):
        if hasattr(self, "stacked_widget"):
            self.stacked_widget.setCurrentIndex(index)  # Change the current index in QStackedWidget