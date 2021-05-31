

class Model:
    def __init__(self, context):
        self.content = None

        self.context = context
        self.context.load()

    def access(self, key):
        self.context.load()
        self.content = self.context.app_info[key]
        return self.content

    def modify(self, key, new_data):
        self.context.app_info[key] = new_data
        self.context.save()