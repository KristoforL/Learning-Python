#What this script does is take in a number and stores it and then returns the number in astring
import json

#Creates Json
filename = 'fav_number.json'

#This is a function that will get the number and if there is something in the file


def get_fav_number():
    try:
        with open(filename) as f:
            number = json.load(f)
    except FileNotFoundError:
        #Ask for favorite number
        fav_numb = input("What is your favorite number? ")
        #Takes in the number and stores it in the json
        with open(filename, 'w') as f:
            json.dump(fav_numb, f)
    else:
        print(f"I know your favorite number is {number}")

get_fav_number()
