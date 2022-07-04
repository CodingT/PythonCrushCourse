class Employee():
    """Class Definition"""
    
    def __init__(self, fname, lname, salary ):
        """Definig class attributes"""
        self.fname = fname.title()
        self.lname = lname.title()
        self.salary = salary

    def give_raise(self, race = 5000):
        """Method to add salary race"""
        self.salary += race
        #return self.salary

#user = Employee('sam', 'brown', 50000)
#user.give_rase()
#print(user.salary)
