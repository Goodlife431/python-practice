import unittest
from names_new_function import get_formatted_name


class NamesTestCase(unittest.TestCase):
    # def test_first_last_name(self):
    #     formatted_name = get_formatted_name('janis', 'joplin')
    #     self.assertEqual(formatted_name, 'Janis Joplin')

    def test_first_last_middle(self):
        formatted_name = get_formatted_name(
            "Wolfgang", "Mozart", "Amadeus"
        )
        self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')


unittest.main()
