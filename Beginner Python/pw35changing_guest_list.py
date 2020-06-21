#This is practice to remove the people from my list who cannot make it to the dinner

#Declare a list 
guest = ['eric l.', 'granny', 'kim', 'cookie']

#Pop those people who will not be able to make it becaue I will be printing their names later
#Creating a list to append those guest who cannot make it
rsvp_no=[]

#Letting everyone know that some people cannot make it.
print("Not everyone from the original guest list can make it thee dinner so I will be changing some new naames to the list.")

#Removing the guest who cannot make it and adding them to a new list for using later
#Adding new people to the list in those indexes
rsvp_no.append(guest.pop(0))
guest[0] = 'lorena'
rsvp_no.append(guest.pop())
guest[-1] = 'mom'

#Cleaned it up for printing purposes
rsvp_no_clean = f"{rsvp_no[0]} and {rsvp_no[1]}"

print(f"I am happy to add {guest[0].title()} and {guest[-1].title()} to the dinner.")
print(f"{guest[1].title()} and {guest[-2].title()} are more than happy to have you guys here")

#Testing to see if the list populated with the guest I cannot invite
#It works. (Insert fist pump here)
print(f"Sadly the guest who I cannot attend the dinner are:\n{rsvp_no_clean.title()}")
