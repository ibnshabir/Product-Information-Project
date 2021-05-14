import json

# this information can come from the window via controller
new_data = {
    "application_version": "1.0.1"
}


class Model:
    def __init__(self):

        self.app_data = []

        self.load('data.json')

    def load(self, file_name):
        with open(file_name, 'r') as file:
            self.app_data = json.load(file)
        return self.app_data

    def save(self, file_name):
        with open("data.json", "r+") as file:
            data = json.load(file)
            data.update(file_name)
            file.seek(0)
            json.dump(data, file, indent=4)

# model = Model()
# print(model.load('data.json'))
# model.save(new_data)
