#This is to practice conditional statements that will do something based on the if statement in the for loop

cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw': #This checks to see if they are the sae value
        print(car.upper())
    
    else:
        print(car)

#Set car to bmw and see that because the print is checking to see if car is equal to bmw it returns true
car = 'bmw'
print(car == 'bmw')

#Set car to audi and because the print is checking to see if the car is equal to bmw it returns false
car ='audi'
print(car == 'bmw')

#Set car to audi and although it is the same Python sees that the cases are different and thinks it is a different car and returns false
car = 'audi'
print(car == 'Audi')

#Sets car to Audi and then changes the print to lower so that we can be specific the case of the car and this time it prints true
car = 'Audi'
print(car.lower() == 'audi')

