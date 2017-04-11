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
            # print("hello") # debugging checks for correct logic
            if room_type == "office":
                # print("world") # debugging checks for correct logic
                for room_name in list(args):
                    office_object = Office("office", room_name)
                    self.all_rooms.append(office_object)
                    self.offices.append(office_object)
                    # print("office created")
            elif room_type == "livingspace":
                # print("stuff")# debugging checks for correct logic
                for room_name in list(args):
                    # print("loops") # debugging checks for correct logic
                    livingspace_object = LivingSpace("livingspace", room_name)
                    self.all_rooms.append(livingspace_object)
                    self.livingspaces.append(livingspace_object)
                    # print(len(self.livingspaces))
                    # print("livingspaces") # debugging checks for correct logic
            else:
                return "Please enter the room type in the correct format"

    def add_person(self, person_name, person_type, wants_accomodation="N"):
        if person_name != "":
            if person_type == "fellow": #
                # print("a fellow") # debugging checks for correct logic
                person_object = Fellow(person_name, person_type, wants_accomodation) # creates
                self.all_people.append(person_object)
                self.fellows.append(person_object)
                # person_object.office_assigned = random.choice(self.offices)
                if wants_accomodation == "Y":
                    # print("room assigned") # debugging checks for correct logic
                    #if len(self.livingspaces) != 0:
                    # print(len(self.livingspaces))
                    # person_object.room_assigned = random.choice(self.livingspaces)
                    #else:
                        #person_object.room_assigned = "No rooms exist"
                    if (len(self.livingspaces)) == 0:
                        person_object.room_assigned = "You can't be placed. No rooms exist"
                    else:
                        person_object.room_assigned = random.choice(self.livingspaces)

            elif person_type == "staff":
                # print("staff dont live here") # debugging checks for correct logic
                person_object = Staff(person_name, person_type, wants_accomodation)
                self.all_people.append(person_object)
                self.staff.append(person_object)

            else:
                return "Please enter the person type in the correct format"





'''doug = Dojo()
doug.create_room("livingspace", "Drangleic")
print(doug.all_rooms[0].room_name)'''
