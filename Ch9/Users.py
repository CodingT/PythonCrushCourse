
class User():
    """Class user"""
    
    def __init__(self, first_name, last_name, age):
        """Class Attributes"""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.age = str(age)
        self.login_attempts = 0
    
    def describe_user(self):
        """Method describes user"""
        user_info =f"{self.first_name} {self.last_name} is {self.age} years old."
        print(user_info)
        
    def greet_user(self):
        """Method greats user"""
        print(f" Hello {self.first_name}! \n")
        
    def increment_login_attempts(self):
        """Method to add number of login attempts"""
        self.login_attempts += 1
        
    def reset_login_attempts(self):
        """Method to reset login trys to 0"""
        self.login_attempts = 0     
        
        
        
user1 = User('sam', 'smith', 24)
#user1.describe_user()
#user1.greet_user()
user1.increment_login_attempts()
user1.increment_login_attempts()
print(f" User: {user1.first_name} {user1.last_name} have tried to login {user1.login_attempts} times. ")

user1.reset_login_attempts()
print(f" User: {user1.first_name} {user1.last_name} have tried to login {user1.login_attempts} times. ")

user2 = User('mike', 'stine', 28)
#user2.describe_user()
#user2.greet_user()