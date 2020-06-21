#Going tocreate a car class

class Car:
    """This will model what makiing car is like"""
    def __init__(self, make, model, year):
        """This will initialize a car"""
        self.make = make
        self.model = model
        self.year = year
        #This sets a default value to the mileage and is not included in the arguements
        self.odometer_reading = 0
        
    def get_descriptive_name(self):
        """Will return a descriptive name neatly"""
        long_name = f"{self.year} {self.make} {self.model}"
        #Returns all the information from long name instead of printing a string with the information
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the cars mileage"""
        print(f"This car has {self.odometer_reading} miles on it")

    #You can use this to update the odometer reading instead of modifying it directly
    def update_odometer(self,mileage):
        """This will increment the odometer reading and not allow them to reverse the amount of miles"""
        if mileage < self.odometer_reading:
            print(f"You cannot roll back the odometer to {mileage}")
        else:
            self.odometer_reading = mileage
        #You can reverse the above and haave it check if it is equal to or above the mile

    def increment_odometer(self, mileage):
        """This will add to the already existing the odometer reading"""
        self.odometer_reading += mileage

    def fill_gas_tank(self):
        """This will simulatet the gas tank is full"""
        print(f"{self.model} has a full tank")

my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

#You can modify the value for attributes by changing the value directly
my_new_car.odometer_reading = 23
my_new_car.read_odometer()

my_new_car.update_odometer(100)
my_new_car.read_odometer()
my_new_car.update_odometer(7)

my_used_car = Car('subaru', 'outback', 2015)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23500)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()



#When you have a lot in one class you can change the way things are by making another class for organization purposes
class Battery:
    """A simple attempt to model a battery for an electric car"""

    def __init__(self, battery_size=75):
        """Initialize the batterys attributes"""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size"""
        print(f"This car has a {self.battery_size}-kWh battery")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315

        print(f"This car can go abouot {range} miles on a full charge.")




#What I have done here is where we make a child class or invoke inheritance
class ElectricCar(Car):
    """Represents aspects of a car, specific to electric vehicles."""
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()

    #This is a method for this specific type of car
    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery")

    #You can override the fill gas tank method in the car class by copying the method in this child class
    def fill_gas_tank(self):
        """This will simulatet the gas tank is full"""
        print(f"{self.model.title()} does not need gas. It's Electric")

my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.fill_gas_tank()
my_tesla.battery.get_range()