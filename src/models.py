class Character:
    name: str

    def __init__(self, **kwargs):
        self.set_name(kwargs.get('name', ''))

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name
