from PyQt5.QtCore import Qt, QEvent
from PyQt5.QtGui import QStandardItem, QFontMetrics, QPalette
from PyQt5.QtWidgets import QComboBox, QStyledItemDelegate, qApp, QSizePolicy


class CheckableComboBox(QComboBox):
    # Custom Delegate to adjust item appearance
    class Delegate(QStyledItemDelegate):
        def sizeHint(self, option, index):
            size = super().sizeHint(option, index)
            size.setHeight(40)  # Adjust item height for increased spacing
            return size

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Set minimum height for the combo box
        self.setMinimumHeight(50)  # This increases the overall height of the combo box

        # Make the combo editable to set a custom text but read-only
        self.setEditable(True)
        self.lineEdit().setReadOnly(True)

        # Customize the `lineEdit` with style sheet to increase its height
        self.lineEdit().setStyleSheet(
            "background-color: white; border: 2px solid gray; border-radius: 10px; padding: 10px; height: 30px; font-size: 16px; color: black;"
        )

        # Set the custom delegate
        self.setItemDelegate(CheckableComboBox.Delegate())

        # Signal to update text when item is toggled
        self.model().dataChanged.connect(self.updateText)

        # Hide and show popup when clicking on the line edit
        self.lineEdit().installEventFilter(self)
        self.closeOnLineEditClick = False

        # Prevent popup from closing when clicking on an item
        self.view().viewport().installEventFilter(self)

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

    def updateText(self):
        texts = []
        for i in range(self.model().rowCount()):
            if self.model().item(i).checkState() == Qt.Checked:
                texts.append(self.model().item(i).text())
        text = ", ".join(texts)

        if not text:
            text = "Pilih Makanan"  # Default text when nothing is selected

        # Compute elided text (with "...")
        metrics = QFontMetrics(self.lineEdit().font())
        elidedText = metrics.elidedText(text, Qt.ElideRight, self.lineEdit().width())
        self.lineEdit().setText(elidedText)

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

    def addItem(self, text, data=None):
        item = QStandardItem()
        item.setText(text)
        item.setFlags(Qt.ItemIsEnabled | Qt.ItemIsUserCheckable)
        item.setData(Qt.Unchecked, Qt.CheckStateRole)
        self.model().appendRow(item)

    def addItems(self, texts, datalist=None):
        for i, text in enumerate(texts):
            data = datalist[i] if datalist else None
            self.addItem(text, data)

    def currentData(self):
        res = []
        for i in range(self.model().rowCount()):
            if self.model().item(i).checkState() == Qt.Checked:
                res.append(self.model().item(i).data())
        return res