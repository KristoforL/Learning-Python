#Going to loop through a list in and move the items from one list another 


#Start with users that need to be verified
#Create an empty list to hold confirmed users

unconfirmed_users = ['alice', 'brian', 'candance']
confirmed_user = []

#Verify each user until there are no more unconfirmed users
#Move verified users from one list to another

while unconfirmed_users:
    user = unconfirmed_users.pop()
    print(f"Verifying user: {user.title()}")
    confirmed_user.append(user)

print("The following users have been verified")
for person in confirmed_user:
    print(f"{person.title()}")