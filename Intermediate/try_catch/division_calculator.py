#In this script I will learn about catching exceptions and handling them the way I would like to handle them insted of crashing a program

#This tries the code we want to test
try:
    print(5/0)
#If this code throws thee error we expect then it will enter the except block and do what needs to be done there
except ZeroDivisionError:
    print("You can't divide by zero")

#If it does not print the code above it will return the answer

#Now we will continue this by making a while loop that will continue even if we divide by zero
print("Give me two numbers, and I will divide them")
print("Enter q to quit")

while True:
    first_number = input("\nFirst Number: ")
    if first_number == 'q':
        break
    second_number = input("\nSecond Number: ")
    if second_number == 'q':
        break
    
    # answer = int(first_number)/int(second_number)
    # print(answer)

#I got ahead of myself here and did this prematurely without looking at the book
#You can uncomment this and comment the above answer section to 
    try:
        print(int(first_number)/int(second_number))
    except ZeroDivisionError:
        print("You can't divide by zero. Please try again")