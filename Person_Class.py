class Person(object):
    def __init__(self, person_name, person_type, wants_accommodation="N", livingspace_assigned='None', office_assigned='None'):
        self.person_name = person_name
        self.person_type = person_type.lower()
        self.wants_accommodation = wants_accommodation
        self.livingspace_assigned = livingspace_assigned
        self.office_assigned = office_assigned


class Fellow(Person):
    def __init__(self, person_name, person_type, wants_accommodation):
        super().__init__(person_name, person_type, wants_accommodation)


class Staff(Person):
    def __init__(self, person_name, person_type, wants_accommodation):
        super().__init__(person_name, person_type, wants_accommodation)
