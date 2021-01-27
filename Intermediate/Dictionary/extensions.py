#I am going to get this favorite languages program and fix it up some

favorite_languages = {
    'jen': ['python', 'c++', 'c#'], 
    'sarah': ['c', 'brain fuck'], 
    'edward': ['ruby', 'java'], 
    'phil': ['python', 'javascript']
}

for names, languages in favorite_languages.items():
    print(f"\n{names.title()}, I noticed your favorite languages are:")
    for language in languages:
        print(f"{language.title()}")
    print()