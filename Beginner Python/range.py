#This is to practice the range fucntion that is built into python

#What this function does is generate a series of numbers
#This code will only print 1-4 because of the one off count. This means that if the next number is the number listed in the range parameter then it will exit the for loop

for value in range(1, 5):
    print(value)

for value in range(1, 6):
    print(value)

#If you just state one number in the range perameter then it will start the index from 0.

for value in range(9):
    print(value)

#You can even make a list using the range fucntion
rangeList = list(range(1,10))
print(rangeList)