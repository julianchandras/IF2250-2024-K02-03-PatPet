# from PyQt5.QtWidgets import QApplication

# global screen_geometry 
# screen_geometry = QApplication.desktop().availableGeometry()

# def getHeight():
#     return screen_geometry.height()

# def getWidth():
#     return screen_geometry.width()


from PyQt5.QtWidgets import QApplication

# Initialize the application
app = QApplication([])

# Get the primary screen
screen = app.primaryScreen()
screen_geometry = screen.availableGeometry()

def getHeight():
    return screen_geometry.height()

def getWidth():
    return screen_geometry.width()
