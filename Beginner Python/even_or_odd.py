#With we take divding a little more into something where we only want the remainder

number = input("Enter a number, and I'll tel you if it's even or odd: ")
number = int(number)

if number % 2 == 0:
    print(f"{number} is even")
else:
    print(f"{number} is odd")