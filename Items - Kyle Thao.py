import random


class Item(object):
    def __init__(self, name, types):
        self.name = name
        self.types = types


class Sword(Item):
    def __init__(self, name, types, blade, damage):
        super(Sword, self).__init__(name, types)
        self.handle = True
        self.blade = blade
        self.damage = damage

    def blade(self, short):
        self.blade = short

    def damage(self):
        self.damage = 10


class ShortSword(Sword):
    def __init__(self):
        super(ShortSword, self).__init__("Short sword", "short", "short", 10)
        self.minimum_damage = 9
        self.max_damage = 12

    def heavy_attack(self):
        return random.randint(self.minimum_damage + 1, self.max_damage)

    def light_attack(self):
        return random.randint(self.minimum_damage, self.minimum_damage + 3)


class LongSword(Sword):
    def __init__(self):
        super(LongSword, self).__init__("Long Sword", "long", "long", 15)
        self.minimum_damage = 15
        self.max_damage = 19

    def heavy_attack(self):
        return random.randint(self.minimum_damage, self.max_damage + 1)

    def light_attack(self):
        return random.randint(self.minimum_damage, self.minimum_damage - 1)


class Stone(Item):
    def __init__(self):
        super(Stone, self).__init__("Stone Piece", "collectible")
        self.can_be_collected = True


class Staff(Item):
    def __init__(self, name,  types, stone):
        super(Staff, self).__init__(name, types)
        self.staff_handle = True
        self.staff_stone = stone
        self.damage = 9


class WoodenStaff(Staff):
    def __init__(self):
        super(WoodenStaff, self).__init__("Wooden Staff", "weak", "weak")
        self.damage = 9

    def wood_spell(self):
        return random.randint(self.damage, self.damage + 1)


class OnyxStaff(Staff):
    def __init__(self):
        super(OnyxStaff, self).__init__("Onyx Staff", "lightning", "strong")
        self.damage = 13

    def lightning_spell(self):
        return random.randint(self.damage + 2, self.damage + 3)


class FireAndIce(Staff):
    def __init__(self):
        super(FireAndIce, self).__init__("Fire and Ice Staff", "fire and ice", "strong")
        self.damage = 20

    def flamethrower(self):
        return random.randint(self.damage, self.damage + 8)

    def blizzaga(self):
        return random.randint(self.damage, self.damage + 5)


my_sword = ShortSword()
my_sword.light_attack()
my_staff = WoodenStaff()
my_staff.wood_spell()
