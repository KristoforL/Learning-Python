#In this script although I am making a copy of the restaurant class

class Make_Restaurant:
    """This will be the creation of the class"""

    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine

    def describe_restaurant(self):
        """This will describe the restaurant"""
        print(f"{self.name} is the name of the restuarant and it serves {self.cuisine}")

    def open_restaurant(self):
        print(f"{self.name} is now open")


ramen = Make_Restaurant('Oodles of noodle', 'japanese')
pasta = Make_Restaurant('Pasta Palace', 'italian')
breakfast = Make_Restaurant('AM', 'breakfast')

breakfast.describe_restaurant()
pasta.describe_restaurant()
ramen.describe_restaurant()
