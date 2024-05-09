import sys
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QStackedWidget,
    QHBoxLayout,
    QWidget,
)
# Import the necessary views and controllers
from boundaries.petViews.mainPetView import MainPetView
from boundaries.petViews.addPetView import AddPetView
from boundaries.petViews.detailPetView import DetailPetView
from boundaries.petViews.editPetView import EditPetView
from controllers.petController import PetController
from models.petModel import PetModel
from components.sidebar import Sidebar

# Main application with QStackedWidget to manage multiple views
class PetManagementApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Pet Management App")
        main_layout = QHBoxLayout()

        central_widget = QWidget()
        central_widget.setLayout(main_layout)

        # Create a QStackedWidget to manage multiple views
        self.stacked_widget = QStackedWidget()

        # Create the model
        self.pet_model = PetModel("database/pet_management.db")

        # Create views
        self.main_pet_view = MainPetView()
        self.add_pet_view = AddPetView()
        self.detail_pet_view = DetailPetView()
        self.edit_pet_view = EditPetView()

        # Add views to QStackedWidget
        self.stacked_widget.addWidget(self.main_pet_view)  # Index 0
        self.stacked_widget.addWidget(self.add_pet_view)  # Index 1
        self.stacked_widget.addWidget(self.detail_pet_view)  # Index 2
        self.stacked_widget.addWidget(self.edit_pet_view)  # Index 3

        # Create the sidebar and pass the stacked widget
        self.sidebar = Sidebar()
        self.sidebar.stacked_widget = self.stacked_widget

        # Add the sidebar and QStackedWidget to the main layout
        main_layout.addWidget(self.sidebar)
        main_layout.addWidget(self.stacked_widget)


        # Set QStackedWidget as the central widget
        self.setCentralWidget(central_widget)

        # Create the controller and pass the stacked widget and model
        self.pet_controller = PetController(self.stacked_widget, self.pet_model)

        # Show the main view initially
        self.stacked_widget.setCurrentIndex(0)  # Start with MainPetView

# Main application entry point
if __name__ == "__main__":
    app = QApplication(sys.argv)  # Create the QApplication instance
    pet_management_app = PetManagementApp()  # Create the main application instance
    pet_management_app.show()  # Show the main window
    sys.exit(app.exec_())  # Start the event loop
