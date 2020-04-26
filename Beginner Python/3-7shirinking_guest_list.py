#This is practice removing people from the list using the pop method. 

#Declare a list
guest = ['jeremy', 'lorena', 'toni', 'granny', 'mom', 'kim', 'dad']

#I used the pop method at index 0 because as they print they remove the first index and reduce the list
print(f"Sorry {guest.pop(0)}, they just called back and said I can only have 2 guest. I will catch you back at your place.")
print(f"Sorry {guest.pop(0)}, they just called back and said I can only have 2 guest. I'd love you to meet them butt I want to meet them instead.")
print(f"Sorry {guest.pop(0)}, they just called back and said I can only have 2 guest. We will have to gt you guys together soon though.")
print(f"Sorry {guest.pop(0)}, they just called back and said I can only have 2 guest. I want you to meet her in person when she gets back")
print(f"Sorry {guest.pop(0)}, they just called back and said I can only have 2 guest. I have talked to you over he phone and will be looking forward to seeing you in person.")

#Printing pictures to those who are still invited
print(f"{guest[0].title()}, are you suer that I have nothing to worry about, when I meet your dad.")
print(f"Hello Mr. {guest[1].title()}. How are you? I am glad that you were able to mnake it to dinner today.")

#Going to delete the only 2 left in the list
print(guest)
del guest[0]
del guest[0]
print("Now looking at the list after using the delete method this should be empty brackets")
print(guest)