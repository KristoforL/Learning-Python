#Going to create a function that takes in two arguments and call the function
#Going to print it out using the positional arguments and then using keyword arguments

def shirt(size, text):
    """Printing a shirt size and what it should say."""
    print(f"Your shirt size is {size} and it will say '{text}'")


shirt('small', 'compact size')

shirt(text='I like pie', size= 'extra large')