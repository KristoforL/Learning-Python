

import json

username = input("What is your name: ")
filename = 'username.json'

with open(filename, 'w') as f:
    json.dump(username, f)
    print(f"We'll remember you when you come back, {username}!")


#Load the username, if it has been stored previously
#Otherwise, prompt for the username and store it
filename = 'username.json'
try:
    with open(filename) as f:
        username = json.load(f)
except FileNotFoundError:
    username = input("What is your name? ")
    with open(filename, 'w') as f:
        json.dump(username, f)
        print(f"We'll remember you when you come back, {username}!")
else:
    print(f"Welcome back, {username}!")

def greet_user():
    """Greet the user by name"""
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        username = input("What is your name? ")
        with open(filename, 'w') as f:
            json.dump(username, f)
            print(f"We'll remember you when you come back, {username}!")
    else:
        print(f"Welcome back, {username}!")

greet_user()

#This function is to get the username if any in the json file selected
def get_stored_username():
    """Get stored username if available."""
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username
    
get_stored_username()

#This will ask for a username if the username json is empty
def get_new_username():
    """Prompt for a new username"""
    username = input("What is your name: ")
    filename = 'username.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username


#This will use the get stored username function to gather the username and if the return is welcome back then function will end if not then then it will ask for your username
def greet_user1():
    """Greet the user by name"""
    username = get_stored_username()
    if username:
        print(f"Welcome back, {username}!")
    else:
        username = get_new_username()
        print(f"We'll remember you when you come back, {username}.")

greet_user1()
