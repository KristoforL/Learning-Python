#Going to do what I did in the previous task and do it with animals instead


pets = {
    'waldo': {
        'owner': 'jq',
        'type': 'boxer pitt',
        'location': 'atlanta',
    },

    'bella': {
        'owner': 'lorena',
        'type': 'lab pitt',
        'location': 'atlanta',
    },

    'dillan': {
        'owner': 'jeremy',
        'type': 'lab pitt',
        'location': 'decatur',
    },

    'blue': {
        'owner': 'christian',
        'type': 'lab pittt',
        'location': 'dekalb',
    },

}

#Going to clean this up some and print the name of the pet, where they live, the owner, and the bread at a later
for pet in pets.items():
    print(pet)
