def city_country(city, country, population = ''):
    """Gather information about a city and country"""
    if population:
       city_info = f"{city.title()} is in {country.title()} and has a population of {population}"
    else:
        city_info = f"{city.title()} is in {country.title()}"
    return city_info
