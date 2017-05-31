import random
from room_class import Office, LivingSpace
from person_class import Fellow, Staff


class Dojo(object):
    def __init__(self):
        self.all_rooms = []
        self.all_people = []
        self.available_offices = []
        self.available_livingspaces = []
        self.unallocated_offices = []
        self.unallocated_livingspaces = []

    def create_room(self, room_type, rooms_to_make):
        """This creates an office or livingspace for use in the system"""
        if len(rooms_to_make) != 0:
            for room_name in rooms_to_make:
                if room_type == "office":
                    office_instance = Office("office", room_name)
                    self.all_rooms.append(office_instance)
                    self.available_offices.append(office_instance)
                    print("An {} called {} has been created".format(office_instance.room_type, office_instance.room_name))
                elif room_type == "livingspace":
                    livingspace_instance = LivingSpace("livingspace", room_name)
                    self.all_rooms.append(livingspace_instance)
                    self.available_livingspaces.append(livingspace_instance)
                    print("A {} called {} has been created".format(livingspace_instance.room_type, livingspace_instance.room_name))
                else:
                    return "Incorrect format of room type used. Check help."

    def add_person(self, person_first_name, person_second_name, person_type, wants_accomodation="N"):
        """This adds a person into the system to allow him/her to be allocated
            a room as required"""
        if person_first_name != "" and person_second_name != "":
            if person_type == "fellow":
                fellow_instance = Fellow(person_first_name, person_second_name, person_type, wants_accomodation)
                self.all_people.append(fellow_instance)
                print("A {} called {} has been created".format(fellow_instance.person_type, fellow_instance.person_first_name))
                self.allocate_livingspace()
            elif person_type == "staff":
                staff_instance = Staff(person_first_name, person_second_name, person_type)
                self.all_people.append(staff_instance)
                print("A {} member called {} has been created".format(staff_instance.person_type, staff_instance.person_first_name))
            else:
                return "Please enter the person type in the correct format."
            self.allocate_office()
            self.room_checker()
        else:
            return "Please enter the person's details in the correct format."

    def allocate_office(self):
        """This function allocates the person created an office to work in"""
        for person in self.all_people:
            if person.person_type == "fellow":
                if (len(self.available_offices)) == 0:
                    self.unallocated_offices.append(person)
                    print("{} has been added to the waiting list due to no available rooms".format(person.person_first_name))
                else:
                    chosen_office_object = random.choice(self.available_offices)
                    person.office_assigned = chosen_office_object
                    chosen_office_object.occupants.append(person)
                    print("{} has been allocated office {}".format(person.person_first_name, person.office_assigned.room_name))
            elif person.person_type == "staff":
                if (len(self.available_offices)) == 0:
                    self.unallocated_offices.append(person)
                    print("{} has been added to the waiting list due to no available rooms".format(person.person_first_name))
                else:
                    chosen_office_object = random.choice(self.available_offices)
                    person.office_assigned = chosen_office_object
                    chosen_office_object.occupants.append(person)
                    print("{} has been allocated office {}".format(person.person_first_name, person.office_assigned.room_name))

    def allocate_livingspace(self):
        """This function allocates the fellow created a livingspace"""
        for person in self.all_people:
            if isinstance(person, Fellow):
                if person.wants_accommodation == "Y":
                    if (len(self.available_livingspaces)) == 0:
                        self.unallocated_livingspaces.append(person)
                    else:
                        chosen_livingspace_object = random.choice(self.available_livingspaces)
                        person.livingspace_assigned = chosen_livingspace_object
                        chosen_livingspace_object.occupants.append(person)
                        print("{} has been allocated living space {}".format(person.person_first_name, person.livingspace_assigned.room_name))

    def room_checker(self):
        """This function updates the list of available rooms on the basis of
        the number of people in the said rooms"""
        for office in self.available_offices:
            if len(office.occupants) < office.max_no:
                pass
            else:
                self.available_offices.remove(office)
        for livingspace in self.available_livingspaces:
            if len(livingspace.occupants) < livingspace.max_no:
                pass
            else:
                self.available_livingspaces.remove(livingspace)

    def print_room(self, room_name):
        """This prints all the people who have been alllocated a specific room by
           management"""
        for rooms in self.all_rooms:
            if rooms.room_name == room_name:
                for occupants in rooms.occupants:
                    print(occupants.person_first_name)
            else:
                print(self.all_rooms[0].room_name + '\n That room doesn\'t exist')

    def print_allocations(self, option_to_txt_file=""):
        """This prints out to the console or to a text file all the active
            allocations within the system"""
        allocation_output = ""
        if len(self.all_rooms) == 0:
            print("Unfortunately, there are no existing rooms to be printed")
        else:
            for room in self.all_rooms:
                if len(room.occupants) > 0:
                    allocation_output += ("\n\n" + room.room_name + "---" + room.room_type)
                    allocation_output += ("\n" + "#" * 50 + "\n")
                    for occupants in room.occupants:
                        allocation_output += (occupants.person_first_name + " " + occupants.person_second_name + ", ")
            if option_to_txt_file == "":
                return allocation_output
            else:
                output_txt_file = open(option_to_txt_file + ".txt", "w+")
                output_txt_file.write(allocation_output)
                output_txt_file.close()
                return "The allocation data has been written to " + option_to_txt_file

    def print_unallocated(self, option_to_txt_file=""):
        """This prints out to the console or to a text file all the
            unallocated people within the system"""
        unallocated_output = ""
        if len(self.all_people) == 0:
            return "No unallocated people, because there are no people in the system."
        else:
            if len(self.unallocated_offices) == 0 and len(self.unallocated_livingspaces) == 0:
                return "Everyone has been allocated an office and livingspace. Yay!"
            else:
                unallocated_output += ("\n\n Unallocated Offices")
                for person in self.unallocated_offices:
                    unallocated_output += (person.person_first_name + " " + person.person_second_name)
                if option_to_txt_file == "":
                    print(unallocated_output)
                else:
                    txt_file_unallocated = open(option_to_txt_file + ".txt", "w+")
                    txt_file_unallocated.write(unallocated_output)
                    txt_file_unallocated.close()
                    return "The data concerning unallocated people has been written to {}".format(option_to_txt_file)
    def reallocate_person(self, ID, room_name):
