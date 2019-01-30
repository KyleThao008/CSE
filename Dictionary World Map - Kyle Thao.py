world_map = {
    'R19A': {
        'NAME': "Wiebe's Classroom",
        'DESCRIPTION': "This is the classroom that you are in right now. "
                       "It has two exits to the north side.",
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
