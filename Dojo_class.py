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
        self.available_offices = []
        self.available_livingspaces = []
        self.unallocated_offices = []
        self.unallocated_livingspaces = []

    def create_room(self, room_type, *args):
        if len(args) != 0:
            for room_name in list(args):
                if room_type == "office":
                    office_instance = Office("office", room_name)
                    self.all_rooms.append(office_instance)
                    self.offices.append(office_instance)
                    self.available_offices.append(office_instance)
                elif room_type == "livingspace":
                    livingspace_instance = LivingSpace("livingspace", room_name)
                    self.all_rooms.append(livingspace_instance)
                    self.livingspaces.append(livingspace_instance)
                    self.available_livingspaces.append(livingspace_instance)


    def add_person(self, person_name, person_type, wants_accomodation="N"):
        if person_name != "":
            if person_type == "fellow":
                fellow_instance = Fellow(person_name, person_type, wants_accomodation)
                self.all_people.append(fellow_instance)
                self.fellows.append(fellow_instance)
                if (len(self.available_offices)) == 0:
                    self.unallocated_offices.append(fellow_instance)
                else:
                    chosen_office_object = random.choice(self.available_offices)
                    fellow_instance.office_assigned = chosen_office_object
                    chosen_office_object.occupants.append(fellow_instance)

                if wants_accomodation == "Y":
                    if (len(self.available_livingspaces)) == 0:
                        self.unallocated_livingspaces.append(fellow_instance)
                    else:
                        chosen_livingspace_object = random.choice(self.available_livingspaces)
                        fellow_instance.livingspace_assigned = chosen_livingspace_object
                        chosen_livingspace_object.occupants.append(fellow_instance)

            elif person_type == "staff":
                staff_instance = Staff(person_name, person_type, wants_accomodation)
                self.all_people.append(staff_instance)
                self.staff.append(staff_instance)
                if (len(self.available_offices)) == 0:
                    self.unallocated_offices.append(staff_instance)
                else:
                    chosen_office_object = random.choice(self.available_offices)
                    staff_instance.office_assigned = chosen_office_object
                    chosen_office_object.occupants.append(staff_instance)

            for office in self.available_offices:
                if len(office.occupants) < office.max_no:
                    pass
                else:
                    self.available_offices.pop(office)
            for livingspace in self.livingspaces:
                if len(livingspace.occupants) < livingspace.max_no:
                    pass
                else:
                    self.available_livingspaces.pop(livingspace)
            else:
                return "Please enter the person type in the correct format"

    def print_room(self, room_name):
        i = 0   # creation of termination factor for loop
        count = (len(self.all_rooms)) - 1
        while i < count:
            if self.all_rooms[i].room_name == room_name:
                print(self.all_rooms[i].occupants)

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
