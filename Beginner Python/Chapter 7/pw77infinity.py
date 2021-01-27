#I will make this a infinite loop

#This loop is inifinite because the check for age happens outside of the loop and loop continues 
old = input("\nHow old is the viewer\nYou can enter 0 to end the program:\n")
old = int(old)

while True:

    if old == 0:
        print(f"Enjoy the movie.")
        break

    if old < 3 and old > 0:
        print("You ticket is free")
    elif old > 2 and old < 13:
        print("Your price is $10")
    elif old > 12:
        print("Your price is $15")
