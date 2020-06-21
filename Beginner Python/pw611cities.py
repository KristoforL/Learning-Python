#Going to create a dictionary or cities and have a string with a fact about the city then print it out

cities = {'atlanta': {'country': 'usa', 'population': 'a lot', 'fact': "it's hot in atlanta"},
          'madrid': {'country': 'europe', 'population': 'a hella lot', 'fact': "it has a renowned soccer team"}, 'japan': {'country': 'asia', 'population': 'a lot for smaller coutry', 'fact': "it's home to the sony headquarters"}, }


#I tested this with one entry in the cities dictionary and with it I was able to see if I could print out the dictionary with a nested for loop
for city, facts in cities.items():
    print(f"Here is a fact about {city.title()}\n")
    for item, facts in facts.items():
        print(f"{item.title()}: {facts}")
