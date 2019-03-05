class Room(object):
    def __init__(self, name, description="", north=None, south=None, east=None, west=None, up=None, down=None):
        self.name = name
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.up = up
        self.down = down
        self.description = description


Outside = Room("Outside", "You are outside a white house and to the north there is an opening to an abandoned basement."
                          " There seems to be light inside.")

Basement = Room('Basement', "As you entered the basement, a door closes behind you, trapping you in the room."
                            "In the room there are a set of weapons on the wall and to the east there is a portal "
                            "that goes somewhere. The weapons are a sword, a staff, a shield, and a bow and arrow.")

Portal = Room('Portal', "You are at a room with a portal. On the wall it says for you to find all 10 pieces of the"
                        "Magic Stone to restore world piece.")

Dungeon1 = Room('Dungeon Room 1', "You are in a dungeon room and there are goblins and"
                                  "ogres in the room. To the north there seems to be an exit"
                                  "but is locked and needs a key.")

Dungeon2 = Room('Dungeon Room 2', "You are in a room full of skeletons and flying demon bats."
                                  " There are 2 exits to the north, east, and west. To the west there seems to be "
                                  "light. There is something shiny to the east.")

Merchant = Room('Merchant', "There is a merchant in the dungeon that has a lot of armoury. He seems to been "
                            "in here for awhile, surviving with his large amount of weapons. The weapons range "
                            "from swords to staffs.")

EastRoom = Room('East Room', "There something very shiny in here.")

Dungeon3 = Room('Dungeon Room 3', "You are in a room full of demon dogs and boars that ram you."
                                  "One of the dogs is being guarded by other dogs because it has a piece of the "
                                  "stone. To the west there is a gate that opens to another room.")

Dungeon4 = Room('Dungeon Room 4', "You are now in a room with a really old man. He doesn't want to fight but he tells "
                                  "you a riddle that you have to solve. To the North there is a chest room. To the west"
                                  "it leads to another dungeon. Once you finish answering th riddle, the man will give"
                                  " you a piece of the magic stone."
                                  " The riddle is 'Their is a couple and they have 4 daughters and each daughter has "
                                  "1 brother. How many family members are there all together?'")

Dungeon5 = Room('Dungeon Room 5', "In this dungeon there are orcs and dire wolves. There is a path to the west that"
                                  "seems to lead to a maze. To the north there is another dungeon.")

Chest = Room('Chest Room', "In this room there are 7 chests and in 3 of them there are pieces of the stone in them."
                           " You have 3 chances to guess the chests that have the stone in them. If you choose the"
                           " wrong 3 a force field pushes you out of the room. Re enter anc choose again. They are "
                           "randomized each fail.")

Maze = Room('Maze', "You are in the maze and there is a rope that goes up somewhere")

MazeUp = Room('Attic Room', "You climb the rope up to the Attic room and there is a chest in here. In the chest you "
                            "find 2 pieces of the stone.")

BossRoom = Room('Dungeon Boss', "In this room you will be fighting a boss. The boss this is the Demon Lord that has "
                                "been sending these monsters at you to fight. Defeat him to get the remaining 3 pieces"
                                "of the Magic Stone.")  # Defeat boss and then portal. Portal is north.

Portal2 = Room('Portal', "This portal takes you to the final room.")

FinalRoom = Room('The Final Room', "Congratulations on defeating the boss. In this room there is a display case and a "
                                   "portal. Once you put all of the pieces of the magic stone into the display case "
                                   "and then walk through the portal to finish the game.")

Case = Room('Display Case', "Put pieces of magic stone in here")  # pieces in case, another portal *north*

Portal3 = Room('Portal', "Walk through to finish.")

Outside.north = Basement
Basement.east = Portal
Portal.east = Dungeon1
Dungeon1.north = Dungeon2
Dungeon2.north = Dungeon3
Dungeon2.east = EastRoom
EastRoom.west = Dungeon2
Dungeon2.south = Dungeon1
Dungeon2.west = Merchant
Merchant.east = Dungeon2
Dungeon3.west = Dungeon4
Dungeon3.south = Dungeon2
Dungeon4.north = Chest
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


class Player(object):
    def __init__(self, starting_location, current_class):
        self.health = 100
        self.current_location = starting_location
        self.player_class = current_class
        self.inventory = []

    def move(self, new_location):
        """This method moves a character to a new location

        :param new_location: The variable containing a room object
        """
        self.current_location = new_location


player = Player(Outside, "")
playing = True
directions = ['north', 'east', 'south', 'west', 'up', 'down']
portal_setting = 0
NUM_OF_PORTAL_OPTIONS = 2

# Controller
while playing:
    print(player.current_location.name)
    print(player.current_location.description)
    command = input(">_")
    if command.lower() in ['q',  'quit', 'exit']:
        playing = False
    elif command.lower() in directions:
        try:
            room_object_that_we_move_to = getattr(player.current_location, command)
            player.move(room_object_that_we_move_to)
        except KeyError:
            print("I can't go that way.")
    elif "change" in command and player.current_location == Portal:
        if portal_setting % NUM_OF_PORTAL_OPTIONS == 0:
            Portal.north = Dungeon1
            print("The portal shows a dungeon room.")
        elif portal_setting % NUM_OF_PORTAL_OPTIONS == 1:
            Portal.north = None
            print("The portal shows the the basement.")
        portal_setting += 1
    else:
        print("Command not recognized")
