#Slicing can be done to specify a section of a list that you want to look at or pull into a loop

#You would specify the list you want to use and then instead of one parameter in the brackets you specify the start and the end. 
#Remember that the list is off by one 

players = ['charles', 'martini', 'michael', 'florence', 'eli']
print(players[1:3])

#You can not include the first index and Python will assume that you anything before the second index will be included in the slice.
print(players[:4])

#You cna not include the second index and Python will assume the slice will include everything after the first index
#You can use negative numbers here as well in either indext to help specify an end of beginning when the list is longer than usual
print(players[3:])

#Here is an examaple of using the slice in a for loop
#This will print up until index 3 not including 3 which should be 'charles', 'martini', 'michael'
print("Here are the first three players on my team")
for player in players[:3]:
    print(player.title())

