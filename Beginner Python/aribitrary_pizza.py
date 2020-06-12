#When you do not know how many arguments you are going to be passing in a function then 

#The asterisk makes an empty tuple called toppings and since it is a tupe it will not be able to be changed
#Print off the actual list
def make_pizza(*toppings):
    """Print the list of toppings that have been replaced."""
    print(toppings)

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')


#Does the same thing and prints out the toppings each one at a time after the arguments have been passed into the tuple
def make_pizza(*toppings):
    """Print the list of toppings that have been replaced."""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")



make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')
