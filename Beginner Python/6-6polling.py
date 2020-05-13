#Going to expand upon the list dictionary I already have and will add some names asking those not in the list to take the poll and thank others for taking the poll

favorite_languages = {'jen': 'python', 'sarah': 'c', 'edward': 'ruby', 'phil': 'python', }

need_poll = ['jen', 'jerry', 'karen', 'edward', 'kim']

for name in need_poll:
    if name in favorite_languages.keys():
        print(f"Thank you for you taking the poll {name.title()}!")
    else:
        print(f"Please take the poll {name.title()}")
