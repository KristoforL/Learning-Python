#This will be my attempt to create a restaurant class and call it and use it

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
    

all_pizza = Make_Restaurant("JQ's Slices", 'pizza')
print(all_pizza.name)
print(all_pizza.cuisine)
all_pizza.describe_restaurant()
all_pizza.open_restaurant()