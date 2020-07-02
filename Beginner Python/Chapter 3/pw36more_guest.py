#This is practice to inserting and adding the people to my list who since I got a bigger table

#Declare a list 
guest = ['lorena', 'granny', 'mom', 'kim']
print(f"My current guest list includes {guest}")

#Adding three new people to the list using append, and isnert

guest.insert(0, 'bro')
guest.insert(2, 'toni')
guest.append('dad')
print(f"I added 3 new peoeple since we got a bigger table and now the entire group will include {guest}.")

#Creating strings for the guys and ladies so that I can shorthhand and invite by gender

guys = f"{guest[0]}, {guest[-1]}"
ladies = f"{guest[1]}, {guest[2]}, {guest[3]}, {guest[4]}, {guest[5]}"

print(f"Finally I am happy to say that we will have everyone show up in matching colors.")
print(f"{guys.title()}, I will need you guys to show up in black and turqouise.")
print(f"{ladies.title()}, I will need you to make an appearance in grey")