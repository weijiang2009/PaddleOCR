class MyModule:
    def __init__(self, *args, **kwargs):
        # your init code
        pass

    def __call_(self, data):
        img = data['image']
        label = data['label']
        # your process code

        data['image'] = img
        data['label'] = label
        return data
