import unittest
from city_country import city_country

class CityCoutryTestCase(unittest.TestCase):
    def test_city_country(self):
        """Test pw111city_country.py"""
        cityCountry = city_country('atlanta', 'usa')
        self.assertEqual(cityCountry, "Atlanta is in Usa")

#This is in place because otherwise the class we setup above will return nothing and have the information stored and checked but not returned
#We run the class in the unit test and then the unit test tells us if at line at succeeded
#It will tell us if there are multiple test with the return of how many dots show in the output
#We will know which test failed as well with the traceback and where it failed
if __name__ == '__main__':
    unittest.main()
