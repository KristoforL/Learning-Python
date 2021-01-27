#This is a script that will cover some good points in when dealing with numbers

#You have to print these or they will not show in the console.
#Basic operations
print(2+3)
print(3-2)
print(2*3)
print(3/2)

print("\n")

#This is using the exponents
print(3**2)
print(3**3)
print(10**6)

print("\n")

#Floats will be the default result if the equation includes floats
#All these will result in a float
print(.1 + .1)
print(.2 + .2)
print(2 *.1)
print(2* .2)

#Sometimes there will be a lot of unnecessary zeroes but they will be printed out per python programming
print("\n")

#You can use underscores in integers and when they are printed they will exclude the underscore and display the normal

universal_age = 14_000_000_000
print(universal_age)

print("\n")

#You can set multiple variable to numbers at one time and this is only new in 3.6^
#This could be helpful when dealing multiple constant variables or variables that will be changing
#All of these are set to 0 at the moment
x, y, z = 0, 0, 0

#I will attempt to change them and set them equal to each other
#This works and you can set them to be operated on
x = 7
y, z = x+4, x-9

print(x)
print(y)
print(z)

print("\n")

#When stating a constant usually it is indicated by the variable name being all capital letters

MAX_CONNECTIONS = 5000
