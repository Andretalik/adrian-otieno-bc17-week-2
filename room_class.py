class Room(object):
    def __init__(self, room_type, room_name, occupants=None):
        if occupants is None:
            occupants = []
        self.room_type = room_type.lower()
        self.room_name = room_name
        self.occupants = occupants


class Office(Room):
    def __init__(self, room_type, room_name):
        super(Office, self).__init__(room_type, room_name)
        self.max_no = 6


class LivingSpace(Room):
    def __init__(self, room_type, room_name):
        super(LivingSpace, self).__init__(room_type, room_name)
        self.max_no = 4
