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
        _number = random.randint(self.minimum_damage + 1, self.max_damage + 3)
        if self.damage > 0:
            print("You swing and hit for", _number)

    def light_attack(self):
        _number = random.randint(self.minimum_damage, self.minimum_damage + 1)
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
        _number = random.randint(self.minimum_damage - 1, self.minimum_damage)
        if self.damage > 0:
            print("You swing and hit for", _number)


class GreatSword(Sword):
    def __init__(self):
        super(GreatSword, self).__init__("Great Sword", "", "heavy", 20)
        self.min_damage = 20
        self.max_damage = 25

    def heavy_attack(self):
        _number = random.randint(self.min_damage, self.max_damage)
        if self.damage > 0:
            print("You swung and hit for", _number)

    def light_attack(self):
        _number = random.randint(self.min_damage - 5, self.min_damage)
        if self.damage > 0:
            print("You swung and hit for", _number)


class Shield(Item):
    def __init__(self, durability, block_damage):
        super(Shield, self).__init__("Shield", "protection")
        self.durability = durability
        self.block_damage = block_damage


class SmallShield(Shield):
    def __init__(self):
        super(SmallShield, self).__init__(20, 5)
        self.damage = input("Damage ")

    def block_damage(self):
        if self.damage > 5:
            print("You block some of the damage but not all.")



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
        _number = random.randint(0, self.damage + 1)
        if _number > 0:
            print("You casted your spell and it hits for", _number)

        else:
            self.damage = 0
            print("You missed")


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

        else:
            self.damage = 0
            print("You missed.")


# ==================================================Instantiated Items==================================================
# Instantiate items
my_sword = ShortSword()
long_sword = LongSword()
great_sword = GreatSword()
small_shield = SmallShield()
wood_staff = WoodenStaff()
onyx_staff = OnyxStaff()
fire_staff = FireStaff()
ice_staff = IceStaff()

# ================================================== Item Upgrades======================================================
my_sword.light_attack()
my_sword.heavy_attack()

long_sword.light_attack()
long_sword.heavy_attack()

great_sword.heavy_attack()
great_sword.light_attack()

wood_staff.wood_spell()

onyx_staff.lightning_spell()

fire_staff.firega()

ice_staff.blizzaga()
