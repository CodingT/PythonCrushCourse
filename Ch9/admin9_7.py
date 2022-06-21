class User():
    """superClass User"""
    
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
        
        
class Admin(User):
    """subClass - chield of User class"""
    
    def __init__(self, first_name, last_name, age):
        """Initiate subClass Attributes from Parent User class"""
        super().__init__(first_name, last_name, age)
        self.privilages = ['can add posts', 'can delete posts', 'can ban users', 'can reset the password']
    
    def show_privilages(self):
        print(f" \n {self.first_name} {self.last_name} is ad Admin, and hes tasks is:")
        for tasks in self.privilages:
            print(tasks)


user5 = Admin('john', 'wane', 33)
user5.describe_user()
user5.show_privilages()
        