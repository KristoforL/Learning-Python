import json

filename = 'username.json'
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


#This will ask for a username if the username json is empty


def get_new_username():
    """Prompt for a new username"""
    username = input("What is your name: ")
    filename = 'username.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username


#This now checks to see if the last person who logged in is logging in again and if so we say hello and if not we gatther the new information
def greet_user1():
    """Greet the user by name"""
    username = get_stored_username()
    if username:
        check = input(f"Is this {username}? y/n: ")
        if check == 'y':
            print(f"Welcome back, {username}!")
        else:
            username = get_new_username()
            print(f"We'll remember you when you come back, {username}.")
    else:
        username = get_new_username()
        print(f"We'll remember you when you come back, {username}.")
greet_user1()
