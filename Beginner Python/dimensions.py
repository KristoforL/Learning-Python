#A tuple is an immutable list or a list that cannot be changed. This is good for list that will never change such as the size of a shape
#A tuple is defined with parenthesis instead of brackets

dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

#This will cause a type error as we are trying to change a list that is immutable
#dimensions[0] = 250

for dimension in dimensions:
    print(dimension)

#This is not changing the values in the tuple but it is instead declaring a new tuple and with new values because that is how code works
dimensions = (400, 100)
for dimention in dimensions:
    print(dimension)