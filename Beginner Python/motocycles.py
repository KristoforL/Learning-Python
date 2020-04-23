#This is to practice adding, removing, and changing the value of the indexes in a list

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

#This changes the value and the first index to ducati from honda so the list will now start with honda instead of ducati
#I printed the first index before and after the change so that you can see how they differ

print(motorcycles[0])
motorcycles[0] = 'ducati'
print(motorcycles)
print(motorcycles[0])

#Not only can you change the value at indexes but you can add elements to the list
#You will use the .append method and add the parameter which will be the new element you are adding and since this is a string you have to use quotations
#The append method adds it to the end of the list only
motorcycles.append('honda')
print(motorcycles)

#You can append to an emptty list to add to it
motorcycles1 = []
motorcycles1.append('honda')
motorcycles1.append('yamaha')
motorcycles1.append('suzuki')
print(motorcycles1)

#If you would like to add an element but not at the end of the list then you can use the insert() method
#Below I have added ducati and inserted it in place of yamaha and pushing yamaha to the 2 index
motorcycles1.insert(1, 'ducati')
print(motorcycles1)

#We can also remove elements fromt the lsit and through a few ways
#You can use del to remove elements in the list
#Since this something you would do to a list it just a declaration and I will delete the first index in motorcycles1 and show that honda is no longer there
print(motorcycles1)
del motorcycles1[0]
print(motorcycles1)
del motorcycles1[1]
print(motorcycles1)

#You may want to remove an element and use it right away. In this case you would use the pop method
print(motorcycles)
popped_motorcycles = motorcycles.pop()
print(motorcycles)
print(popped_motorcycles)