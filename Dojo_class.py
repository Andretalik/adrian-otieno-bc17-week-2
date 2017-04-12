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
        self.available_rooms = []

    def create_room(self, room_type, *args):
        if len(args) != 0:
            if room_type == "office":
                for room_name in list(args):
                    office_object = Office("office", room_name)
                    self.all_rooms.append(office_object)
                    self.offices.append(office_object)
            elif room_type == "livingspace":
                for room_name in list(args):
                    livingspace_object = LivingSpace("livingspace", room_name)
                    self.all_rooms.append(livingspace_object)
                    self.livingspaces.append(livingspace_object)
            else:
                return "Please enter the room type in the correct format"


    # def available_rooms(self, ):

    def add_person(self, person_name, person_type, wants_accomodation="N"):
        if person_name != "":
            if person_type == "fellow":
                person_object = Fellow(person_name, person_type, wants_accomodation)  # creates
                self.all_people.append(person_object)
                self.fellows.append(person_object)
                if (len(self.offices)) == 0:
                    pass
                else:
                    chosen_office_object = random.choice(self.offices)
                    if len(chosen_office_object.occupants) < 6:
                        person_object.office_assigned = chosen_office_object
                        chosen_office_object.occupants.append(person_object)
                    else:
                        return "Office is Full."
                if wants_accomodation == "Y":
                    if (len(self.livingspaces)) == 0:
                        pass
                    else:
                        chosen_livingspace_object = random.choice(self.livingspaces)
                        if len(chosen_livingspace_object.occupants) < 4:
                            person_object.livingspace_assigned = chosen_livingspace_object
                            chosen_livingspace_object.occupants.append(person_object)

            elif person_type == "staff":
                person_object = Staff(person_name, person_type, wants_accomodation)
                self.all_people.append(person_object)
                self.staff.append(person_object)
                if (len(self.offices)) == 0:
                    pass
                else:
                    chosen_office_object = random.choice(self.offices)
                    if len(chosen_office_object.occupants) < 6:
                        person_object.office_assigned = chosen_office_object
                        chosen_office_object.occupants.append(person_object)

            else:
                return "Please enter the person type in the correct format"

    def print_room(self, room_name):
        i = 0   # creation of termination factor for loop
        count = (len(self.all_rooms)) - 1
        while i < count:
            if self.all_rooms[i].room_name == room_name:
                return self.all_rooms[i].occupants

    def print_allocations(self, option_to_txt_file=""):
        i = 0  # creation of termination factor for loop
        count = (len(self.all_rooms)) - 1
        if option_to_txt_file == "":
            while i < count:
                if len(self.all_rooms[i].occupants) > 0:
                    print(self.all_rooms[i].room_name)
                    i += 1
                    x = 0  # creation of termination factor for loop
                    count2 = (len(self.all_rooms)) - 1
                    while x < count2:
                        print(self.all_rooms[i].occupants.person_name)
                        x += 1
        else:
            txt_filename = option_to_txt_file
            output_txt = open(txt_filename, mode='w+')
            while i < count:
                if len(self.all_rooms[i].occupants) > 0:
                    output_txt.write(self.all_rooms[i].room_name)
                    i += 1
                    x = 0  # creation of termination factor for loop
                    count2 = (len(self.all_rooms)) - 1
                    while x < count2:
                        output_txt.write(self.all_rooms[i].occupants.person_name)
                        x += 1
