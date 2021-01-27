#Going to create a function that allows cities and functions to be passed aas arguments

def cities(city, country = 'usa'):
    """Prints out a city and the country it is located in"""
    print(f"{city.title()} is in {country.title()}")


cities('atlanta')

cities('los angeles')

cities('toronto', 'canada')
