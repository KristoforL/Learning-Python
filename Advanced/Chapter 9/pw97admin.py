#Inheriting user module functions and using them

class Users:
    """Creates users and stores them"""

    def __init__(self, first_name, last_name, age, state):
        self.first = first_name
        self.last = last_name
        self.age = age
        self.state = state

    def describe_user(self):
        """This will describe the user and return information about the person"""
        print(f"{self.last}, {self.first}\nAge: {self.age}\nLocation: {self.state}")

    def greet_user(self):
        """This will greet the user with a nice message"""
        print(f"Welcome {self.first} {self.last}!")


#Creates a child class and inherits all functions from the user parent class
class Admin(Users):
    """Going to create an admin and grant special permissions that regular users dont have"""
    def __init__(self, first_name, last_name, age, state):
        super().__init__(first_name, last_name, age, state)
        self.privileges =[]

    def show_privileges(self):
        """Shows all the priveleges that the admin has"""
        print(f"{self.first} has the following privileges:")
        for privilege in self.privileges:
            print(privilege)


AA = Admin('JQ','L',26,'Georgia')
AA.privileges = ['Can add post', 'Can edit post', 'Can delete post', 'Can add user', 'Can ban user', 'Can edit user privileges', 'Can delete site']
AA.describe_user()
AA.show_privileges()
