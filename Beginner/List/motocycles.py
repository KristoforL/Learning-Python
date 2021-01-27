#This is to practice adding, removing, and changing the value of the indexes in a list
print("###CHANGING THE ELEMENT AT AND INDEX###")
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

#This changes the value and the first index to ducati from honda so the list will now start with honda instead of ducati
#I printed the first index before and after the change so that you can see how they differ

print(motorcycles[0])
motorcycles[0] = 'ducati'
print(motorcycles)
print(motorcycles[0])

print("\n###ADDING ELEMENT TO END OF LIST USING APPEND###")
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

print("\n###ADD ELEMENT TO LIST USING INSERT###")
#If you would like to add an element but not at the end of the list then you can use the insert() method
#Below I have added ducati and inserted it in place of yamaha and pushing yamaha to the 2 index
motorcycles1.insert(1, 'ducati')
print(motorcycles1)

print("\n###DELETING AN ELEMENT FROM LIST USING DEL###")
#We can also remove elements from the list and through a few ways
#You can use del to remove elements in the list
#Since this something you would do to a list it just a declaration and I will delete the first index in motorcycles1 and show that honda is no longer there
print(motorcycles1)
del motorcycles1[0]
print(motorcycles1)
del motorcycles1[1]
print(motorcycles1)

print("\n###POPPING ELEMENTS FROM END OF THE LIST###")
#You may want to remove an element and use it right away. In this case you would use the pop method
#I remove a motorcycle and then I use it immediately
print(motorcycles)
popped_motorcycles = motorcycles.pop()
print(motorcycles)
print(popped_motorcycles)

#I can now assign popped elements from list to a string variable and print it if needed
message = popped_motorcycles
print(message)
message = motorcycles.pop()
print(f"{popped_motorcycles}")
print(f"The last motorcycle I owned was a {message.title()}.")

#You can remove elements from certain spots in the list
print(motorcycles)
first_owned = motorcycles.pop(0)
print(f"The first motocyle I owned was {first_owned.title()}.")

#If you want to decide del or pop just think if you plan on using the element after you have removed it from the list and if so then you will pop it and if you do not need it anymore than you will just delete it.

print("\n###REMOVING ELEMENTS BY VALUE###")
#stating the list and then showing the contents
#Removing the element by value and then printing to show what the list shows now
#If there are multiple of the same elements in the list then the first one seen will be removed.
motorcycles = ['honda', 'yamaha', 'suzuki', 'honda']
print(motorcycles)
motorcycles.remove('honda')
print(motorcycles)

#Removed an element from the dictionary with a variable in place of the actual value
too_expensive = 'honda'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\n{too_expensive.title()} is too expensive for me.")