#Revisiting Pizzas toppings and having a list in a dictionary to have two items for values in kay pair values

pizza = {
    'crust':'thick',
    'toppings':['mushrooms', 'extra cheese'],
}

print(f"You ordered a {pizza['crust']}-crust pizza with the following toppings:")
for topping in pizza['toppings']:
    print(f"\t{topping}")

