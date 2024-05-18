from PyQt5.QtCore import Qt, QEvent
from PyQt5.QtGui import QStandardItem
from PyQt5.QtWidgets import (
    QComboBox,
    QStyledItemDelegate,
)
from utils.font import set_font

class CheckableComboBox(QComboBox):

    class Delegate(QStyledItemDelegate):
        def sizeHint(self, option, index):
            size = super().sizeHint(option, index)
            size.setHeight(80)
            return size
            
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setMinimumHeight(60)
        self.setStyleSheet(
            """
            QComboBox {
                border: 2px solid gray;
                border-radius: 10px;
                padding: 10px;
            }
            QComboBox::drop-down {
                border: 0px;
            }
            QComboBox::down-arrow {
                image: url(img/chevron-down.png);
                width: 30px;
                height: 30px;
                margin-right: 20px;
            }
            """
        )
        self.setEditable(True)
        self.lineEdit().setReadOnly(True)
        self.lineEdit().setStyleSheet(
            " padding: 5px; height: 40px; font-size: 16px; color: black;"
        )
        self.lineEdit().setFont(set_font("regular",12))
        self.setItemDelegate(CheckableComboBox.Delegate())
    
        self.model().dataChanged.connect(self.updateText)
        self.lineEdit().installEventFilter(self)
        self.view().viewport().installEventFilter(self)
        self.closeOnLineEditClick = False

    def resizeEvent(self, event):
        self.updateText()
        super().resizeEvent(event)

    def eventFilter(self, obj, event):
        if obj == self.lineEdit():
            if event.type() == QEvent.MouseButtonRelease:
                if self.closeOnLineEditClick:
                    self.hidePopup()
                else:
                    self.showPopup()
                return True
            return False

        if obj == self.view().viewport():
            if event.type() == QEvent.MouseButtonRelease:
                index = self.view().indexAt(event.pos())
                item = self.model().item(index.row())

                if item.checkState() == Qt.Checked:
                    item.setCheckState(Qt.Unchecked)
                else:
                    item.setCheckState(Qt.Checked)
                return True
        return False

    def showPopup(self):
        super().showPopup()
        self.closeOnLineEditClick = True

    def hidePopup(self):
        super().hidePopup()
        self.startTimer(100)
        self.updateText()

    def timerEvent(self, event):
        self.killTimer(event.timerId())
        self.closeOnLineEditClick = False

    def updateText(self):
        texts = []
        for i in range(self.model().rowCount()):
            if self.model().item(i).checkState() == Qt.Checked :
                
                texts.append(self.model().item(i).text())
        
        text = ", ".join(texts)

        if text == "" or texts == [] or text == None:
            text = "Pilih Makanan"
        self.lineEdit().clear()
        self.lineEdit().setText(text)

    def addItem(self, text, data=None):
        item = QStandardItem()
        item.setText(text)  # Displayed text
        
        if data is None:
            data = text  # If no data is provided, use the text as the data (not ideal)
        
        item.setData(data, Qt.UserRole)  # Store unique data under UserRole
        item.setFlags(Qt.ItemIsEnabled | Qt.ItemIsUserCheckable)  # Make it checkable
        item.setData(Qt.Unchecked, Qt.CheckStateRole)  # Initial check state

        self.model().appendRow(item)  # Add the item to the combo box's model

    def addItems(self, items):
        for text, data in items:
            self.addItem(text, data)  # Add each item with its data

    def currentData(self):
        """Returns a list of unique data values for checked items."""
        checked_data = []
        for i in range(self.model().rowCount()):
            item = self.model().item(i)
            if item.checkState() == Qt.Checked:
                checked_data.append(item.data(Qt.UserRole))  # Get data from UserRole
        return checked_data
    
    def setCheckState(self, index, state):
        item = self.model().item(index)
        item.setCheckState(Qt.Checked if state else Qt.Unchecked)
        self.updateText()
    


