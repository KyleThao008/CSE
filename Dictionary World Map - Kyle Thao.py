world_map = {
    'OUTSIDE HOUSE': {
        'NAME': "OUTSIDE",
        'DESCRIPTION': "You are outside a white house and to the north there is an opening to an abandoned basement."
                       "There seems to be some light.",
        'PATHS': {
            'NORTH': "BASEMENT"
        }
    },
    'BASEMENT': {
        'NAME': "ABANDONED BASEMENT",
        'DESCRIPTION': "As you entered the basement, a door closes behind you"
                       "and trap you in the room."
                       "In the room there are a set of weapons on the wall "
                       "and to the east there is a portal that goes somewhere."
                       "The weapons are a sword, a staff, a shield, and a bow and arrow.",
        'PATHS': {
            'EAST': "PORTAL"
        }
    },
    'PORTAL': {
        'NAME': "PORTAL",
        'DESCRIPTION': "You are at a room with a portal. On the wall it says for you "
                       "to find all 10 pieces of the magic stone "
                       "to restore world peace.",
        'PATHS': {
            'EAST': "DUNGEON ROOM 1"
        }
    },
    'DUNGEON ROOM 1': {
        'NAME': "DUNGEON ROOM 1",
        'DESCRIPTION': "You are in a dungeon room and there are goblins and"
                       "ogres in the room. To the north there seems to be an exit"
                       "but is locked and needs a key.",
        'PATHS': {
            'NORTH': "DUNGEON ROOM 2"
        }
    },
    'DUNGEON ROOM 2': {
        'NAME': "DUNGEON ROOM 2",
        'DESCRIPTION': "You are in a room full of skeletons and flying demon bats. There are 2 exits to the north and "
                       "to the west. To the west there seems to be light. There is something shiny on the east side of"
                       "the room.",
        'PATHS': {
            'NORTH': "DUNGEON ROOM 3",
            'WEST': "MERCHANT",
            'EAST': "SHINY",
            'SOUTH': "DUNGEON ROOM 1"
        }
    },
    'DUNGEON ROOM 3': {
        'NAME': "DUNGEON ROOM 3",
        'DESCRIPTION': "You are in a room full of demon dogs and boars that ram you."
                       "One of the dogs is being guarded by other dogs because it has a piece of the stone."
                       "To the west there is a gate that opens to another room.",
        'PATHS': {
            'WEST': "DUNGEON ROOM 4",
            'SOUTH': "DUNGEON ROOM 2"
        }
    },
    'SHINY': {
        'NAME': "SHINY",
        'DESCRIPTION': "There is something shiny here.",
        'PATHS': {
            'WEST': "DUNGEON ROOM 2"
        }
    },
    'MERCHANT': {
        'NAME': "MERCHANT",
        'DESCRIPTION': "There is a merchant in the dungeon that has a lot of armoury. He seems to been "
                       "in here for awhile, surviving with his large amount of weapons. The weapons range from swords "
                       "to staffs.",
        'PATHS': {
            'EAST': "DUNGEON ROOM 2"
        }
    },
    'DUNGEON ROOM 4': {
        'NAME': "DUNGEON ROOM 4",
        'DESCRIPTION': "You are now in a room with a really old man. He doesn't want to fight but he tells you a riddle"
                       " that you have to solve. The riddle is 'Their is a couple and they have 4 daughters and each"
                       " daughter has 1 brother. How many family members are there all together?'",
        'PATHS': {
            'NORTH': "CHEST",
            'WEST': "DUNGEON ROOM 5",
            'EAST': "DUNGEON ROOM 3"
        }
    },
    'CHEST': {
        'NAME': "CHEST ROOM",
        'DESCRIPTION': "There are 7 chests in this room. 3 of them contain the shards to the magic stone."
                       "4 of them contain something else.",
        'PATHS': {
            'SOUTH': "DUNGEON ROOM 4"
        }
    },
    'DUNGEON ROOM 5': {
        'NAME': "DUNGEON ROOM 5",
        'DESCRIPTION': "In this dungeon there are orcs and dire wolves. There is a path to the west that"
                       "seems to lead to a maze. To the north there is another dungeon.",
        'PATHS': {
            'NORTH': "BOSS ROOM",
            'WEST': "MAZE"
        }
    },
    'BOSS ROOM': {
        'NAME': "BOSS ROOM",
        'DESCRIPTION': "In this room you will be fighting a boss. The boss this is the Demon Lord that has "
                       "been sending these monsters at you to fight. Defeat him to get the remaining 3 pieces "
                       "of the Magic Stone.",  # once entered can't come go back out.
        'PATHS': {
            'NORTH': "PORTAL ROOM 2"
        }
    },
    'PORTAL ROOM 2': {
        'NAME': "PORTAL ROOM 2",
        'DESCRIPTION': "This portal takes you to the final room.",
        'PATHS': {
            'NORTH': "FINAL ROOM"
        }
    },
    'FINAL ROOM': {
        'NAME': "FINAL ROOM",
        'DESCRIPTION': "",
    }
}

current_node = world_map["OUTSIDE HOUSE"]
directions = ["NORTH", "SOUTH", "EAST", "WEST", "UP", "DOWN"]
playing = True
portal_setting = 0
NUM_OF_PORTAL_OPTIONS = 2

# Controller
while playing:
    print(current_node["NAME"])
    print(current_node["DESCRIPTION"])
    command = input(">_")
    if command.lower() in ['q',  'quit', 'exit']:
        playing = False
    elif command in directions:
        try:
            room_name = current_node['PATHS'][command.upper()]
            current_node = world_map[room_name]
        except KeyError:
            print("I can't go that way.")
    elif "change" in command and current_node == world_map['PORTAL']:
        if portal_setting % NUM_OF_PORTAL_OPTIONS == 0:
            world_map['PORTAL']['PATHS']["NORTH"] = 'DUNGEON ROOM 1'
            print("The portal shows a dungeon room.")
        elif portal_setting % NUM_OF_PORTAL_OPTIONS == 1:
            del world_map['PORTAL']['PATHS']["NORTH"]
            print("The portal shows the the basement.")
        portal_setting += 1
    else:
        print("Command not recognized")
