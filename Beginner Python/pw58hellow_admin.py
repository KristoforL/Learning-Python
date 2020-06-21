#I will be practicing what I have learned for this where I have to a make a list of 5 usernames and loop to greet through esch one

users = ['marie', 'don', 'chief', 'admin', 'cheese']

for user in users:
    if user.lower() == 'admin':
        print(f"Hello {user}, would you like to see a status report?")
    else:
        print(f"Hello {user.title()}. Thank you for logging in again")

        