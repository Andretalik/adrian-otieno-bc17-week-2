class Person(object):
    def __init__(self, person_name, person_type, wants_accommodation):
        self.person_name = person_name
        self.person_type = person_type.lower()
        self.wants_accommodation = wants_accommodation.lower()


class Fellow(Person):
    pass


class Staff(Person):
    pass