class Room(object):
    def __init__(self, room_type, room_name, occupants=None):
        if occupants is None:
            occupants = []
        self.room_type = room_type.lower()
        self.room_name = room_name
        self.occupants = occupants


class Office(Room):
    def __init__(self, room_type, room_name):
        super().__init__(room_type, room_name)


class LivingSpace(Room):
    def __init__(self, room_type, room_name):
        super().__init__(room_type, room_name)
