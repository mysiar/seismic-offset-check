from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import Qt
from UIWarning import Ui_UIWarning


class Warning(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_UIWarning()
        self.ui.setupUi(self)

        self.ui.label.setAlignment(Qt.AlignVCenter | Qt.AlignCenter)

    def set_label(self, text):
        self.ui.label.setText(text)
