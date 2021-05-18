from context import Context


class Model:
    def __init__(self, context):
        self.content = None

        self.context = context
        self.context.load()

    def access(self, key):
        self.context.load()
        self.content = self.context.product_info[key]
        return self.content

    def modify(self, key, new_data):
        self.context.product_info[key] = new_data
        self.context.save()


# model = Model()
# print(model.access("app_version"))
# model.modify("app_version", "000000")
# model.add_data("hw_version", 12345)
# print(model.access("app_version"))
