import unittest
from city_country import city_country


class CityCoutryTestCase(unittest.TestCase):
    def test_city_country(self):
        """Test pw111city_country.py"""
        cityCountry = city_country('atlanta', 'usa')
        self.assertEqual(cityCountry, "Atlanta is in Usa")

        def test_city_country_population(self):
            """Test pw111city_country.py"""
        cityCountry = city_country('atlanta', 'usa', 1_500_000_000_000)
        self.assertEqual(
            cityCountry, "Atlanta is in Usa and has a population of 1500000000000")

if __name__ == '__main__':
    unittest.main()
