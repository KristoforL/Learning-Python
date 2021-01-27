#Going ot have this child class for ice cream since it is a type of restaurant

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


class IceCreamStand(Make_Restaurant):
    
    flavors = ['chocolate', 'vanilla', 'strawberry', 'peanut butter', 'vanilla bean']
    
    def __init__(self, name, cuisine ='ice cream'):
        super().__init__(name, cuisine)
        #Set flavors to an empty list until we know what flavors we have
        self.flavors = []

    def get_flavors(self):
        """Prints all the flavors in the list"""
        print("We have the following flavors:")
        #Cycles through all the flavors in the list for return
        for flavor in self.flavors:
            print(flavor)
       

    #def add_flavors(self, addons = []):
    
    
ICS = IceCreamStand('Ice Palace', 'Ice Cream')
ICS.describe_restaurant()
ICS.flavors= ['chocolate', 'vanilla', 'strawberry']
ICS.get_flavors()