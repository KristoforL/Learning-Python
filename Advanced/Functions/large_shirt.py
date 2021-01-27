#Going to make a functionlike 8-3 and set the size to large by default


def shirts(size='large', text="I love python"):
    """Going to print out the size with an I love python message"""
    print(f"Make a {size} size shirt with text that says '{text}'")


shirts()

shirts('medium')

shirts('small small', 'I used to like some certain food')
