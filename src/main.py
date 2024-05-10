import sys
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QStackedWidget,
    QHBoxLayout,
    QWidget,
)

from boundaries.mainView import MainPetView
from boundaries.petViews.addPetView import AddPetView
from boundaries.petViews.detailPetView import DetailPetView
from boundaries.petViews.editPetView import EditPetView
from boundaries.articleViews.mainArticleView import MainArticleView
from boundaries.articleViews.detailArticleView import DetailArticleView
from controllers.petController import PetController
from models.petModel import PetModel
from components.sidebar import Sidebar

# Main application with QStackedWidget to manage multiple views
class PetManagementApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Pet Management App")

        # Create the main layout and central widget
        main_layout = QHBoxLayout()
        central_widget = QWidget()

        ## Set the layout and spacing of the main layout
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)
        
        ## Set the layout and spacing of the central widget
        central_widget.setLayout(main_layout)
        central_widget.setContentsMargins(0, 0, 0, 0)
        
  

        # Create a QStackedWidget to manage multiple views
        self.stacked_widget = QStackedWidget()

        # Create the model
        self.pet_model = PetModel("database/pet_management.db")

        # Create views
        self.main_pet_view = MainPetView()
        self.add_pet_view = AddPetView()
        self.detail_pet_view = DetailPetView()
        self.edit_pet_view = EditPetView()
        self.main_article_view = MainArticleView()
        self.detail_article_view = DetailArticleView()

        # Add views to QStackedWidget
        self.stacked_widget.addWidget(self.main_pet_view)  # Index 0
        self.stacked_widget.addWidget(self.add_pet_view)  # Index 1
        self.stacked_widget.addWidget(self.detail_pet_view)  # Index 2
        self.stacked_widget.addWidget(self.edit_pet_view)  # Index 3
        self.stacked_widget.addWidget(self.main_article_view)
        self.stacked_widget.addWidget(self.detail_article_view)

        # Create the sidebar and pass the stacked widget
        self.sidebar = Sidebar(QApplication.desktop().availableGeometry().width() // 6)
       
        self.sidebar.stacked_widget = self.stacked_widget

    
        # Add the sidebar and QStackedWidget to the main layout
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)
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
