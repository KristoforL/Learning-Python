#This going to be a script where we make a class for making dogs

class Dog:
    #This init method will create a dog with name and age  attribute/arguement
    """A simple attemptto model a dog"""
    def __init__(self, name, age):
        """Initialize name and get attributes"""
        self.name = name
        self.age = age

    #Function for making the dog sit
    def sit(self):
        """Simulate a dog sitting in response to a command"""
        print(f"{self.name} is now sitting")

    #Function for making the dog rolling over
    def roll_over(self):
        """Simulaate rolling over in response to a command"""
        print(f"{self.name} rolled over!")

my_dog = Dog('Willie', 6)
print(f"My dog's name is {my_dog.name}.")
print(f"My Dog is {my_dog.age} years old")

my_dog.sit()
my_dog.roll_over()

your_dog = Dog('Lucy', 3)

print(f"My dogs name is {my_dog.name}")
print(f"My dog is {my_dog.age} years old")
my_dog.sit()

print(f"\nYour dog's name is {your_dog.name}")
print(f"Your dog is {your_dog.age}")
your_dog.sit()

