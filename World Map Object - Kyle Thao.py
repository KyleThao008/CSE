import random

from termcolor import colored


def fight(enemy):
    print("A wild %s appears!" % enemy.name)
    while player.health > 0 and enemy.health > 0:
        input("Press any key to attack")
        player.attack(enemy)
        if enemy.health > 0:
            enemy.attack(player)
        if player.health <= 0:
            print("GAME OVER")
            quit(0)


class Room(object):
    def __init__(self, name, description="", north=None, south=None, east=None, west=None, up=None, down=None,
                 items=None, enemies=None):
        if enemies is None:
            enemies = []
        self.name = name
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.up = up
        self.down = down
        self.description = description
        self.items = items
        self.enemies = enemies


class Item(object):
    def __init__(self, name):
        self.name = name


class Weapon(Item):
    def __init__(self, name, damage):
        super(Weapon, self).__init__(name)
        self.damage = damage


class Character(object):
    def __init__(self, name, health, weapon, armor):
        self.name = name
        self.health = health
        self.weapon = weapon
        self.armor = armor

    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0
        print("%s has %d health left." % (self.name, self.health))

    def attack(self, target):
        print("%s attacks %s for %d damage" % (self.name, target.name, self.weapon.damage))
        target.take_damage(self.weapon.damage)


class Player(object):
    def __init__(self, starting_location, current_class, pick_up, drop, use, weapon):
        self.health = 100
        self.name = "Player"
        self.current_location = starting_location
        self.player_class = current_class
        self.inventory = []
        self.pick_up = pick_up
        self.drop = drop
        self.weapon = weapon
        self.max_hp = 100
        self.use = True

    def move(self, new_location):
        """This method moves a character to a new location

        :param new_location: The variable containing a room object
        """
        if new_location is not None:
            self.current_location = new_location
        else:
            print("You can't go that way")

    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0
        print("%s has %d health left." % (self.name, self.health))

    def attack(self, target):
        print("%s attacks %s for %d damage" % (self.name, target.name, self.weapon.damage))
        target.take_damage(self.weapon.damage)

    def has_weapon(self):
        for item in self.inventory:
            if issubclass(type(item), Weapon):
                return True
        return False

    def recover(self):
        self.health += 35
        if self.health > self.max_hp:
            self.health = self.max_hp


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


class Stone(Item):
    def __init__(self):
        super(Stone, self).__init__("Stone Piece", "collectible")
        self.can_be_collected = True
        self.weight = 1


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


class OmegaAxe(Axe):
    def __init__(self):
        super(OmegaAxe, self).__init__("The Legendary Axe of the Omega", "legendary", 1000, "large")
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


class Orc(Character):
    def __init__(self):
        super(Orc, self).__init__("Orc", 100, sword, '')


class Goblin(Character):
    def __init__(self):
        super(Goblin, self).__init__("Goblin", 50, sword, '')


class Ogre(Character):
    def __init__(self):
        super(Ogre, self).__init__("Ogre", 100, small_axe, '')


class Bat(Character):
    def __init__(self):
        super(Bat, self).__init__("Bat", 100, Fists, '')


class Skeleton(Character):
    def __init__(self):
        super(Skeleton, self).__init__("Skeleton", 100, small_axe, '')


class DemonDog(Character):
    def __init__(self):
        super(DemonDog, self).__init__("Demon Dog", 75, Bite(), '')


class Fists(Weapon):
    def __init__(self):
        super(Fists, self).__init__("Fists", 1)


class Bite(Weapon):
    def __init__(self):
        super(Bite, self).__init__("Bite", 5)


class Heal(Item):
    def __init__(self, name, types, heal):
        super(Heal, self).__init__(name, types)
        self.heal = heal


class SmallPotion(Heal):
    def __init__(self):
        super(SmallPotion, self).__init__("Small Potion", 'weak', 35)


# ===================================================Instantiated Items=================================================
sword = ShortSword()
long_sword = LongSword()
small_axe = SmallAxe()
wolf_axe = WolfAxe()
katana = Katana()
omega_axe = OmegaAxe()

# NUMBER 22 ============================================Rooms===========================================================

Outside = Room("Outside", "You are outside a white house and to the north there is an opening to an abandoned basement."
                          "\nThere seems to be light inside.")

Basement = Room('Basement', "As you entered the basement, a door closes behind you, trapping you in the room.\n"
                            "In the room there are a set of weapons on the wall and to the east there is a portal\n"
                            "that goes somewhere.", None, None, True, None, None, None,
                [sword, small_axe, SmallPotion(), Stone()])

Portal = Room('Portal', "You are at a room with a portal. On the wall it says for you to find all 10 pieces of the\n"
                        "Magic Stone to restore world piece.")

Dungeon1 = Room('Dungeon Room 1', "You are in a dungeon room and there are goblins and"
                                  "ogres in the room. To the north there seems to be an exit.", None, None, None, None,
                None, None, None, [Ogre(), Goblin()])

Dungeon2 = Room('Dungeon Room 2', "You are in a room full of skeletons and flying demon bats.\n"
                                  "There are 2 exits to the north, east, and west. To the west there seems\n"
                                  "to be spooky red lights.",
                True, True, True, True, None, None, [], [DemonDog(), Bat()])

Merchant = Room('Merchant', "There is a merchant in the dungeon that has a lot of armoury. He seems to been\n"
                            "in here for awhile, surviving with his large amount of weapons. The weapons range\n"
                            "from swords to staffs.", None, None, True, None, None, None, [wolf_axe, katana,
                                                                                           long_sword])

EastRoom = Room('East Room', "There it is empty here.", None, None, None,
                True, None, None, None, None)

Dungeon3 = Room('Dungeon Room 3', "You are in a room full of demon dogs and boars that ram you.\n"
                                  "To the west there is a gate that opens to another room.", None, None, True,
                True, None, None, None, None)

Dungeon4 = Room('Dungeon Room 4', "You are now in a room with a really old man. He doesn't want to fight but he tells\n"
                                  "you a riddle that you have to solve. To the North there is a chest room. To the west"
                                  "it leads to another dungeon. Once you finish answering th riddle, the man will give"
                                  " you a key"
                                  " The riddle is 'Their is a couple and they have 4 daughters and each daughter has\n "
                                  "1 brother. How many family members are there all together?'")

Dungeon5 = Room('Dungeon Room 5', "In this dungeon there are orcs and dire wolves. There is a path to the west that\n"
                                  "seems to lead to a maze. To the north there is another dungeon.")

Maze = Room('Maze', "You are in the maze and there is a rope that goes up somewhere")

MazeUp = Room('Attic Room', "You climb the rope up to the Attic room and there is a  ", None, None, None, None, None,
              True, [OmegaAxe], None)

BossRoom = Room('Dungeon Boss', "In this room you will be fighting a boss. The boss this is the Demon Lord that has "
                                "been sending these monsters at you to fight. Defeat him to get the remaining 3 pieces"
                                "of the Magic Stone.")  # Defeat boss and then portal. Portal is north.

Portal2 = Room('Portal', "This portal takes you to the final room.")

FinalRoom = Room('The Final Room', "Congratulations on defeating the boss. In this room there is a display case and a "
                                   "portal. Once you put all of the pieces of the magic stone into the display case "
                                   "and then walk through the portal to finish the game.")

Case = Room('Display Case', "Put pieces of magic stone in here")  # pieces in case, another portal *north*

Portal3 = Room('Portal', "Walk through to finish.")

# ==================================================Instantiated Rooms==================================================
Outside.north = Basement
Basement.east = Portal
Portal.east = Dungeon1
Portal.west = Basement
Dungeon1.north = Dungeon2
Dungeon2.north = Dungeon3
Dungeon2.east = EastRoom
EastRoom.west = Dungeon2
Dungeon2.south = Dungeon1
Dungeon2.west = Merchant
Merchant.east = Dungeon2
Dungeon3.west = Dungeon4
Dungeon3.south = Dungeon2
Dungeon4.west = Dungeon5
Dungeon4.east = Dungeon3
Dungeon5.west = Maze
Maze.up = MazeUp
MazeUp.down = Maze
Dungeon5.north = BossRoom
BossRoom.north = Portal2
Portal2.north = FinalRoom
FinalRoom.west = Case
Case.north = Portal3
Portal3.north = Portal3
# ======================================================================================================================


player = Player(Outside, "", pick_up=True, drop=True, weapon=True, use=True)
playing = True
directions = ['north', 'east', 'south', 'west', 'up', 'down']
short_directions = ['n', 'e', 's', 'w', 'u', 'd']
portal_setting = 0
NUM_OF_PORTAL_OPTIONS = 2
player.weapon = Fists()

# Controller
while playing:
    print(colored(player.current_location.name, 'yellow'))
    print(player.current_location.description)

    while len(player.current_location.enemies) > 0:
        fight(player.current_location.enemies[0])
        player.recover()
        player.current_location.enemies.pop(0)

    if player.current_location.items is not None:
        print("The following items are in the room:")
        for num, item in enumerate(player.current_location.items):
            print(str(num + 1) + ": " + item.name)

    command = input(">_")

    if command.lower() in short_directions:
        pos = short_directions.index(command.lower())
        command = directions[pos]

    if command.lower() in ['q',  'quit', 'exit']:
        playing = False
    elif command.lower() in directions:
        try:
            room_object_that_we_move_to = getattr(player.current_location, command)
            player.move(room_object_that_we_move_to)
        except KeyError:
            print(colored("I can't go that way.", 'red'))
    elif "change" in command and player.current_location == Portal:
        if portal_setting % NUM_OF_PORTAL_OPTIONS == 0:
            Portal.north = Dungeon1
            print("The portal shows a dungeon room.")
        elif portal_setting % NUM_OF_PORTAL_OPTIONS == 1:
            Portal.north = None
            print("The portal shows the the basement.")
        portal_setting += 1

    elif "take " in command:
        item_name = command[5:]
        item_object = None

        for item in player.current_location.items:
            if item.name == item_name:
                item_object = item

        if item_object is not None:
            player.inventory.append(item_object)
            player.current_location.items.remove(item_object)
            print("You added to your inventory.")

    elif "drop " in command:
        item_name = command[5:]
        item_object = None

        for item in player.inventory:
            if item.name == item_name:
                item_object = item

        if item_object is not None:
            player.inventory.remove(item_object)
            player.current_location.items.append(item_object)
            print("1")

    elif "inventory" in command:
        if player.inventory is not None:
            print("The following items are in your inventory:")
            for num, item in enumerate(player.inventory):
                print(str(num + 1) + ": " + item.name)

    elif "equip " in command:
        item_name = command[6:]
        item_object = None

        for item in player.inventory:
            if issubclass(type(item_object), Weapon) and player.has_weapon():
                print("You are already carrying a weapon")
            if item.name == item_name:
                item_object = item

        if item_object is not None:
            print("Equipped.")
            player.weapon = item_object

    elif "equipment" in command:
        if player.weapon is not None:
            print("You have equipped a", player.weapon.name)

    elif "health" in command:
        if player.health > 0:
            print("You have", player.health, "health.")

    elif "use " in command:
        item_name = command[4:]
        item_object = None

        for item in player.inventory:
            if item.name == item_name:
                item_object = item

        if issubclass(type(item_object), Heal):
            if player.health < 50:
                player.health += item_object.heal
                print("You have healed for", item_object.heal, "You now have", player.health), "health."
            if player.health > 50:
                player.health += item_object.heal
                print("You used a potion and it gave you", colored(item_object.heal, 'red'),
                      "health. You now have", colored(player.health, 'red'), "health.")
    else:
        print(colored("Command not recognized", 'red'))
