#This is a practice script for copying the list and then copying the list to an empty list

my_food = ['pizza', 'flafel', 'carrot cake']

#This is is not to be confused with setting the list equal to each other. (=)
friend_food = my_food[:]

print("My favorite foods are: ")
print(my_food)
print("\nMy friend's favorite foods are: ")
print(friend_food)

my_food.append('canoli')
friend_food.append('ice cream')

print("My favorite foods are: ")
print(my_food)
print("\nMy friend's favorite foods are: ")
print(friend_food)

#If you do the equal sign instead of the copy method this will set the second list equal to the first list so everything you change in the first list will also be in the second list instead of just copying the content of the orginal list
my_food = ['pizza', 'flafel', 'carrot cake']
friend_food = my_food

print("\nWe are setting the list equal to esch other now and my favorite foods are: ")
print(my_food)
print("My friend's favorite foods are: ")
print(friend_food)

my_food.append('canoli')
friend_food.append('ice cream')

print("As you can see the list are all the same and when you add to one the other will replicate because they are equal to each other and will undergo the same changes")
print("\nMy favorite foods are: ")
print(my_food)
print("My friend's favorite foods are: ")
print(friend_food)


#You can have a third paramter that will skip between items in your range
#As you can see this skipped the 1st and 3rd index 
print(my_food[1:5:2])


