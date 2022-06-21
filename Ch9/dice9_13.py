from random import randint

class Die():
    """Die class"""
    def __init__(self, sides = 6):
        """Defininf class Attributes"""
        self.sides = sides
    
    def roll_die(self):
        """Rolling die Method"""
        print(f" {randint(1, self.sides)} ")
        
play_tries = 10
dice = Die()

for i in range(int(play_tries)):
    dice.roll_die()
    