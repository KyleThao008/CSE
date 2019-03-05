class Item(object):
    def __init__(self, name, types):
        self.name = name
        self.types = types


class Swords(object):
    def __init__(self, handle, blade, damage):
        self.handle = handle
        self.blade = blade
        self.damage = damage

    def handle(self):
        self.handle = True
