from PyQt5.QtWidgets import QDialog, QLabel, QPushButton, QVBoxLayout
from PyQt5.QtCore import pyqtSlot

from modify_window import ModifyWindow
import sys


class DisplayWindow(QDialog):  # use QDialog if want to set layout
    def __init__(self, controller, model):
        super().__init__()

        self.app_version = None
        self.modify = None
        self.cancel = None

        self.controller = controller
        self.model = model
        self.modify_window = None

        self.customize()
        self.setWindow()

        self.modify.clicked.connect(self.modify_data)
        self.controller.data.connect(self.save_content)
        self.cancel.clicked.connect(sys.exit)

    def setWindow(self):
        self.setWindowTitle("Application Version")
        self.setGeometry(100, 100, 600, 500)
        self.show()

    def customize(self):
        label = self.model.access("app_version")
        self.app_version = QLabel(self)
        self.app_version.setText(label)
        self.modify = QPushButton('Modify', self)
        self.cancel = QPushButton('Cancel', self)
        vbox = QVBoxLayout(self)
        vbox.addWidget(self.app_version)
        vbox.addWidget(self.modify)
        vbox.addWidget(self.cancel)
        self.setLayout(vbox)

    def modify_data(self):
        self.modify_window = ModifyWindow(self.controller, self.model)

    @pyqtSlot(str)
    def save_content(self, new_data):
        self.app_version.setText(new_data)
