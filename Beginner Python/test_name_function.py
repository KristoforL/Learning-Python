#This is testing with the built in functions

import unittest
from name_function import get_formated_name

class NamesTestCase(unittest.TestCase):
    """Test for name_function.py"""

    def test_first_last_name(self):
        """Do names like janis joplin work?"""
        formatted_name = get_formated_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')
    
    def test_first_middle_last_name(self):
        """Do names like wolfgang amadeus mozart work"""
        formatted_name =  get_formated_name('wolfgang', 'mozart', 'amadeus')
        self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')

if __name__ == '__main__':
    unittest.main()