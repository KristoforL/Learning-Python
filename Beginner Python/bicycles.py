#This is to start covering the list and how to declare them
#list are declared with a variable name and the [] brackets with each element in it seperated by a comma
#List are ordered in Python

bicycles = ['trek', 'cannondale', 'redline', 'specialized']

#You can print all content of the list by just printing the list name and it will list it as the raw list
#Because list are ordered in python you can specify which element you want to see and remember you start counting at 0 instead of 1
print(bicycles)
print(bicycles[2])
#If you are trying to print something that is not in the range you will get an out of range error. An example is below
##print(bicycles[9])

#You can adjust the elements in the list the same way you would a string by using the .title .upper() and .lower() methods().
print(bicycles[0].upper())
print(bicycles[1].lower())
print(bicycles[2].title())

#You can get the last element by identifying the -1 index and you can go backwards from there
print(bicycles[-1])
print(bicycles[-2])
print(bicycles[-3])

#You can also format the name of the indexes if they are strings like you would a normal string if it is a string. 
print(bicycles[0].upper())
print(bicycles[1].title())
print(bicycles[2].lower())