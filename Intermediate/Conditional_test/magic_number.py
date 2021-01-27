#This is to practice with the comparing numbers

answer = 17

if answer != 42:
    print("That is not the correct answer. Please try again!")

#This is setting age to a value and then printing comparisons to see if the statement is true
#Age is less 21 which is true
age = 19
print(age <21)

#Age is less then or equal to 21
print(age<=21)

#Age is not greater than 21
print(age>21)

#Age is not greater than or equal to 21
print(age>=21)

age_0 = 22
age_1 = 18

#You can use the and/or modifiers to do further comparisons
print(age_0 >= 21 and age_1 >= 21)

age_1 = 21
print(age_0 >= 21 and age_1 >= 21)

age_0 = 22
age_1 = 18

print(age_0 >= 21 or age_1 >= 21)

age_0 = 18
print(age_0 >= 21 or age_1 >= 21)

#You can even check true or false for values in a list

toppings = ['pepperoni', 'italian sausage', 'bacon', 'mushrooms']

print('pepperoni' in toppings)
print('olives' in toppings)