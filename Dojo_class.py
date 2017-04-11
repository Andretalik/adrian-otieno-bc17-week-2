import random
from Room_Class import *
from Person_Class import *


class Dojo(object):
    def __init__(self):
        self.all_rooms = []
        self.livingspaces = []
        self.offices = []
        self.all_people = []
        self.fellows = []
        self.staff = []

    def create_room(self, room_type, *args):
        if len(args) != 0:
            # print("hello")
            if room_type == "office":
                # print("world")
                for room_name in list(args):
                    office_object = Office("office", room_name)
                    self.all_rooms.append(office_object)
                    self.offices.append(office_object)
            elif room_type == "livingspace":
                # print("stuff")
                for room_name in list(args):
                    # print("loops")
                    livingspace_object = LivingSpace("livingspace", room_name)
                    self.all_rooms.append(livingspace_object)
                    self.offices.append(livingspace_object)
            else:
                return "Please enter the office type in the correct format"

    def add_person(self, person_name, person_type, wants_accomodation):
        if person_name != "":
            if person_type == "fellow":
                person_object = Fellow(person_name, "fellow", wants_accommodation)
                self.all_people.append(person_object)
                self.fellows.append(person_object)
            elif person_type == "staff":
                person_object = Staff(person_name, "staff", wants_accommodation)
                self.all_people.append(person_object)
                self.staff.append(person_object)
            else:
                return "Please enter the person type in the correct format"

    def assign_room(self, person_name, person_type, wants_accommodation="N"):



# doug = Dojo()
# print(doug.create_room("livingspace", "drangleic"))