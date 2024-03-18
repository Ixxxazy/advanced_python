import unittest
from ..person import Person

class TestPerson(unittest.TestCase):
    def setUp(self):
        self.base_person = Person('Andrew', 2000)

    def test_can_get_correct_name(self):
        name = self.base_person.get_name()
        self.assertEqual(name, 'Andrew')

    def test_can_get_correct_age(self):
        age = self.base_person.get_age()
        self.assertEqual(age, 24)

    def test_can_set_name(self):
        name = 'Alex'
        self.base_person.set_name(name)
        name_after_set = self.base_person.get_name()
        self.assertEqual(name, name_after_set)

    def test_can_get_correct_is_homeless(self):
        self.assertTrue(self.base_person.is_homeless())

    def test_can_get_address(self):
        address = self.base_person.get_address()
        self.assertEqual(address, '')

    def test_can_set_address(self):
        address = 'Wall Street, New York'
        self.base_person.set_address(address)
        address_after_set = self.base_person.get_address()
        self.assertEqual(address, address_after_set)


if __name__ == '__main__':
    unittest.main()
