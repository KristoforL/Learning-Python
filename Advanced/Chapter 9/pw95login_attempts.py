#Going to work on the user class created in 9-3 and add an attributes and methods

class Users:
    """Creates users and stores them"""

    def __init__(self, first_name, last_name, age, state):
        self.first = first_name
        self.last = last_name
        self.age = age
        self.state = state
        self.login_attempts = 0

    def describe_user(self):
        """This will describe the user and return information about the person"""
        print(f"{self.last}, {self.first}\nAge: {self.age}\nLocation: {self.state}")

    def greet_user(self):
        """This will greet the user with a nice message"""
        print(f"Welcome {self.first} {self.last}!")

    def increment_login(self):
        """This will increase by a 1"""
        self.login_attempts += 1

    def reset_login(self):
        """This will reset the attempts the person has made"""
        self.login_attempts = 0
    

user1 = Users('JQ', 'L', 26, 'Georgia')
print(user1.login_attempts)
user1.increment_login()
user1.increment_login()
user1.increment_login()
print(user1.login_attempts)
user1.reset_login()
print(user1.login_attempts)
    
