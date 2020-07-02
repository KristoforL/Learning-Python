#Copying the 10-8 work and making it fail silently

cats = 'ats.txt'
dogs = 'dogs.txt'

files = [cats, dogs]

for file in files:
    try:
        with open(file) as animal:
            names = animal.read()
            print(names)
    except FileNotFoundError:
        #print(f"Cannot find this file {file}")
        pass
