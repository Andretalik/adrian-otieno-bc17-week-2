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

    def test_special_chars(self):
        testing_special = self.dojo.create_room("office", ["**@*!&^@%&"])
        self.assertEqual(testing_special, "Incorrect room name", msg="Program broken by syntax error in create_room method.")


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

    def test_names_special_chars(self):
        testing_names_special = self.dojo.add_person("*(#(&#!))", "#*((#!()))", "fellow", "Y")
        self.assertEqual(testing_names_special, "Incorrect format of person name", msg="Program broken by syntax error in add_person method")

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
        self.dojo.print_allocations("Allocations")
        self.assertTrue(os.path.exists, "*/Unallocated.txt")

    def tearDown(self):
        os.remove("Allocations.txt")


class TestPrintUnallocated(unittest.TestCase):
    def setUp(self):
        self.dojo = Dojo()
        self.dojo.add_person("Androxus", "Godslayer", "staff")
        self.dojo.add_person("Samus", "Aran", "fellow")
        self.dojo.add_person("Christianne", "Ochieng", "fellow")

    def test_unallocated_people_printed(self):
        self.dojo.print_unallocated("Unallocated")
        self.assertTrue(os.path.exists, "*/Unallocated.txt")

    def tearDown(self):
        os.remove("Unallocated.txt")


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
        self.tst = "OLUWAFEMI SULE FELLOW Y\nDOMINIC WALTERS STAFF\n"
        self.tst += "SIMON PATTERSON FELLOW Y\nMARI LAWRENCE FELLOW Y\n"
        self.tst += "LEIGH RILEY STAFF\nTANA LOPEZ FELLOW Y\n"
        self.tst += "KELLY McGUIRE STAFF\nJOHN DOE FELLOW N\n"
        self.tst += "ELIZABETH WARREN STAFF\nJANE DOE FELLOW Y\n"
        self.tst += "ANSLEM OKUMU STAFF\nJULIAN PRINCE FELLOW Y\n"
        test_file = open("People.txt", "w+")
        test_file.write(self.tst)
        test_file.close()

    def test_loading_people(self):
        initial_people_count = len(self.dojo.all_people)
        self.dojo.mass_add_people("People.txt")
        final_person_count = len(self.dojo.all_people)
        self.assertEqual(final_person_count - initial_people_count, 12)

    def tearDown(self):
        os.remove("People.txt")


class TestDatabase(unittest.TestCase):
    def setUp(self):
        self.dojo = Dojo()
        self.dojo.create_room("office", ["Overwatch"])
        self.dojo.add_person("Androxus", "Godslayer", "staff")
        self.dojo.add_person("Samus", "Aran", "fellow")
        self.dojo.add_person("Christianne", "Ochieng", "fellow")

    def test_save_to_db(self):
        self.assertEqual(self.dojo.save_to_db("allocation"), "Data stored in the allocation.db database")

    def test_save_to_db_special_chars(self):
        self.assertEqual(self.dojo.save_to_db("#(@&#&*@)"), "Database name can't have special characters.")

    def test_db_exists_for_loading(self):
        self.dojo.save_to_db("allocation")
        outcome = self.dojo.load_db("allocation.db")
        self.assertEqual(outcome, "Data successfully loaded")
        self.assertEqual(len(self.all_people), 3)

    def test_load_correct_file(self):
        outcome = self.dojo.load_db("sway.docx")
        self.assertEqual(outcome, "Please check for the correct database name.")

    def tearDown(self):
        os.remove("allocation.db")


if __name__ == '__main__':
    unittest.main()
