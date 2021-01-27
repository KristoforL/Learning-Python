#Going to recreate a previous piece of work and add three ways to exit the code


#This program is ending due to a conditional statement
total_people = input("How many people are seeing a movie:\n")
total_people = int(total_people)

count = 1
price = 0

while count <= total_people:
    age_check = total_people
    age = input("\nHow old is the next:\n")
    age = int(age)

    #This checks the ages given to see what the price is for each person
    if age < 3:
        print("You ticket is free")

    elif age < 13:
        print("Your price is $10")
        price += 10
    else:
        print("Your price is $15")
        price += 15

    count += 1

print(f"\nYour final price is ${price}.00 before tax")


#This one will end when active is false

active = True
price = 0
while active:
    old = input("\nHow old is the viewer\nYou can enter 0 to end the program:\n")
    old = int(old)
    if old == 0:
        print(f"Enjoy the movie. Your final price is ${price}.00 before tax")
        active = False
    
    if old < 3 and old > 0:
        print("You ticket is free")
    elif old > 2 and old < 13:
        price += 10
        print("Your price is $10")        
    elif old > 12:
        price += 15
        print("Your price is $15")


#This will break out of the program completely
#This will continue regardless and will break out when there is a condition that is met

while True:
    old = input("\nHow old is the viewer\nYou can enter 0 to end the program:\n")
    old = int(old)
    if old == 0:
        print(f"Enjoy the movie. Your final price is ${price}.00 before tax")
        break

    if old < 3 and old > 0:
        print("You ticket is free")
    elif old > 2 and old < 13:
        price += 10
        print("Your price is $10")
    elif old > 12:
        price += 15
        print("Your price is $15")
