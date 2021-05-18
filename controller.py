from PyQt5.QtCore import QObject, pyqtSlot, pyqtSignal
from model import Model


class Controller(QObject):
    data = pyqtSignal(str)

    def __init__(self, model):
        super(Controller, self).__init__()
        self.model = model

        self.data.connect(self.modify_content)

    @pyqtSlot(str)
    def modify_content(self, new_data):
        self.model.modify("app_version", new_data)

    def add_data(self, key, content):
        self.model.context.product_info[key] = content
        self.model.context.save()