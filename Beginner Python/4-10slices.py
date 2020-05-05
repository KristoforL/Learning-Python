#I am going to recreate a program made earlier in then add the several small task after it

my_food = ['pizza', 'flafel', 'carrot cake', 'pie', 'cereal', 'chicken']


for food in my_food[:3]:
    print(f"The first three items of the list are {food.title()}")

for food in my_food[2:4]:
    print(f"The three items in the middle of the list are {food.title()}")

for food in my_food[-3:]:
    print(f"The last three items in the list are {food.title()}")