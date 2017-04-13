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
        self.unallocated_for_offices = []
        self.unallocated_for_livingspaces = []

    def create_room(self, room_type, *args):
        if len(args) != 0:
            for room_name in list(args):
                if room_type == "office":
                    office_instance = Office("office", room_name)
                    self.all_rooms.append(office_instance)
                    self.offices.append(office_instance)
                    return office_instance.room_type, office_instance.room_name
                elif room_type == "livingspace":
                    livingspace_instance = LivingSpace("livingspace", room_name)
                    self.all_rooms.append(livingspace_instance)
                    self.livingspaces.append(livingspace_instance)
                    return livingspace_instance.room_type, livingspace_instance.room_name

            for office in self.offices:                         # this block of code ensure that the room chosen at
                if office not in self.available_offices:        # random for each added person has a space.
                    self.available_offices.append(office)
                else:
                    if len(office.occupants) < office.max_no:
                        pass
                    else:
                        self.available_offices.pop(office)
            for livingspace in self.livingspaces:
                if livingspace not in self.available_livingspaces:
                    self.available_livingspaces.append(livingspace)
                else:
                    if len(livingspace.occupants) < livingspace.max_no:
                        pass
                    else:
                        self.available_livingspaces.pop(livingspace)
            else:

                return "Please enter the room type in the correct format"

    def add_person(self, person_name, person_type, wants_accomodation="N"):
        if person_name != "":
            if person_type == "fellow":
                fellow_instance = Fellow(person_name, person_type, wants_accomodation)
                self.all_people.append(fellow_instance)
                self.fellows.append(fellow_instance)
                if (len(self.available_offices)) == 0:
                    self.unallocated_for_offices.append(fellow_instance)
                else:
                    chosen_office_object = random.choice(self.available_offices)
                    fellow_instance.office_assigned = chosen_office_object
                    chosen_office_object.occupants.append(fellow_instance)

                if wants_accomodation == "Y":
                    if (len(self.available_livingspaces)) == 0:
                        self.unallocated_for_livingspaces.append(fellow_instance)
                    else:
                        chosen_livingspace_object = random.choice(self.available_livingspaces)
                        fellow_instance.livingspace_assigned = chosen_livingspace_object
                        chosen_livingspace_object.occupants.append(fellow_instance)
                        return fellow_instance.person_type, fellow_instance.person_name, fellow_instance.office_assigned, fellow_instance.livingspace_assigned
                    
            elif person_type == "staff":
                staff_instance = Staff(person_name, person_type, wants_accomodation)
                self.all_people.append(staff_instance)
                self.staff.append(staff_instance)
                if (len(self.available_offices)) == 0:
                    self.unallocated_for_offices.append(staff_instance)
                else:
                    chosen_office_object = random.choice(self.available_offices)
                    staff_instance.office_assigned = chosen_office_object
                    chosen_office_object.occupants.append(staff_instance)
                    return staff_instance.person_type, staff_instance.person_name, staff_instance.office_assigned, staff_instance.livingspace_assigned

            for office in self.offices:                         # this block of code ensure that the room chosen at
                if office not in self.available_offices:        # random for each added person has a space.
                    if len(office.occupants) < office.max_no:
                        self.available_offices.append(office)
                else:
                    if len(office.occupants) < office.max_no:
                        pass
                    else:
                        self.available_offices.pop(office)
            for livingspace in self.livingspaces:
                if livingspace not in self.available_livingspaces:
                    if len(livingspace.occupants) < livingspace.max_no:
                        self.available_livingspaces.append(livingspace)
                else:
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
                return self.all_rooms[i].occupants

    def print_allocations(self, option_to_txt_file=""):
        i = 0  # creation of termination factor for loop
        count = (len(self.all_rooms)) - 1
        if count > 0:
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
        else:
            return "No rooms exist, hence allocations cannot exist either."

    def print_unallocated(self, option_to_txt_file=""):
        if option_to_txt_file == "":
            print("The following people have not been allocated an office:")
            i = 0  # creation of termination factor for loop
            count = (len(self.unallocated_for_offices)) - 1
            if count > 0:
                while i < count:
                    print(self.unallocated_for_offices[i].person_name)
                    i += 1
            else:
                print("N/A")
            print("The following people have not been allocated a living space:")
            j = 0  # creation of termination factor for loop
            counter = (len(self.all_rooms)) - 1
            if count > 0:
                while j < counter:
                    print(self.unallocated_for_livingspaces[i].person_name)
            else:
                print("N/A")
