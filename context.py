import json


class Context:
    def __init__(self):

        self.file_name = 'data.json'
        self. product_info = {}

    def load(self):
        with open(self.file_name, 'r') as file:
            self.product_info = json.load(file)
            file.close()
            # return self.product_info

    def save(self):
        with open(self.file_name, 'w') as file:
            json.dump(self.product_info, file, indent=4)
            file.close()


# context = Context()
# context.load()
# context.save()
# print(context.product_info)
