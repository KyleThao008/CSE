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


class Stone(Item):
    def __init__(self):
        super(Stone, self).__init__("Stone Piece", "collectible")
        self.can_be_collected = True
        self.weight = 1


class Staff(Item):
    def __init__(self, name,  types, stone):
        super(Staff, self).__init__(name, types)
        self.staff_handle = True
        self.staff_stone = stone
        self.damage = 9


class WoodenStaff(Staff):
    def __init__(self):
        super(WoodenStaff, self).__init__("Wooden Staff", "weak", "weak")
        self.damage = 14

    def wood_spell(self):
        _number = random.randint(0, self.damage + 1)
        if _number > 0:
            print("You casted your spell a GIANT TREE appears. They are launched towards the enemy "
                  "and it hits for", _number)

        else:
            self.damage = 0
            print("The trees missed the enemy?")


class OnyxStaff(Staff):
    def __init__(self):
        super(OnyxStaff, self).__init__("Onyx Staff", "lightning", "strong")
        self.max_damage = 13

    def lightning_spell(self):
        _number = random.randint(0, self.max_damage)
        if _number > 0:
            print("You casted your spell and a WILD ZAPDOS APPEARS??? It uses lightning bolt and it hits for", _number)

        else:
            self.damage = 0
            print("Zapdos misses its lightning bolt.")


class FireStaff(Staff):
    def __init__(self):
        super(FireStaff, self).__init__("Fire Staff", "fire", "strong")
        self.max_damage = 10

    def firega(self):
        _number = random.randint(0, self.max_damage)
        if self.damage > 0:
            print("You casted your spell and it spawns a Moltres. Moltres uses flamethrower and it hits for ", _number)

        else:
            self.damage = 0
            print("Moltres misses his flamethrower attack.")


class IceStaff(Staff):
    def __init__(self):
        super(IceStaff, self).__init__("Ice Staff", "ice", "strong")
        self.max_damage = 15

    def blizzaga(self):
        if self.damage > 0:
            print("You casted your spell and a ice block spawns on top of the enemy. "
                  "It hit for", random.randint(0, self.max_damage))

        else:
            self.damage = 0
            print("You missed.")


class Axe(Item):
    def __init__(self, name, types, damage, axe_head):
        super(Axe, self).__init__(name, types)
        self.damage = damage
        self.axe_head = axe_head
        self.handle = True


class SmallAxe(Axe):
    def __init__(self):
        super(SmallAxe, self).__init__("Small Axe", "small", 10, "small")
        self.max_damage = 10

    def attack(self):
        if self.damage > 0:
            print("You attack and hit for", random.randint(0, self.max_damage))


class WolfAxe(Axe):
    def __init__(self):
        super(WolfAxe, self).__init__("Wolf Axe", "wolf", 13, "medium")
        self.min_damage = 10
        self.max_damage = 13

    def spin_attack(self):
        if self.damage > 0:
            print("You spin around in a circle and hit a an enemy", random.randint(1, 4), "times and it does",
                  random.randint(0, 13))

        else:
            self.damage = 0
            print("You spin and miss.")

    def heavy_attack(self):
        _number = random.randint(self.min_damage, self.max_damage)
        if self.damage > 0:
            print("You swung and hit for", _number)

    def light_attack(self):
        _number = random.randint(self.min_damage - 5, self.min_damage)
        if self.damage > 0:
            print("You swung and hit for", _number)


class DariusAxe(Axe):
    def __init__(self):
        super(DariusAxe, self).__init__("The Legendary Axe of Darius", "legendary", 1000, "large")
        self.min_damage = 1000
        self.max_damage = 1999

    def spin_attack(self):
        if self.damage > 0:
            print("You spin around and hit for", random.randint(self.min_damage, self.max_damage))

    def heavy_attack(self):
        if self.damage > 0:
            print("You launch the axe at the enemy and it does", random.randint(self.min_damage, self.max_damage))

    def light_attack(self):
        if self.damage > 0:
            print("You hit for", self.min_damage)


class Katana(Sword):
    def __init__(self):
        super(Katana, self).__init__("Katana", "long", "slim", 14)
        self.min_damage = 14
        self.max_damage = 19

    def poke(self):
        if self.damage > 0:
            print("You use your sword to stab the enemy and it hit for", random.randint(0, self.min_damage))

        else:
            self.damage = 0
            print("You try to stab your enemy and miss.")


class HolySword(Sword):
    def __init__(self):
        super(HolySword, self).__init__("THE holy GIANT sword", "holy", "GIANT", 10000)
        self.min_damage = 10000
        self.max_damage = 7777777777

    def grant_me_power(self):
        if self.damage is 10000:
            self.damage += 9999
            print("The Holy spirits have given you power.")


class BusterSword(Sword):
    def __init__(self):
        super(BusterSword, self).__init__("Buster Sword", "strong", "giant", 20)
        self.min_damage = 20
        self.max_damage = 40

    def many_attack(self):
        if self.damage > 0:
            print("You hit the enemy", random.randint(0, 10), "times and hit for", random.randint(self.min_damage,
                                                                                                  self.max_damage))

        else:
            if self.damage is 0:
                print("You try to attack and miss.")

    def large_swing(self):
        if self.damage > 0:
            print("You hit for", self.max_damage)

        else:
            print("You swing and miss.")


class Rapier(Sword):
    def __init__(self):
        super(Rapier, self).__init__("Rapier", "fast", "skinny", 15)
        self.min_damage = 15
        self.max_damage = 20

    def quick_attack(self):
        if self.damage > 0:
            print("You attack the enemy so fast that the enemy becomes confused.")


class BigBone(Sword):
    def __init__(self):
        super(BigBone, self).__init__("Big Bone", "big", "Bone", 10)
        self.min_damage = 10
        self.max_damage = 15

    def bone_toss(self):
        if self.damage > 0:
            print("You toss your big bone and hit for", random.randint(0, self.min_damage, self.min_damage + 2))

        else:
            self.damage = 0
            print("You potato. How do you miss with a huge bone thing?")


class SupportStaff(Staff):
    def __init__(self):
        super(SupportStaff, self).__init__("Support Staff", "summon", "strong")
        self.min_damage = 10
        self.max_damage = 15

    def minions(self):
        if self.damage > 0:
            print("You summon minions to attack your enemy. They hit the enemy for", random.randint(self.min_damage,
                                                                                                    self.max_damage))


# ===================================================Instantiated Items=================================================
my_sword = ShortSword()
long_sword = LongSword()
small_axe = SmallAxe()
wolf_axe = WolfAxe()
katana = Katana()
rapier = Rapier()
great_sword = GreatSword()
wood_staff = WoodenStaff()
onyx_staff = OnyxStaff()
fire_staff = FireStaff()
ice_staff = IceStaff()
darius_axe = DariusAxe()
bone = BigBone()
support = SupportStaff()

# =====================================================Item Commands====================================================
my_sword.light_attack()
my_sword.heavy_attack()

bone.bone_toss()

long_sword.light_attack()
long_sword.heavy_attack()

rapier.quick_attack()

great_sword.heavy_attack()
great_sword.light_attack()

small_axe.attack()

katana.poke()

wolf_axe.light_attack()
wolf_axe.heavy_attack()
wolf_axe.spin_attack()

darius_axe.spin_attack()
darius_axe.light_attack()
darius_axe.heavy_attack()

wood_staff.wood_spell()

onyx_staff.lightning_spell()

fire_staff.firega()

ice_staff.blizzaga()

support.minions()
