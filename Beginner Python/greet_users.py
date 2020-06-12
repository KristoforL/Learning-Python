#This is a program that will take in a list as an argument and print out a greeting to each person in the list

def greet_users(names):
    """Print a simple greeting to each person in the list"""
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)

usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)