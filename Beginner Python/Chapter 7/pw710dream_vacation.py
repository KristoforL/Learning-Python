

vacation = {}

more_vacay = True

while more_vacay:
    name = input("What is your name: ")
    vacay = input("Where is a place you would like to visit: ")

    vacation[name] = vacay

    repeat = input("Would you like to continue putting in vacations? yes/no: ")
    print("\n")
    
    if repeat == 'no':
        more_vacay = False
    
for name, vacay in vacation.items():
    print(f"{name.title()} would like to take a vacation to {vacay}")
