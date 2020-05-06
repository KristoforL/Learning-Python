#Checking a list to see if there is someone is in the banned users list

banned_users = ['marie', 'Chuckie', 'andrew', 'Susie', 'Taylor']
user = 'Doja'
user1 = 'marie'

if user not in banned_users:
    print(f"{user.title()}, you can post response if you wish")

if user1 not in banned_users:
    print(f"{user1.title()}, you can post response if you wish")
else:
    print(f"{user1.title()}, you can't post!")
