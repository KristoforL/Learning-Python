#Create a program that takes in 2 positional values and as many arbitrary ones as possible

#This function will return the information in the given parameter an the positional statement 
def make_profile(first, last, **other_info):
    """Returns info about a person first name last name and random facts"""
    #You are basically making these key pair values by assigning them to first and last name
    other_info['first_name'] = first
    other_info['last_name'] = last
    return other_info

#Creates a list that will have the first and last name along with arbitrary information
JQ = make_profile('j', 'q', state='GA', status='none of your business', hobby='coding in python')
print(JQ)