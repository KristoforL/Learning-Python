
#This is going to continue the earlier assignment and will have to add the name and number to a print out

fav_numbers = {'k': [3, 34], 'j': [3, 15] , 'jq': [15, 5, 11], 'eric': [13, 7], 'waldo': [10, 17], 'bella': [8, 9]}

for name, numbers in fav_numbers.items():
    print(f"{name.title()}'s favorite number are:")
    for number in numbers:
        print(f"{number}")