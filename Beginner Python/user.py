#Working on looping through users in a dictionary where they have multiple values

user_0 = {
    'username':'efermi',
    'first':'enrico',
    'last':'fermi',
}

#You can return at both the value and keys in a dictionary while looping through it
for key, value in user_0.items():
    print(f"\nKey: {key}")
    print(f"\nValue: {value}")

print("\n")

favorite_languages = {'jen': 'python', 'sarah': 'c', 'edward': 'ruby', 'phil': 'python', }

friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(f"Hi {name.title()}.")

    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")


#You can do this and have a fail safe for when people or items are not in the dictionary

if 'erin' not in favorite_languages.keys():
    print("Erin please take our poll")


#You can even sort a list and then print keys or values in a different order
keys = favorite_languages.keys()
print(f"\n{keys}\n")

for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")


#You can do this even with the value of the dictionary keys
print(f"\n{keys}\n")

for language in (favorite_languages.values()):
    print(language.title())

#For the repeat offenders you can get rid of those by creating a set.
#A set will look for all distinct values that are referenced in the dictionary
print(f"\n{keys}\n")

for language in set(favorite_languages.values()):
    print(language.title())




