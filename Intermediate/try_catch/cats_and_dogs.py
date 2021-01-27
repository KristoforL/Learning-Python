#This will read a list of files and perform a print of the files content


cats = 'cats.txt'
dogs = 'dogs.txt'

files = [cats, dogs]

for file in files:
    try:
        with open(file) as animal:
            names = animal.read()
            print(names)
    except FileNotFoundError:
        print(f"Cannot find this file {file}")