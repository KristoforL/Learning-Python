#Creating a function that takes in a list of items for a sandwich
#It should be able to take in as many items as you want
#It will return a summary of the sandwich you ordered 

def make_sandwich(toppings):
    """This will take in toppins from a list and print all toppings in back in a nice message"""
    print("You ordered a sandwich with the following:")
    for topping in toppings:
        print(f"{topping}")

items = ['turkey', 'cheese', 'no pickle', 'no mayo', 'no mustard', 'no tomato', 'fruit punch']
make_sandwich(items)
print("\n")
items = ['turkey', 'cheese', 'no pickle', 'no mayo', 'no mustard']
make_sandwich(items)
print("\n")
items = ['turkey', 'cheese', 'no pickle', 'no mayo', 'no mustard', 'no tomato', 'pie', 'pizza', 'hot sauce']
make_sandwich(items)
print("\n")
