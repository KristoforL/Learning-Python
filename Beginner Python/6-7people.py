#Going to create a list of users to printt out information for everyone in the list

people = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'priniceton',
    },

    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },

    'dcurry': {
        'first': 'denzel',
        'last': 'curry',
        'location': 'usa',
    },

    'jcole': {
        'first': 'jermaine',
        'last': 'cole',
        'location': 'north carolina',
    },

}

#Going to clean this up some later and provide name first and last and where they are
for person in people.items():
    print(person)