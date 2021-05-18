import json

data = {
    "application_version": "1.0.1",
    "hardware_version": "Asd123"
}


class Context:
    def __init__(self):

        self.file_name = 'data.json'
        self.app_version = None
        self. product_info = []



    def load(self):
        with open(self.file_name, 'r') as file:
            data = json.load(file)
            return data

    def save(self):
        with open(self.file_name, 'w') as file:
            json.dump(data, file, indent=4)


model = Model()
print(model.load())
model.modify_content("2.1.0")
model.add_data("software_version", "A12345")
print(model.get_app_version())
model.save()
print(model.product_info)
