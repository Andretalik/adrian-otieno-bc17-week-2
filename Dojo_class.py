import random
from room_class import Office, LivingSpace
from person_class import Fellow, Staff


class Dojo(object):
    def __init__(self):
        self.all_rooms = []
        # self.livingspaces = []
        # self.offices = []
        self.all_people = []
        # self.fellows = []
        # self.staff = []
        self.available_offices = []
        self.available_livingspaces = []
        self.unallocated_offices = []
        self.unallocated_livingspaces = []

    def create_room(self, room_type, rooms_to_make):
        if len(rooms_to_make) != 0:
            for room_name in rooms_to_make:
                if room_type == "office":
                    office_instance = Office("office", room_name)
                    self.all_rooms.append(office_instance)
                    # self.offices.append(office_instance)
                    self.available_offices.append(office_instance)
                    print("An {} called {} has been created".format(office_instance.room_type, office_instance.room_name))
                elif room_type == "livingspace":
                    livingspace_instance = LivingSpace("livingspace", room_name)
                    self.all_rooms.append(livingspace_instance)
                    # self.livingspaces.append(livingspace_instance)
                    self.available_livingspaces.append(livingspace_instance)
                    print("A {} called {} has been created".format(livingspace_instance.room_type, livingspace_instance.room_name))
                else:
                    print("Incorrect format of room type used. Check help.")


    def add_person(self, person_first_name, person_second_name, person_type, wants_accomodation="N"):
        if person_first_name != "" and person_second_name != "":
            if person_type == "fellow":
                fellow_instance = Fellow(person_first_name, person_second_name, person_type, wants_accomodation)
                self.all_people.append(fellow_instance)
                # self.fellows.append(fellow_instance)
                print("A {} called {} has been created".format(fellow_instance.person_type, fellow_instance.person_first_name))

                if (len(self.available_offices)) == 0:
                    self.unallocated_offices.append(fellow_instance)
                    print("{} has been added to the waiting listdue to no available rooms".format(fellow_instance.person_first_name))
                else:
                    chosen_office_object = random.choice(self.available_offices)
                    fellow_instance.office_assigned = chosen_office_object
                    chosen_office_object.occupants.append(fellow_instance)
                    print("{} has been allocated office {}".format(fellow_instance.person_name, fellow_instance.office_assigned))

                if wants_accomodation == "Y":
                    if (len(self.available_livingspaces)) == 0:
                        self.unallocated_livingspaces.append(fellow_instance)
                    else:
                        chosen_livingspace_object = random.choice(self.available_livingspaces)
                        fellow_instance.livingspace_assigned = chosen_livingspace_object
                        chosen_livingspace_object.occupants.append(fellow_instance)
                        print("{} has been allocated living space {}".format(fellow_instance.person_first_name, fellow_instance.livingspace_assigned))

            elif person_type == "staff":
                staff_instance = Staff(person_first_name, person_second_name, person_type, wants_accomodation)
                self.all_people.append(staff_instance)
                # self.staff.append(staff_instance)
                print("A {} member called {} has been created".format(staff_instance.person_type, staff_instance.person_first_name))

                if (len(self.available_offices)) == 0:
                    self.unallocated_offices.append(staff_instance)
                    print("{} has been added to the waiting list due to no available rooms".format(staff_instance.person_first_name))
                else:
                    chosen_office_object = random.choice(self.available_offices)
                    staff_instance.office_assigned = chosen_office_object
                    chosen_office_object.occupants.append(staff_instance)
                    print("{} has been allocated office {}".format(staff_instance.person_first_name, staff_instance.office_assigned))
            else:
                print("Please enter the person type in the correct format.")

            for office in self.available_offices:
                if len(office.occupants) < office.max_no:
                    pass
                else:
                    self.available_offices.pop(office)
            for livingspace in self.available_livingspaces:
                if len(livingspace.occupants) < livingspace.max_no:
                    pass
                else:
                    self.available_livingspaces.pop(livingspace)

    def print_room(self, room_name):
        for rooms in self.all_rooms:
            if rooms.room_name == room_name:
                for occupants in rooms.occupants:
                    print(occupants.person_first_name)
            else:
                print(self.all_rooms[0].room_name)
                print('That room doesn\'t exist')

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
                        print(self.all_rooms[i].occupants.person_first_name)
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
                        output_txt.write(self.all_rooms[i].occupants.person_first_name)
                        x += 1
