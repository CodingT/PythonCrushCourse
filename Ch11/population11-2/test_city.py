import unittest
from city_function import city_count_pop

class City_pop_test(unittest.TestCase):
    """Testing class """
    def test_city_country(self): # Methods names in test class should start with 'test_' to autorun tests cases
        """Method to test just city and country"""
        formated_city = city_count_pop('santiago', 'chile')
        self.assertEqual(formated_city, "Santiago, Chile")

    def test_city_count_pop(self):
        """Meththod to test city, country and population"""
        formated_city = city_count_pop('santiago', 'chilie', 500000)
        self.assertEqual(formated_city, "Santiago, Chilie - population is 500000.")

unittest.main()