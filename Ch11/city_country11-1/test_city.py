import unittest
from city_fuctions import city_country

class City_country_test(unittest.TestCase):
    """Testing class"""
    def test_city_country(self):
        """Class method for test"""
        formated_name = city_country('santiago', 'chile')
        self.assertEquals(formated_name, "Santiago, Chile")

unittest.main()