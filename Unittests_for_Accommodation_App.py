import unittest
from Dojo_class import *


class TestCreateRoom(unittest.TestCase):
    def test_create_one_room_successful(self):
        test_instance_one_room = Dojo()
        initial_rooms_count = len(test_instance_one_room.all_rooms)
        test_instance_one_room.create_room("livingspace", "Drangleic")
        final_rooms_count = len(test_instance_one_room.all_rooms)
        self.assertEqual(final_rooms_count - initial_rooms_count, 1, 'The room has not been created')

    def test_create_multiple_rooms(self):
        test_instance_multiple_rooms = Dojo()
        initial_rooms_count = len(test_instance_multiple_rooms.all_rooms)
        test_instance_multiple_rooms.create_room("livingspace", "Drangleic", "Rockport", "Camden", "Halo")
        self.assertEqual(test_instance_multiple_rooms.all_rooms[0].room_name, "Drangleic", "The rooms have not been created")
        self.assertEqual(test_instance_multiple_rooms.all_rooms[2].room_name, "Camden", "The rooms have not been created")
        final_rooms_count = len(test_instance_multiple_rooms.all_rooms)
        self.assertEqual(final_rooms_count - initial_rooms_count, 4, "Multiple rooms were not created")


class TestAddPerson(unittest.TestCase):
    def setUp(self):
        self.test_case_instance = Dojo()

    def test_add_person_fellow_successful(self):
        test_instance_person_add = Dojo()
        initial_person_count = len(test_instance_person_add.all_people)
        test_instance_person_add.add_person("Adrian Otieno", "fellow", "Y")
        final_person_count = len(test_instance_person_add.all_people)
        self.assertEqual(final_person_count - initial_person_count, 1, 'The person has not been added')

    def test_add_person_staff_successful(self):
        test_instance_person_add_staff = Dojo()
        initial_person_count = len(test_instance_person_add_staff.all_people)
        test_instance_person_add_staff.add_person("Master Chief", "staff", "Y")
        final_person_count = len(test_instance_person_add_staff.all_people)
        self.assertEqual(final_person_count - initial_person_count, 1, 'The person has not been added')

    def test_person_room_allocation(self):
        self.test_case_instance.create_room("livingspace", "Drangleic", "Rockport", "Camden", "Halo")
        self.test_case_instance.create_room("office", "Paladins")
        self.test_case_instance.add_person("General Shephard", "fellow", "Y")
        self.assertIn(self.test_case_instance.fellows[0].office_assigned, self.test_case_instance.offices, "Person hasn't been assigned an office")
        self.assertIn(self.test_case_instance.fellows[0].livingspace_assigned, self.test_case_instance.livingspaces, "Person hasn't been assigned a living-space")


class TestMembersOfRooms(unittest.TestCase):
    def setUp(self):
        self.test_case_instance_members = Dojo()

    def test_member_in_specific_rooms(self):
        self.test_case_instance_members = Dojo()
        self.test_case_instance_members.create_room("office", "Overwatch")
        self.test_case_instance_members.add_person("Androxus Godslayer", "staff")
        self.test_case_instance_members.add_person("Samus Aran", "fellow")
        self.test_case_instance_members.add_person("Christianne Ochieng", "fellow")
        self.test_case_instance_members.print_room("Paladins")
        self.assertIn(self.test_case_instance_members.all_rooms[0].occupants[0], self.test_case_instance_members.all_people, "Function isn't appending rooms correctly")
        self.assertIn(self.test_case_instance_members.all_rooms[0].occupants[1], self.test_case_instance_members.all_people, "Function isn't appending rooms correctly")


    # def test_