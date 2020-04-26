#Working on organizing list

cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Showing cars list in the original order:")
print(cars)

#Sorting with the sort method is a permanent action and once the sort has happened it does not revert and you cannot revert it to the original order other than by reorganizing it manually.
cars.sort()
print("\nThis is what it looks like after the sort:")
print(cars)

#You can use the reverse peramenter to reverse the sort so it is now Z-A
#This is a permenant sort so the only way to  get it back to A - Z will be to run the sort(reverse=True) again
cars.sort(reverse=True)
print("Now the cars are order from Z to A")
print(cars)
cars.sort(reverse=True)
print(cars)

#If you want to sort a list temporarily the you can use the sorted function
#As you can tell the sorted function is done in the string and not as a method outside a print statement
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("\nHere is the original list:")
print(cars)
print("\nHere is the list after it is temporarily sorted:")
print(sorted(cars))
print("That was a temp sort and now the list has reverted back to the original order:")
print(cars)

#You can reverse the order of the list and with the .reverse() method and this is a premanent function so to reverse you just use rreverse again
print(cars)
cars.reverse()
print(cars)


#You can find the length of the list by using the len() method
#This can be useful when trying to trying to figure how long a list is and taking away from it without going out of range
#You can put the length in an f-string and get the content as seen below
print(f"The length of the cars list is {len(cars)}.")
print(len(cars))

#The below comment is an example of wrong index when it comes to trying to access indexes in a list

#print(cars[6])
#This will show an error index out of range