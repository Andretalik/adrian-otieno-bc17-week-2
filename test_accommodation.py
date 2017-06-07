import unittest
from dojo_class import Dojo
import os


class TestCreateRoom(unittest.TestCase):
    def setUp(self):
        self.dojo = Dojo()

    def test_create_one_room_successful(self):
        initial_rooms_count = len(self.dojo.all_rooms)
        self.dojo.create_room("livingspace", ["Drangleic"])
        final_rooms_count = len(self.dojo.all_rooms)
        self.assertEqual(final_rooms_count - initial_rooms_count, 1, 'The room has not been created')

    def test_create_multiple_rooms(self):
        initial_rooms_count = len(self.dojo.all_rooms)
        self.dojo.create_room("livingspace", ["Drangleic", "Rockport", "Camden", "Halo"])
        self.assertEqual(self.dojo.all_rooms[0].room_name, "Drangleic", "The rooms have not been created")
        self.assertEqual(self.dojo.all_rooms[2].room_name, "Camden", "The rooms have not been created")
        final_rooms_count = len(self.dojo.all_rooms)
        self.assertEqual(final_rooms_count - initial_rooms_count, 4, "Multiple rooms were not created")

    def test_wrong_syntax_create_room(self):
        testing = self.dojo.create_room("sleepingarea", "Son Goku")
        self.assertEqual(testing, "Incorrect format of room type used. Check help.", msg="Program broken by syntax error in create_room method.")


class TestAddPerson(unittest.TestCase):
    def setUp(self):
        self.dojo = Dojo()
        self.dojo.create_room("livingspace", ["Drangleic", "Rockport", "Camden", "Halo"])
        self.dojo.create_room("office", ["Paladins"])
        self.dojo.add_person("General", "Shephard", "fellow", "Y")

    def test_add_person_fellow_successful(self):
        initial_person_count = len(self.dojo.all_people)
        self.dojo.add_person("Adrian", "Otieno", "fellow", "Y")
        final_person_count = len(self.dojo.all_people)
        self.assertEqual(final_person_count - initial_person_count, 1, 'The person has not been added')

    def test_add_person_staff_successful(self):
        initial_person_count = len(self.dojo.all_people)
        self.dojo.add_person("Master", "Chief", "staff", "Y")
        final_person_count = len(self.dojo.all_people)
        self.assertEqual(final_person_count - initial_person_count, 1, 'The person has not been added')

    def test_wrong_syntax_add_person(self):
        testing = self.dojo.add_person("Kurosaki", "Ichigo", "worker")
        self.assertEqual(testing, "Please enter the person type in the correct format.", msg="Program broken by syntax error in add_person method.")

    def test_person_room_allocation(self):
        self.assertIn(self.dojo.all_people[0].office_assigned, self.dojo.all_rooms, "Person hasn't been assigned an office")
        self.assertIn(self.dojo.all_people[0].livingspace_assigned, self.dojo.all_rooms, "Person hasn't been assigned a living-space")

    def test_member_in_specific_rooms(self):
        self.assertIn(self.dojo.all_rooms[4].occupants[0], self.dojo.all_people, "Function isn't appending rooms correctly")


class TestAllocationPrintout(unittest.TestCase):
    def setUp(self):
        self.dojo = Dojo()
        self.dojo.create_room("office", ["Overwatch"])
        self.dojo.add_person("Androxus", "Godslayer", "staff")
        self.dojo.add_person("Samus", "Aran", "fellow")
        self.dojo.add_person("Christianne", "Ochieng", "fellow")

    def test_created_textfile(self):
        self.dojo.print_allocations("Allocations.txt")
        allocations_file = open("Allocations.txt", "r")
        self.assertIn("Androxus Godslayer", allocations_file)
        allocations_file.close()


class TestPrintUnallocated(unittest.TestCase):
    def setUp(self):
        self.dojo = Dojo()
        self.dojo.add_person("Androxus", "Godslayer", "staff")
        self.dojo.add_person("Samus", "Aran", "fellow")
        self.dojo.add_person("Christianne", "Ochieng", "fellow")

    def test_unallocated_people_printed(self):
        self.dojo.print_unallocated("Unallocated.txt")
        unallocated_file = open("Unallocated.txt", "r")
        self.assertIn("Samus Aran", unallocated_file)
        unallocated_file.close()


class TestReallocation(unittest.TestCase):
    def setUp(self):
        self.dojo = Dojo()
        self.dojo.create_room("office", ["Lenovo"])
        self.dojo.add_person("Androxus", "Godslayer", "staff")
        self.dojo.create_room("office", ["Lamar", "Risque"])

    def test_person_reallocated(self):
        self.dojo.reallocate_person("1", "Risque")
        self.assertEqual(self.dojo.all_people[0].office_assigned.room_name, "Risque")


class TestLoadPeople(unittest.TestCase):
    def setUp(self):
        self.dojo = Dojo()

    def test_loading_people(self):
        loaded_file = open("People.txt", "r")
        initial_people_count = len(self.all_people)
        self.dojo.add_people(loaded_file)
        final_person_count = len(self.all_people)
        self.assertNotEqual(final_person_count - initial_people_count, 0)
        loaded_file.close()


class TestDatabase(unittest.TestCase):
    def setUp(self):
        self.dojo = Dojo()
        self.dojo.create_room("office", ["Overwatch"])
        self.dojo.add_person("Androxus", "Godslayer", "staff")
        self.dojo.add_person("Samus", "Aran", "fellow")
        self.dojo.add_person("Christianne", "Ochieng", "fellow")
        self.dojo.save_to_db("allocation.db")

    def test_save_to_db(self):
        self.assertTrue(os.path.exists, "./db/allocation.db")

    def test_db_exists_for_loading(self):
        self.dojo.load_db("allocation.db")
        self.assertTrue(os.path.exists, "./db/allocation.db")

    def test_load_correct_file(self):
        file_name = "sway.docx"
        self.dojo.load_db(file_name)
        self.assertTrue(file_name[-2:], "db")


if __name__ == '__main__':
    unittest.main()
