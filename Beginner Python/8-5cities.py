#Going to creaet a functiotn that allows cities and functions to be passed aas arguements

def cities(city, country = 'usa'):
    """Prints out a city and the country it is located in"""
    print(f"{city.title()} is in {country.title()}")


cities('atlanta')

cities('los angelos')

cities('toronto', 'canada')
