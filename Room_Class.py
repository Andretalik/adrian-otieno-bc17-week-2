class Room(object):
    def __init__(self, room_type, room_name, occupants=None):
        if occupants is None:
            occupants = []
        self.room_type = room_type.lower()
        self.room_name = room_name
        self.occupants = occupants


class Office(Room):
    def __init__(self, room_type, room_name, max_no=6):
        super().__init__(room_type, room_name)
        self.max_no = max_no


class LivingSpace(Room):
    def __init__(self, room_type, room_name, max_no=4):
        super().__init__(room_type, room_name)
        self.max_no = max_no
