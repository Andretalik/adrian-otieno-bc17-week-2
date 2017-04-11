class Room(object):
    def __init__(self, room_type, room_name):
        self.room_type = room_type.lower()
        self.room_name = room_name


class Office(Room):
    pass


class LivingSpace(Room):
    pass
