#Going to return if an input number from a user is a multiple of 10

number = input("Put in a number and I will tell you if it is a multiple of 10:\n")
number = int(number)

if number % 10 == 0:
    print(f"{number} is multiple of ten")
else:
    print(f"{number} is not a multiple of ten.")

