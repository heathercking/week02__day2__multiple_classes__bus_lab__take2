import unittest
from src.person import Person

class TestPerson(unittest.TestCase):
    def setUp(self):
        self.person = Person("Guido van Rossum", 64, "Ocean Terminal", [22, 30])

    
    def test_person_has_name(self):
        self.assertEqual("Guido van Rossum", self.person.name)

    
    def test_person_has_age(self):
        self.assertEqual(64, self.person.age)

    def test_person_has_destination(self):
        self.assertEqual("Ocean Terminal", self.person.destination)

    def test_person_has_valid_buses(self):
        self.assertEqual([22, 30], self.person.valid_buses)
