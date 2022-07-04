import unittest

from employee import Employee

class TestEmployee(unittest.TestCase):
    """Test class for Employee class"""

    def setUp(self):
        """SetUp class to create attributes for test methods"""
        self.user = Employee ('mike','smith', 50000)
    
    def test_give_race(self):
        """Testing metod for def raise"""
        self.user.give_raise()
        self.assertEqual(self.user.salary, 55000)
    
    def test_give_race_custom(self):
        """Testing custom rase amount"""
        self.user.give_raise(10000) 
        self.assertEqual(self.user.salary, 60000)

unittest.main()