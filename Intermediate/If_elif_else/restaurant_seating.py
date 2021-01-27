#Going to take in a number for number of guest and then let them know if there is a wait based on the number of people

seating = input("How many people are in your party?\n")
seating = int(seating)

if seating >= 8:
    print("There will be a wait. Is that okay?")
else:
    print("There is a table available. Please follow me.")