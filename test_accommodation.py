import unittest
from Dojo_class import Dojo


class TestCreateRoom(unittest.TestCase):
    def test_create_one_room_successful(self):
        test_instance_one_room = Dojo()
        initial_rooms_count = len(test_instance_one_room.all_rooms)
        test_instance_one_room.create_room("livingspace", ["Drangleic"])
        final_rooms_count = len(test_instance_one_room.all_rooms)
        self.assertEqual(final_rooms_count - initial_rooms_count, 1, 'The room has not been created')

    def test_create_multiple_rooms(self):
        test_instance_multiple_rooms = Dojo()
        initial_rooms_count = len(test_instance_multiple_rooms.all_rooms)
        test_instance_multiple_rooms.create_room("livingspace", ["Drangleic", "Rockport", "Camden", "Halo"])
        self.assertEqual(test_instance_multiple_rooms.all_rooms[0].room_name, "Drangleic", "The rooms have not been created")
        self.assertEqual(test_instance_multiple_rooms.all_rooms[2].room_name, "Camden", "The rooms have not been created")
        final_rooms_count = len(test_instance_multiple_rooms.all_rooms)
        self.assertEqual(final_rooms_count - initial_rooms_count, 4, "Multiple rooms were not created")

    def test_wrong_syntax_create_room(self):
        test_instance_wrong_syntax_room = Dojo()
        testing = test_instance_wrong_syntax_room.create_room("sleepingarea", "Son Goku")
        self.assertEqual(testing, "Incorrect format of room type used. Check help.", msg="Program broken by syntax error in create_room method.")


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

    def test_wrong_syntax_add_person(self):
        test_instance_wrong_syntax_person = Dojo()
        testing = test_instance_wrong_syntax_person.add_person("Kurosaki Ichigo", "worker")
        self.assertEqual(testing, "Please enter the person type in the correct format.", msg="Program broken by syntax error in add_person method.")

    def test_person_room_allocation(self):
        self.test_case_instance.create_room("livingspace", ["Drangleic", "Rockport", "Camden", "Halo"])
        self.test_case_instance.create_room("office", "Paladins")
        self.test_case_instance.add_person("General Shephard", "fellow", "Y")
        # print(self.test_case_instance.all_people)
        self.assertIn(self.test_case_instance.fellows[0].office_assigned, self.test_case_instance.offices, "Person hasn't been assigned an office")
        self.assertIn(self.test_case_instance.fellows[0].livingspace_assigned, self.test_case_instance.livingspaces, "Person hasn't been assigned a living-space")


class TestMembersOfRooms(unittest.TestCase):
    def setUp(self):
        self.dojo = Dojo()

    def tearDown(self):
        self.dojo = Dojo()

    def test_member_in_specific_rooms(self):
        self.dojo.create_room("office", ["Overwatch"])
        self.dojo.add_person("Androxus Godslayer", "staff")
        self.dojo.add_person("Samus Aran", "fellow")
        self.dojo.add_person("Christianne Ochieng", "fellow")
        self.dojo.print_room("Overwatch")
        self.assertIn(self.dojo.all_rooms[0].occupants[0], self.dojo.all_people, "Function isn't appending rooms correctly")
        self.assertIn(self.dojo.all_rooms[0].occupants[1], self.dojo.all_people, "Function isn't appending rooms correctly")


class TestAllocationPrintout(unittest.TestCase):
    def setUp(self):
        self.dojo = Dojo()

    def tearDown(self):
        self.dojo = Dojo()

    def test_created_textfile(self):
        self.dojo.create_room("office", ["Overwatch"])
        self.dojo.add_person("Androxus Godslayer", "staff")
        self.dojo.add_person("Samus Aran", "fellow")
        self.dojo.add_person("Christianne Ochieng", "fellow")
        self.dojo.print_allocations("Allocations")
        allocations_file = open("Allocations.txt", "r")
        self.assertIn("Androxus Godslayer", allocations_file)


class TestPrintUnallocated(unittest.TestCase):
    def setUp(self):
        self.dojo = Dojo()

    def tearDown(self):
        self.dojo = Dojo()

    def test_unallocated_people_printed(self):
        self.dojo.add_person("Androxus Godslayer", "staff")
        self.dojo.add_person("Samus Aran", "fellow")
        self.dojo.add_person("Christianne Ochieng", "fellow")
        self.dojo.print_unallocated("Unallocated")
        unallocated_file = open("Unallocated.txt", "r")
        self.assertIn("Samus Aran", unallocated_file)


class TestReallocation(unittest.TestCase):
    def setUp(self):
        self.dojo = Dojo()

    def tearDown(self):
        self.dojo = Dojo()

    def test_person_reallocated(self):
        self.dojo.create_room("office", ["Lenovo"])
        self.dojo.add_person("Androxus Godslayer", "staff")
        self.dojo.create_room("office", ["Lamar", "Risque"])
        self.dojo.reallocate_person("ID", "Risque")
        self.assertEqual(self.all_people[0].office_assigned, "Risque")


class TestLoadPeople(unittest.TestCase):
    def setUp(self):
        self.dojo = Dojo()

    def tearDown(self):
        self.dojo = Dojo()

    def test_loading_people(self):
        loaded_file = open("People.txt", "r")
        initial_people_count = len(self.all_people)
        self.dojo.add_people(loaded_file)
        final_person_count = len(self.all_people)
        self.assertNotEqual(final_person_count - initial_people_count, 0)


class TestDatabase(unittest.TestCase):
    def setUp(self):
        self.dojo = Dojo()

    def tearDown(self):
        self.dojo = Dojo()

    def test_save_to_db(self):


    def test_load_from_db(self):


if __name__ == '__main__':
    unittest.main()
