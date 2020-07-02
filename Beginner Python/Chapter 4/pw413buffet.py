#Going to declare a menu tuple and then use a for loop to print them

menu = ('chicken', 'pizza', 'mac n cheese', 'fries', 'green beans')
for item in menu:
    print(item)

#This will give a type error because we tried to alter a tuple
#menu[2] = ('pie')

#This will give an entirely new tuple with the new name since the menu changed
menu = ('chicken fingers', 'pizza', 'mac n cheese', 'mashed potatoes', 'green peas')

for item in menu:
    print(item)
