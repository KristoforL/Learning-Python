#Take in a dictionary for a car that has make and model
#Takes in as many arbitrary key pair values at the end

def make_car(make, model, **other_details):
    """Make a car and prints the information about it out"""
    other_details['Make'] = make
    other_details['Model'] = model
    return other_details

tesla = make_car('tesla', '3', color='blue', year=2019)
print(tesla)