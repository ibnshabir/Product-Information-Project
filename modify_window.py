from PyQt5.QtWidgets import QDialog, QPushButton, QLabel, QVBoxLayout, QLineEdit


class ModifyWindow(QDialog):
    def __init__(self, controller, model):
        super().__init__()

        self.modify_data = None
        self.edit_text = None
        self.apply = None
        self.cancel = None
        self.new_data = None

        self.model = model
        self.controller = controller

        self.customize()
        self.setWindow()

        self.apply.clicked.connect(self.set_content)
        self.cancel.clicked.connect(self.close)

    def setWindow(self):
        self.setWindowTitle("Modify Application Version")
        self.setGeometry(800, 100, 600, 500)
        self.show()

    def customize(self):
        self.apply = QPushButton('Apply', self)
        label = self.model.access("app_version")
        self.modify_data = QLabel(label, self)
        self.edit_text = QLineEdit(self)
        self.edit_text.setText(label)
        self.cancel = QPushButton('Cancel', self)
        vbox = QVBoxLayout(self)
        vbox.addWidget(self.modify_data)
        vbox.addWidget(self.edit_text)
        vbox.addWidget(self.apply)
        vbox.addWidget(self.cancel)
        self.setLayout(vbox)

    def set_content(self):
        self.new_data = self.edit_text.text()
        self.modify_data.setText(self.new_data)
        self.controller.data.emit(self.new_data)
        self.close()
