#Going to make a dictionary of people who have favorite places and print them out

fav_places = {'christian': ['japan', 'china', 'new york'], 'corey':['new york','jamaica','uk'], 'kelli':['california', 'spain'], 'toni':['shanghai', 'colorado'], }

for person, places in fav_places.items():
    print(f"{person.title()}'s favorite place or places are")
#This is in place and it is regarding the value of the dictionary keys and will be able to be looped through to display in a cleaner format
    for place in places:
        print(f"{place.title()}")