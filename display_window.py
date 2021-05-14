from PyQt5.QtWidgets import QDialog, QApplication, QLabel, QPushButton, QVBoxLayout
import sys
from model import Model
from controller import Controller


class DisplayWindow(QDialog):  # use QDialog if want to set layout
    def __init__(self):
        super().__init__()
        self.modify = None
        self.app_version = None
        self.model = Model()
        self.controller = Controller()

        self.customize()
        self.setWindow()

        self.modify.clicked.connect(self.modify_app_version)

    def setWindow(self):
        self.setWindowTitle("Application Version")
        self.setGeometry(100, 100, 400, 300)
        self.show()

# use the controller class to get and set information
    def customize(self):
        self.modify = QPushButton('Modify', self)
        label = self.controller.get_app_version()
        self.app_version = QLabel(label, self)
        vbox = QVBoxLayout(self)
        vbox.addWidget(self.app_version)
        vbox.addWidget(self.modify)
        self.setLayout(vbox)

    def modify_app_version(self):
        pass


app = QApplication(sys.argv)
display_window = DisplayWindow()
sys.exit(app.exec())
