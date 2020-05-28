#There are several ways of passing arguements to a function

#This is a positional arguement where it matters what you put first in the arguement when calling the function
def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")


describe_pet('boxer, pitt mix', 'waldo')
#If you did this backwards it would not make sense
describe_pet('waldo', 'boxer, pitt mix')

#With the next call we change one thing and make it a keyword arguement. We make sure the keyword is being used when calling the function so there is no confusion
#I put the arguements backwards but it does not matter and still prints correctly
describe_pet(pet_name='waldo', animal_type='boxer, pitt')


#With this function we make one arguements default to a specific value
#When doing this you want to have that preset value at the end of the functions to be taken in by the function

def describe_pet(pet_name, animal_type='dog'):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")


describe_pet("waldo")
#You can still use the arguement name if you want to change it from dog to something another animal
describe_pet('ezekiel', 'cat')


def describe_pet(pet_name, animal_type):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

#Just putting in the function will produce a type error where it cannot find the missing aarguements
describe_pet()
