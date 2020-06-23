#This to practice testing

# def get_formated_name(first, last):
#     """Generate a neatly formated full name"""
#     full_name = f"{first} {last}"
#     return full_name.title()


def get_formated_name(first, last, middle=""):
    """Generate a neatly formated full name"""
    if middle:
        full_name = f"{first} {middle} {last}"
    else:
        full_name = f"{first} {last}"
    return full_name.title()







