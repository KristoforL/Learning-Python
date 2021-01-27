#This is practice for the toppings requested and then returns something based on if the requested toppings include a certain value

requested_topping = 'mushroom'

if requested_topping != 'anchovies':
    print("Hold the anchovies")

add_toppings = ['pepperoni', 'italian sausage', 'bacon', 'mushrooms']

for topping in add_toppings:
    if topping == requested_topping:
        print(f"Hold {requested_topping}")
    else:
        print(f"Add {topping}")



#Going to attempt having a list of toppings I do not want and toppings I do want and compare them to each other thn print which to add and which to hold
all_toppings = ['pepperoni', 'italian sausage', 'bacon', 'mushrooms', 'anchovies', 'pineapple', 'olives']
hold_toppings = ['anchovies', 'pineapple', 'mushrooms', 'olives']

for topping in hold_toppings:
    check = topping
    for all in all_toppings:
        if all == check:
            print(f"Hold {check}!")


