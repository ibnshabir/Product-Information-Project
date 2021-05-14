"""
    - get the label title for DisplayWindow from Model
"""
from model import Model
from modify_window import ModifyWindow

class Controller:
    def __init__(self):
        self.model = Model()
        self.modify_window = ModifyWindow() # connected it with modify button

    def get_app_version(self):
        return self.model.app_data["application_version"]

# controller = Controller()
# controller.get_app_version()