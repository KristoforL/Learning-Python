#Importing classes from modules

#This will still print everything else because we took all the code in the class
from car import Car

my_new_car = Car('audi','a4',2019)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()

from car import Car, ElectricCar

my_beetle = Car('volkswagon','beetle', 2019)
print(my_beetle.get_descriptive_name())

my_tesla = ElectricCar('tesla','roadster',2019)
print(my_tesla.get_descriptive_name())

import car
import car as wheels