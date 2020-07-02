#Going to create a function that takes in two arguements and call the function
#Going to print it out using the positional arguements and then using keyword arguements

def shirt(size, text):
    """Printing a shirt size and what it should say."""
    print(f"Your shirt size is {size} and it will say '{text}'")


shirt('small', 'compact size')

shirt(text='I like pie', size= 'extra large')