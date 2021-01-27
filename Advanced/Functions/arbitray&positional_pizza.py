#This will print a pizza and have a positional statement where the size is expected first then all the other toppings that may come with it 

def make_pizza(size, *toppings):
    """Print the list of toppings that have been replaced."""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")


make_pizza(16, 'pepperoni')
make_pizza(22, 'mushrooms', 'green peppers', 'extra cheese')
