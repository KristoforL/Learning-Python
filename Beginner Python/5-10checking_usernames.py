#Making a list of the current users and checking them to see if a name is taken

current_users = ['todd', 'que', 'tim', 'terrrance', 'terryann']

new_users = ['terrance', 'que', 'tim', 'toni', 'curly']
        
users_lower = []

#Converts all the users in current users to lower case and appends to new list for caparison later
for users in current_users:
    users_lower.append(users.lower())

#Checks all users in the new_users against the users in users_lower as to see if the users match
for user in new_users:
    if user.lower() in users_lower:
        print(f"{user} is already taken. Please try another username")
    else:
        print(f"{user} is available for use")