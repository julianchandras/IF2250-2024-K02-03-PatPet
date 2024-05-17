from PyQt5.QtGui import QFont, QFontDatabase

def get_font(font_path):
    # Check if the font path contains "regular" or "bold"
    if "regular" in font_path.lower():
        font_path = "img/fonts/Raleway-Regular.ttf"
    else:
        font_path = "img/fonts/Raleway-Bold.ttf"

    # Load the font
    font_id = QFontDatabase.addApplicationFont(font_path)
    font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
    font = QFont(font_family)
    return font

def set_font(font_path, point_size):
    # Check if the font path contains "regular" or "bold"
    if "regular" in font_path.lower():
        font_path = "img/fonts/Raleway-Regular.ttf"
    else:
        font_path = "img/fonts/Raleway-Bold.ttf"

    # Load the font
    font_id = QFontDatabase.addApplicationFont(font_path)
    if font_id == -1:
        raise ValueError(f"Font at path '{font_path}' could not be loaded.")

    font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
    font = QFont(font_family, point_size)  # Set the font family and point size
    return font