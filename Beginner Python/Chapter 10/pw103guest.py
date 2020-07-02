#In this script I will prompt a user for their name and add it to a txt file

user = input("What is you name: ")

guest = 'guest.txt'

with open(guest,'w') as guest_name:
    guest_name.write(user)
