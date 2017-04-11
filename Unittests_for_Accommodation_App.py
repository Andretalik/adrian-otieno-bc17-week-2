import unittest
from Dojo_class import *


class TestCreateRoom(unittest.TestCase):
    def test_create_one_room_successful(self):
        test_instance_one_room = Dojo()
        initial_rooms_count = len(test_instance_one_room.all_rooms)
        drangleic_livingspace = test_instance_one_room.create_room("livingspace", "Drangleic")
        # self.assertTrue(drangleic_livingspace)
        final_rooms_count = len(test_instance_one_room.all_rooms)
        self.assertEqual(final_rooms_count - initial_rooms_count, 1, 'The room has not been created')

    def test_create_multiple_rooms(self):
        test_instance_multiple_rooms = Dojo()
        initial_rooms_count = len(test_instance_multiple_rooms.all_rooms)
        multiple_livingspace = test_instance_multiple_rooms.create_room("livingspace", "Drangleic", "Rockport", "Camden", "Halo")
        # self.assertTrue(multiple_livingspace)
        self.assertEqual(test_instance_multiple_rooms.all_rooms[0].room_name, "Drangleic", "The rooms have not been created")
        self.assertEqual(test_instance_multiple_rooms.all_rooms[2].room_name, "Camden", "The rooms have not been created")
        final_rooms_count = len(test_instance_multiple_rooms.all_rooms)
        self.assertEqual(final_rooms_count - initial_rooms_count, 4, "Multiple rooms were not created")


class TestAddPerson(unittest.TestCase):
    def test_add_person_fellow_successful(self):
        test_instance_person_add = Dojo()
        initial_person_count = len(test_instance_person_add.all_people)
        adrian_otieno_fellow = test_instance_person_add.add_person("Adrian Otieno", "fellow", "Y")
        # self.assertTrue(adrian_otieno_fellow)
        final_person_count = len(test_instance_person_add.all_people)
        self.assertEqual(final_person_count - initial_person_count, 1, 'The person has not been added')

    def test_add_person_staff_successful(self):
        test_instance_person_add_staff = Dojo()
        initial_person_count = len(test_instance_person_add_staff.all_people)
        master_chief_fellow = test_instance_person_add_staff.add_person("Master Chief", "staff", "Y")
        # self.assertTrue(adrian_otieno_fellow)
        final_person_count = len(test_instance_person_add_staff.all_people)
        self.assertEqual(final_person_count - initial_person_count, 1, 'The person has not been added')

    '''def test_person_accommodation(self):
        room_instance = Room("livingspace", "Drangleic", "Rockport", "Camden", "Halo")
        multiple_livingspace = room_instance.create_room("livingspace", "Drangleic", "Rockport", "Camden", "Halo")
        self.assertTrue(multiple_livingspace)
        person_instance = Person("Master Chief", "Fellow", "Y")
        master_chief_fellow = person_instance.add_person("Master Chief", "Fellow", "Y")
        self.assertTrue(isinstance(master_chief_fellow.room_assigned, master_chief_fellow.livingspaces),
                        msg="Person has been assigned room that does not exist")'''





