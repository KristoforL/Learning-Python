#Going to loop through the dictionary of rivers and what they run through

rivers = {'mississippi':'usa', 'nile':'egypt', 'amazon':'south america'}

for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}")

for river in rivers.keys():
    print(river.title())

for country in rivers.values():
    print(country.title())