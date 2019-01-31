world_map = {
    'OUTSIDE HOUSE': {
        'NAME': "OUTSIDE",
        'DESCRIPTION': "You are outside a white house and there is an opening to an abandoned basement."
                       "There seems to be some light.",
        'PATHS': {
            'NORTH': "PARKING_LOT"
        }
    },
    'PARKING_LOT': {
        'NAME': "The Edison Parking Lot",
        'DESCRIPTION': "There Are cars parked here."
                       "To the south is Mr. Wiebe's room.",
        'PATHS': {
            'SOUTH': "R19A"
        }
    }
}

current_node = world_map["OUTSIDE HOUSE"]
directions = ["NORTH", "SOUTH", "EAST", "WEST", "UP", "DOWN"]
playing = True

# Controller
while playing:
    print(current_node["NAME"])
    command = input(">_")
    if command.lower() in ['q',  'quit', 'exit']:
        playing = False
    try:
        room_name = current_node['PATHS'][command.upper()]
        current_node = world_map[room_name]
    except KeyError:
        print("I can't go that way.")
    else:
        print("Command not recognied")