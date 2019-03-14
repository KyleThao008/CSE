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
        _number = random.randint(self.minimum_damage + 1, self.max_damage)
        if self.damage > 0:
            print("You swing and hit for", _number)

    def light_attack(self):
        _number = random.randint(self.minimum_damage, self.max_damage)
        if self.damage > 0:
            print("You swing and hit for", _number)


class LongSword(Sword):
    def __init__(self):
        super(LongSword, self).__init__("Long Sword", "long", "long", 15)
        self.minimum_damage = 15
        self.max_damage = 19

    def heavy_attack(self):
        _number = random.randint(self.minimum_damage, self.max_damage + 1)
        if self.damage > 0:
            print("You swing and you hit for", _number)

    def light_attack(self):
        _number = random.randint(self.minimum_damage, self.minimum_damage - 1)
        if self.damage > 0:
            print("You swing and hit for", _number)


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
        self.max_damage = 13

    def lightning_spell(self):
        _number = random.randint(0, self.max_damage)
        if _number > 0:
            print("You casted your spell and it hits for", _number)

        else:
            self.damage = 0
            print("You missed")


class FireStaff(Staff):
    def __init__(self):
        super(FireStaff, self).__init__("Fire Staff", "fire", "strong")
        self.max_damage = 10

    def firega(self):
        _number = random.randint(0, self.max_damage)
        if self.damage > 0:
            print("You casted your spell and it hit for", _number)

        else:
            self.damage = 0
            print("You missed.")


class IceStaff(Staff):
    def __init__(self):
        super(IceStaff, self).__init__("Ice Staff", "ice", "strong")
        self.max_damage = 15

    def blizzaga(self):
        if self.damage > 0:
            print("You casted your spell and it hit for", random.randint(0, self.max_damage))


# ==================================================Instantiated Items==================================================
# Instantiate items
my_sword = ShortSword()
long_sword = LongSword()
wood_staff = WoodenStaff()
onyx_staff = OnyxStaff()
fire_staff = FireStaff()
ice_staff = IceStaff()

# ================================================== Item Upgrades======================================================
my_sword.light_attack()
my_sword.heavy_attack()
long_sword.light_attack()
long_sword.heavy_attack()
wood_staff.wood_spell()
onyx_staff.lightning_spell()
fire_staff.firega()
ice_staff.blizzaga()
