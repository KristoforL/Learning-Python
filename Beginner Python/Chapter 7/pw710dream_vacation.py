
#There is list a dictionary created and a while loop is created so that you can add to the dictionary the key and value then when the loop is over the dictionary is printed with each person and the place they want to visit.

vacation = {}

more_vacay = True

while more_vacay:
    name = input("What is your name:\n")
    vacay = input("Where is a place you would like to visit:\n")

    vacation[name] = vacay

    repeat = input("Would you like to continue putting in vacations? yes/no:\n")
    
    if repeat == 'no':
        more_vacay = False
    
for name, vacay in vacation.items():
    print(f"{name.title()} would like to take a vacation to {vacay}")
