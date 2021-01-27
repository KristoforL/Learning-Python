#Going to continue with the restaurant class and add an attribute and method

class Make_Restaurant:
    """This will be the creation of the class"""

    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine
        self.number_served = 0

    def describe_restaurant(self):
        """This will describe the restaurant"""
        print(f"{self.name} is the name of the restuarant and it serves {self.cuisine}")


    def open_restaurant(self):
        print(f"{self.name} is now open")

    def set_number_served(self, served):
        """This is a method that will do the work of changing the number served instead of doing it directly"""
        if served >= self.number_served:
            self.number_served = served
        else:
            print(f"You cannot reduce how many people you have served to {served}")

    def increment_served(self, served):
        """This is add to the number of people served"""
        self.number_served += served



coffee = Make_Restaurant('Code Coffee', 'Coffee')
print(coffee.number_served)
coffee.number_served = 1
print(coffee.number_served)
coffee.set_number_served(5)
print(coffee.number_served)
coffee.set_number_served(1)

print(coffee.number_served)
coffee.increment_served(7)
print(coffee.number_served)
