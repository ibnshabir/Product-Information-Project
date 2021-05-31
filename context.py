import json


class Context:
    def __init__(self):

        self.file_name = 'data.json'
        self. app_info = {}

    def load(self):
        with open(self.file_name, 'r') as file:
            self.app_info = json.load(file)
            file.close()

    def save(self):
        with open(self.file_name, 'w') as file:
            json.dump(self.app_info, file, indent=4)
            file.close()