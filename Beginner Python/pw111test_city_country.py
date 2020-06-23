import unittest
from city_country import city_country

class CityCoutryTestCase(unittest.TestCase):
    def test_city_country(self):
        """Test pw111city_country.py"""
        cityCountry = city_country('atlanta', 'usa')
        self.assertEqual(cityCountry, "Atlanta is in Usa")

if __name__ == '__main__':
    unittest.main()
