import sys
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QStackedWidget,
    QHBoxLayout,
    QWidget,
)
from PyQt5.QtGui import QFontDatabase, QFont



## Boundaries
from boundaries.mainView import MainView
from boundaries.petViews.addPetView import AddPetView
from boundaries.petViews.detailPetView import DetailPetView
from boundaries.petViews.editPetView import EditPetView
from boundaries.foodViews.mainFoodView import MainFoodView
from boundaries.articleViews.detailArticleView import DetailArticleView
from boundaries.articleViews.mainArticleView import MainArticleView
from boundaries.activityViews.addActivityView import AddActivityView
from boundaries.activityViews.updateActivityView import UpdateActivityView

## Controllers
from controllers.petController import PetController
from controllers.foodController import FoodController
from controllers.articleController import ArticleController
from controllers.activityController import ActivityController
from controllers.mainController import MainController


## Models
from models.petModel import PetModel
from models.foodModel import FoodModel
from models.articleModel import ArticleModel
from models.activityModel import ActivityModel

## Components
from components.sidebar import Sidebar

# Main application with QStackedWidget to manage multiple views
class PetManagementApp(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set the window title
        self.setWindowTitle("Pet Management App")
        # font_id = QFontDatabase.addApplicationFont("img/fonts/Raleway-Regular.ttf")
        # font_family = QFontDatabase.applicationFontFamilies(font_id)[0]

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
        self.food_model = FoodModel("database/pet_management.db")
        self.article_model = ArticleModel("database/pet_management.db")
        self.activity_model = ActivityModel("database/pet_management.db")

        # Create views
        self.main_pet_view = MainView()
        self.main_article_view = MainArticleView()
        self.detail_article_view = DetailArticleView()
        self.add_pet_view = AddPetView()
        self.edit_pet_view = EditPetView()
        self.detail_pet_view = DetailPetView()
        self.main_food_view = MainFoodView()
        self.add_activity_view = AddActivityView()
        self.update_activity_view = UpdateActivityView()

        # Add views to QStackedWidget
        self.stacked_widget.addWidget(self.main_pet_view) # Index 0
        self.stacked_widget.addWidget(self.main_article_view) # Index 1
        self.stacked_widget.addWidget(self.detail_article_view) # Index 2
        self.stacked_widget.addWidget(self.add_pet_view) # Index 3
        self.stacked_widget.addWidget(self.edit_pet_view) # Index 4
        self.stacked_widget.addWidget(self.detail_pet_view) # Index 5
        self.stacked_widget.addWidget(self.main_food_view) # Index 6
        self.stacked_widget.addWidget(self.add_activity_view) # Index 7
        self.stacked_widget.addWidget(self.update_activity_view) # Index 8

        ## Clear input when changing views
        self.stacked_widget.currentChanged.connect(self.clear_input)

        # Create the sidebar and pass the stacked widget
        self.sidebar = Sidebar(QApplication.desktop().availableGeometry().width() // 6)
        self.sidebar.stacked_widget = self.stacked_widget

        # Add the sidebar and QStackedWidget to the main layout
        main_layout.addWidget(self.sidebar)
        main_layout.addWidget(self.stacked_widget)

        # Set QStackedWidget as the central widget
        self.setCentralWidget(central_widget)

        # Create the controller and pass the stacked widget and model
        self.pet_controller = PetController(self.stacked_widget, self.pet_model, self.food_model, self.activity_model)
        self.food_controller = FoodController(self.stacked_widget, self.food_model)
        self.article_controller = ArticleController(self.stacked_widget, self.article_model)
        self.activity_controller = ActivityController(self.stacked_widget, self.activity_model)
        self.main_controller = MainController(self.stacked_widget, self.food_model, self.pet_model, self.activity_model)

        # Show the main view initially
        self.stacked_widget.setCurrentIndex(0)  # Start with MainPetView
    
    # Handle the window close event
    def clear_input(self, index):
        needed_clear = [0,3,6,7]
        if index in needed_clear:
            self.stacked_widget.currentWidget().clear_input()
            if (index == 6):
                self.stacked_widget.currentWidget().revert_food()
            
        

# Main application entry point
if __name__ == "__main__":
    app = QApplication(sys.argv)  # Create the QApplication instance
    pet_management_app = PetManagementApp()  # Create the main application instance
    pet_management_app.showFullScreen()  # Show the main window
    sys.exit(app.exec_())  # Start the event loop





