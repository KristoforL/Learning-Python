#In this I will make a class called users and create some attributes call first name and last name

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

JQ = Users('JQ','L',26,'Georgia')
KN = Users('K','N',25,'Mississippi')
TMC = Users('T','MC',21,'Georgia')

JQ.describe_user()
JQ.greet_user()

KN.describe_user()
KN.greet_user()

TMC.describe_user()
TMC.greet_user()
