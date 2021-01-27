#This will do what I did in 10-6 but will be a loop as to not stop when trying this out

print("Please provide two numbers and I will add them")

while True:
    first_number = input("\nFirst number: ")
    second_number = input("\nSecond number: ")
    try:
        answer = int(first_number) + int(second_number)
    except ValueError:
        print("Please enter numbers")
    else:
        print(answer)
