#Going to create an input where the user tells me their age
#They will then be checked to see what age corresponds to the appropriate price
#Going to loop it all and have them input q when they are done

total_people = input("How many people are seeing a movie:\n")
total_people = int(total_people)


#There is a counter to compare against how many people will be seeing the movie 
#The count is also offset by one because python starts counting from 0 and not from 1
#There is a price to keep track of how much it will be total and present it at the end
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
