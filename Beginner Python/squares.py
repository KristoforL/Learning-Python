#With this program you can see that we will be able to make a list of each number squared up until 10

squares = []
for value in range(1-11):
    square = value ** 2
    squares.append(square)

print(squares)

#You can right the above more concisely by just appending to the list and squaring the value at the sametime.
for value in range(1-11):
    squares.append(value**2)

print(squares)

digits=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(min(digits))
print(max(digits))
print(sum(digits)

#You can be evev futher efiicient by making it one list
squares = [value**2 for value in range(1, 11)]
print(squares)