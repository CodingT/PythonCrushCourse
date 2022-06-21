

class Restaurant():
    """Class"""
    
    def __init__(self, restaurant_name, cuisine_type):
        """Defining class Attributes"""
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type
        self.number_served = 0
        
    def describe_restaurant(self):
        """Method describe"""
        print(self.restaurant_name + " food type is " + self.cuisine_type)
        
    def open_restaurant(self):
        """Method of the class"""
        print(f" {self.restaurant_name} is Opens 24/7")
     
    def set_number_served(self, number_served ):
        """Method number_served"""
        self.number_served = number_served
         
    def increment_number_served(self, visited_customers):
        """Method to add number of served customers"""
        self.number_served += visited_customers
    
        
        
ny_stake = Restaurant('kins', 'stake house')
#ny_stake.describe_restaurant()
#ny_stake.open_restaurant()
ny_stake.set_number_served(25)
ny_stake.increment_number_served(20)
print(f"\n  The number of served customers at {ny_stake.restaurant_name} is {ny_stake.number_served} ")

#la_pizza = Restaurant("tonny's pizza", 'pizzaria')
#la_pizza.describe_restaurant()        