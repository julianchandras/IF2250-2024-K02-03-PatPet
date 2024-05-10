from PyQt5.QtWidgets import (
    QVBoxLayout,
    QPushButton,
    QWidget,
    QLabel,
    
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap

class Sidebar(QWidget):
    def __init__(self, width):
        super().__init__()
        self.setup_ui(width)

    def setup_ui(self, width):
        layout = QVBoxLayout()  # Vertical layout for the sidebar
        layout.setContentsMargins(0, 0, 0, 0)  # Set layout margins to 0
        layout.setSpacing(0)  # Set the spacing between widgets to 0
        
        # Set a fixed width for the sidebar
        self.setFixedWidth(width)

        # Create a widget to contain the main content with a specified background color
        main_content_widget = QWidget(self)
        main_content_widget.setStyleSheet("background-color: #F99035;")
        main_content_layout = QVBoxLayout(main_content_widget)
        
        # Add a logo at the top
        logo_label = QLabel()  # Create a label to display the logo
        logo_pixmap = QPixmap("img/logo_patpet.svg")  # Load the logo image
        logo_label.setPixmap(logo_pixmap)  # Set the pixmap to the label
        logo_label.setAlignment(Qt.AlignHCenter)


        # Navigation buttons
        main_button = QPushButton("Main View")
        add_button = QPushButton("Add Pet")
        detail_button = QPushButton("Detail View")
        edit_button = QPushButton("Edit View")
        test_button = QPushButton("Test View")
        
        # Set styles for buttons for better visibility on the orange background
        button_style = "font-weight: bold; border: none; color: white;"
        for button in (main_button, add_button, detail_button, edit_button):
            button.setStyleSheet(button_style)  # Apply style to all buttons
        
        # Connect buttons to change views in QStackedWidget
        main_button.clicked.connect(lambda: self.change_view(0))
        add_button.clicked.connect(lambda: self.change_view(1))
        detail_button.clicked.connect(lambda: self.change_view(5))
        edit_button.clicked.connect(lambda: self.change_view(3))
        test_button.clicked.connect(lambda: self.change_view(4))
        
        # Add widgets to the layout
        main_content_layout.addWidget(logo_label)  # Add the logo at the top
        # Optional: add a bit of spacing after the logo
        main_content_layout.addSpacing(20)
        # Add navigation buttons
        main_content_layout.addWidget(main_button)
        main_content_layout.addWidget(add_button)
        main_content_layout.addWidget(detail_button)
        main_content_layout.addWidget(edit_button)
        main_content_layout.addWidget(test_button)
        main_content_layout.setAlignment(Qt.AlignTop)  # Align the content to the top
        
        layout.addWidget(main_content_widget)  # Add the main content widget to the sidebar layout

        self.setLayout(layout)  # Set the sidebar layout

    def change_view(self, index):
        if hasattr(self, "stacked_widget"):
            self.stacked_widget.setCurrentIndex(index)  # Change the current index in QStackedWidget
