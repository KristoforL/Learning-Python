#This will divide numbers and stop the error from showing if there is a letter put in instead of a number

print("Please provide two numbers and I will add them")

first_number = input("\nFirst number: ")
second_number = input("\nSecond number: ")

try:
    answer = int(first_number) + int(second_number)
except ValueError:
    print("Please enter numbers")
else:
    print(answer)
