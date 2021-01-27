#In this exercise I am asked to print out numbers from 1-20 using a for loop

#Declare a list and print every element in the list
twenty = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

for number in twenty:
    print(number)

#Print each number in a range
for number in range(1, 21):
    print(number)

#Declare an empty list and append to the list then print the list
count = []
for number in range(1, 21):
    count.append(number)

print(count)
