from random import randint

class Die():
    """Class representing a single die"""
    def __init__(self, num_sides=6):
        self.num_sides = num_sides

    def roll(self):
        """returns random value between 1 and num of sides"""
        return randint(1, self.num_sides)