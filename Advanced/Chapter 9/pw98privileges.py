#Going to make a separate class for privileges


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

#This is a class that is not a child class and does what the privileges method does in 9-7
class Privileges:
    #Sets a list in the argument so that it is a parameter
    def __init__(self, privileges=[]):
        self.privileges = privileges

    def show_privileges(self):
        """Shows all the privileges that the admin has"""
        print(f"User has the following privileges:")
        if self.privileges:
            for privilege in self.privileges:
                print("- " + privilege)
        else:
            print("- This user has no privileges.")

#Creates a child class and inherits all functions from the user parent class
class Admin(Users):
    """Going to create an admin and grant special permissions that regular users don't have"""

    def __init__(self, first_name, last_name, age, state):
        super().__init__(first_name, last_name, age, state)
        self.privileges = Privileges()




AA = Admin('JQ', 'L', 26, 'Georgia')
AA.describe_user()
privs = ['Can add post', 'Can edit post', 'Can delete post', 'Can add user', 'Can ban user', 'Can edit user privileges', 'Can delete site']
AA.privileges.privileges = privs
AA.privileges.show_privileges()


