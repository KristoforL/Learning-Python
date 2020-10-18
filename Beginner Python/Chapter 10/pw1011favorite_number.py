#What this script does is take in a number and stores it and then returns the number in astring

import json

#Creates Json
filename = 'fav_number.json'

#Ask for favorite number
fav_numb = input("What is your favorite number? ")

#Takes in the number and stores it in the json
with open(filename, 'w') as f:
    json.dump(fav_numb, f)

#This is a function that will get the number and if there is something in the file
with open(filename) as f:
    number = json.load(f)
print(f"I know your favorite number. It is {number}")

