import random
import pickle
import sqlite3
import os
from termcolor import colored
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
                if room_name.isalpha():
                    if room_type == "office":
                        office_instance = Office("office", room_name)
                        self.all_rooms.append(office_instance)
                        self.available_offices.append(office_instance)
                        print(colored("\nAn {} called {} has been created".format(office_instance.room_type, office_instance.room_name), "green"))
                    elif room_type == "livingspace":
                        livingspace_instance = LivingSpace("livingspace", room_name)
                        self.all_rooms.append(livingspace_instance)
                        self.available_livingspaces.append(livingspace_instance)
                        print(colored("\nA {} called {} has been created".format(livingspace_instance.room_type, livingspace_instance.room_name), "green"))
                    else:
                        print(colored("\nIncorrect format of room type used. Check help.", "red"))
                        return "Incorrect format of room type used. Check help."
                else:
                    print(colored("\nRoom name cannot have special characters or numbers", "red"))
                    return "Incorrect room name"

    def add_person(self, person_first_name, person_second_name, person_type, wants_accomodation="N"):
        """This adds a person into the system to allow him/her to be allocated
            a room as required"""
        if person_first_name != "" and person_second_name != "":
            if person_first_name.isalpha() and person_second_name.isalpha():
                if person_type == "fellow":
                    person_instance = Fellow(person_first_name, person_second_name, person_type, wants_accomodation)
                    person_instance.identifier = int((len(self.all_people))+1)
                    self.all_people.append(person_instance)
                    print(colored("\nA {} called {} has been created\t\t\tID:{}".format(person_instance.person_type, person_instance.person_first_name, person_instance.identifier), "green"))
                    self.allocate_livingspace(person_instance)
                elif person_type == "staff":
                    person_instance = Staff(person_first_name, person_second_name, person_type)
                    person_instance.identifier = int((len(self.all_people))+1)
                    self.all_people.append(person_instance)
                    print(colored("\nA {} member called {} has been created\t\t\tID:{}".format(person_instance.person_type, person_instance.person_first_name, person_instance.identifier), "green"))
                else:
                    print(colored("\nPlease enter the person type in the correct format.", "red"))
                    return "Please enter the person type in the correct format."
                self.allocate_office(person_instance)
                self.room_checker()
            else:
                print(colored("\nPerson's name only accepts letters and not special characters or numbers", "red"))
                return "Incorrect format of person name"
        else:
            print(colored("\nPlease enter the person's details in the correct format.", "red"))
            return "Please enter the person's details in the correct format."

    def allocate_office(self, object_allocate):
        """This function allocates the person created an office to work in"""
        if object_allocate.person_type == "fellow":
            if (len(self.available_offices)) == 0:
                self.unallocated_offices.append(object_allocate)
                print(colored("\n{} has been added to the waiting list due to no available rooms".format(object_allocate.person_first_name), "green"))
            else:
                chosen_office_object = random.choice(self.available_offices)
                object_allocate.office_assigned = chosen_office_object
                chosen_office_object.occupants.append(object_allocate)
                print(colored("{} has been allocated office {}".format(object_allocate.person_first_name, object_allocate.office_assigned.room_name), "green"))
        elif object_allocate.person_type == "staff":
            if (len(self.available_offices)) == 0:
                self.unallocated_offices.append(object_allocate)
                print(colored("\n{} has been added to the waiting list due to no available rooms".format(object_allocate.person_first_name), "green"))
            else:
                chosen_office_object = random.choice(self.available_offices)
                object_allocate.office_assigned = chosen_office_object
                chosen_office_object.occupants.append(object_allocate)
                print(colored("\n{} has been allocated office {}".format(object_allocate.person_first_name, object_allocate.office_assigned.room_name), "green"))

    def allocate_livingspace(self, object_allocate):
        """This function allocates the fellow created a livingspace"""
        if isinstance(object_allocate, Fellow):
            if object_allocate.wants_accommodation == "Y":
                if (len(self.available_livingspaces)) == 0:
                    self.unallocated_livingspaces.append(object_allocate)
                else:
                    chosen_livingspace_object = random.choice(self.available_livingspaces)
                    object_allocate.livingspace_assigned = chosen_livingspace_object
                    chosen_livingspace_object.occupants.append(object_allocate)
                    print(colored("\n{} has been allocated living space {}".format(object_allocate.person_first_name, object_allocate.livingspace_assigned.room_name), "green"))

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
        if room_name.isalpha():
            if len(self.all_rooms) == 0:
                print(colored("\nThere are no existing rooms in the system", "red"))
                return "No existing rooms"
            else:
                for rooms in self.all_rooms:
                    if rooms.room_name == room_name:
                        if len(rooms.occupants) > 0:
                            for occupants in rooms.occupants:
                                print(occupants.person_first_name, " ", occupants.person_second_name, "   ")
                            return "Occupants printed."
                        else:
                            print("\n", "\t", room_name, "\n")
                            print(colored("No occupants at the moment.", "yellow"))
                    else:
                        print("\n", "\t", room_name, "\n")
                        print(colored("\nThis room does not exist, hence no occupants.", "red"))
        else:
            print(colored("\nNo room name has special characters.", "red"))
            return "Invalid. Special characters used."

    def print_allocations(self, option_to_txt_file=None):
        """This prints out to the console or to a text file all the active
            allocations within the system"""
        allocation_output = ""
        if len(self.all_rooms) == 0:
            print(colored("\nUnfortunately, there are no existing rooms to be printed", "red"))
        else:
            for room in self.all_rooms:
                if len(room.occupants) > 0:
                    allocation_output += ("\n\n" + room.room_name + "---" + room.room_type)
                    allocation_output += ("\n" + "#" * 50 + "\n")
                    for occupants in room.occupants:
                        allocation_output += (occupants.person_first_name + " " + occupants.person_second_name + ", ")
            if option_to_txt_file is None:
                print(allocation_output)
                return allocation_output
            else:
                output_txt_file = open(option_to_txt_file + ".txt", "w+")
                output_txt_file.write(allocation_output)
                output_txt_file.close()
                print(colored("\nThe allocation data has been written to {}".format(option_to_txt_file), "green"))
                return "The allocation data has been written to {}".format(option_to_txt_file)

    def print_unallocated(self, option_to_txt_file=None):
        """This prints out to the console or to a text file all the
            unallocated people within the system"""
        unallocated_output = ""
        if len(self.all_people) == 0:
            print(colored("\nNo unallocated people, because there are no people in the system.", "red"))
            return "No unallocated people, because there are no people in the system."
        else:
            if len(self.unallocated_offices) == 0 and len(self.unallocated_livingspaces) == 0:
                print(colored("\nEveryone has been allocated an office and livingspace. Yay!", "green"))
                return "Everyone has been allocated an office and livingspace. Yay!"
            else:
                unallocated_output_offices = ""
                unallocated_output_livingspaces = ""
                unallocated_output_offices += ("\nUnallocated Offices\n")
                unallocated_output_offices += ("#" * 50 + "\n")
                for person in self.unallocated_offices:
                    unallocated_output_offices += (person.person_first_name + " " + person.person_second_name + ",   ")
                unallocated_output_livingspaces += ("\nUnallocated LivingSpaces\n")
                unallocated_output_livingspaces += ("#" * 50 + "\n")
                for person in self.unallocated_livingspaces:
                    unallocated_output_livingspaces += (person.person_first_name + " " + person.person_second_name + ",   ")
                if option_to_txt_file is None:
                    print(unallocated_output_offices)
                    print(unallocated_output_livingspaces)
                    return unallocated_output_offices
                    return unallocated_output_livingspaces
                else:
                    txt_file_unallocated = open(option_to_txt_file + ".txt", "w+")
                    txt_file_unallocated.write(unallocated_output_offices)
                    txt_file_unallocated.write(unallocated_output_livingspaces)
                    txt_file_unallocated.close()
                    print(colored("\nThe data concerning unallocated people has been written to {}".format(option_to_txt_file), "green"))
                    return "The data concerning unallocated people has been written to {}".format(option_to_txt_file)

    def deallocation(self, ID, room):
        """This function is a module for the reallocation function: It removes
        the person to be reallocated from the room he was currently allocated
        to (for offices)"""
        for person in room.occupants:
            if ID == person.identifier:
                room.occupants.remove(person)

    def reallocate_person(self, ID, room_name):
        """This function reallocates a person to another room using his/her ID
        to identify him/her"""
        requested_ID = int(ID)
        for person in self.all_people:
            if requested_ID == person.identifier:
                for room in self.all_rooms:
                    if room_name == room.room_name:
                        if room.room_type == "office":
                            for room in self.available_offices:
                                if room_name == room.room_name:
                                    if person.office_assigned.room_type == room.room_type:
                                        if person in room.occupants:
                                            print(colored("\nCannot reallocate to the same room.", "red"))
                                            return "Cannot reallocate to the same room."
                                        else:
                                            self.deallocation(ID, room)
                                            room.occupants.append(person)
                                            person.office_assigned = room
                                            self.room_checker()
                                            print(colored("\n{} has been reallocated to {}"
                                                  .format(person.person_first_name, person.office_assigned.room_name), "green"))
                                            return ("{} has been reallocated to {}"
                                                    .format(person.person_first_name, person.office_assigned.room_name))
                                    else:
                                        print(colored("\nReallocation is only from office to office as well as livingspace to livingspace.", "red"))
                                        return "Reallocation is only from office to office as well as livingspace to livingspace."
                        elif room.room_type == "livingspace":
                            for room in self.available_livingspaces:
                                if room_name == room.room_name:
                                    if person.office_assigned.room_type == room.room_type:
                                        if person in room.occupants:
                                            print(colored("\nCannot reallocate to the same room.", "red"))
                                            return "Cannot reallocate to the same room."
                                        else:
                                            self.deallocation(ID, room)
                                            room.occupants.append(person)
                                            person.livingspace_assigned = room
                                            self.room_checker()
                                            print(colored("\n{} has been reallocated to {}"
                                                  .format(person.person_first_name, person.livingspace_assigned.room_name), "green"))
                                            return ("{} has been reallocated to {}"
                                                    .format(person.person_first_name, person.livingspace_assigned.room_name))
                                    else:
                                        print(colored("\nReallocation is only from office to office as well as livingspace to livingspace.", "red"))
                                        return "Reallocation is only from office to office as well as livingspace to livingspace."

        print(colored("\nThe person you want to reallocate does not exist in the system", "red"))
        return "The person you want to reallocate does not exist in the system"

    def mass_add_people(self, file_name=""):
        """This function adds people to the system from a textfile"""
        try:
            with open(file_name, "r") as batch_file:
                for line in batch_file:
                    person_details = line.rstrip().split()
                    if len(person_details) == 4:
                        self.add_person(person_details[0].title(), person_details[1].title(),
                                        person_details[2].lower(), person_details[3])
                    elif len(person_details) == 3:
                        self.add_person(person_details[0].title(), person_details[1].title(),
                                        person_details[2].lower())

                    else:
                        print(colored("\nThere is an issue with the target file.", "red"))
                        return "There is an issue with the target file."
        except:
            print(colored("\nThe file specified couldn't be found. Please specify the\
                    correct file path.", "red"))
            return "Incorrect path."

    def save_to_db(self, database_name):
        """This function saves the objects created in their respective lists\
        in a database for future reference"""
        if database_name is None:
            database_name = "dojo"
        if database_name.isalpha():
            database_name = database_name + ".db"
            connected = sqlite3.connect(database_name)
            connected.execute('''CREATE TABLE IF NOT EXISTS Dojo (
            Id INTEGER PRIMARY KEY, all_rooms TEXT, all_people TEXT, unallocated_offices TEXT,
            unallocated_livingspaces TEXT);''')
            connected.close()

            # conversion of list variables to strings for storage
            all_rooms_save = pickle.dumps(self.all_rooms)
            all_people_save = pickle.dumps(self.all_people)
            unallocated_offices_save = pickle.dumps(self.unallocated_offices)
            unallocated_livingspaces_save = pickle.dumps(self.unallocated_livingspaces)
            connected = sqlite3.connect(database_name)
            connected.execute("INSERT OR REPLACE INTO Dojo(Id, all_rooms, all_people, "
                              "unallocated_offices, unallocated_livingspaces) "
                              "VALUES (?, ?, ?, ?, ?);",
                              (1, all_rooms_save, all_people_save, unallocated_offices_save, unallocated_livingspaces_save))
            connected.commit()
            connected.close()
            return_msg = "\nData stored in the {} database".format(database_name)
            print(colored(return_msg, "green"))
            return return_msg
        else:
            print(colored("\nDatabase name can't have special characters.", "red"))
            return "Database name can't have special characters."

    def load_from_db(self, database_name="dojo.db"):
        """This function loads the the objects from the database and refreshes\
        and refreshes them back into their respective lists for use within the\
        system."""
        connected = sqlite3.connect(database_name)
        cursor = connected.cursor()

        try:
            cursor.execute("SELECT all_rooms FROM Dojo WHERE Id=1")
            all_rooms_dmp = cursor.fetchone()

            cursor.execute("SELECT all_people FROM Dojo WHERE Id=1")
            all_people_dmp = cursor.fetchone()

            cursor.execute("SELECT unallocated_offices FROM Dojo WHERE Id=1")
            unallocated_offices_dmp = cursor.fetchone()

            cursor.execute("SELECT unallocated_livingspaces FROM Dojo WHERE Id=1")
            unallocated_livingspaces_dmp = cursor.fetchone()

            connected.close()

            rooms_list = pickle.loads(all_rooms_dmp[0])
            people_list = pickle.loads(all_people_dmp[0])
            unallocated_offices_list = pickle.loads(unallocated_offices_dmp[0])
            unallocated_livingspaces_list = pickle.loads(unallocated_livingspaces_dmp[0])

            self.all_rooms = rooms_list
            self.all_people = people_list
            self.unallocated_offices = unallocated_offices_list
            self.unallocated_livingspaces = unallocated_livingspaces_list
            status_msg = "\nData successfully loaded from {}".format(database_name)
            print(colored(status_msg, "green"))
            return status_msg
        except:
            print(colored("\nSerious problem encountered while loading from the database\
                  Kindly crosscheck the name of the database", "red"))
            os.remove(database_name)
            return "Error while loading from file."
