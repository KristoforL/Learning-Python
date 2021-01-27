#Wokring with the list and looping through each index and printing it out

#Declaring a list of magicians
magicians = ['alice', 'david', 'carolina']
 

for magician in magicians: #Can be read for each magician in the list magicians
    print(magician)

#Name the items in the list something that is easy to remember and makes sense with the list like for each cat in cats or dog in dogs. 

#This makes cycling through the list easier and printing each name out in the list and using the title function to format it
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    #You can add more the loop as long as is is till indented after the for loop. This will print for each magician in the list
    print(f"I can't wait to see your next trick {magician.title()}.\n")

#Because this is not indented this this is not part of the loop and prints once
print("Thank you, everyone. That was a great magic show!")


#Again indenting is important and should not be forgot or you will cause a few types of errors depending on where your indent error is
#This is just telling you that the line after the declaration of the for loop is not indeneted and should be. Uncomment the for for and print statement below to see the indent indicator telling you that the block is not indented

#for magician in magicians:
#print(magicians)

#This is not a syntax error but it will not show up in the terminal. It will show in the results and it is called a logical error
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    #Without this indent it will only print for one magician instead of for every magician.
print(f"I can't wait to see your next trick {magician.title()}.\n")


#If you indent something unnecessarily then you will be told as well. Uncomment these below two line to see the unexpected indent error
#message = "This is a message"
    #print(message)

#This will be anaother logical error where you indented by mistake and then leads to an issue that give you a different output then expected
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick {magician.title()}.\n")

    print("Thank you everyone, that was a great magic show!")

#Do not forget the colon as it will help python know that this is supposed to be a for loop. If you uncomment the two line below we will see the red line indicator not knowing what to do with the print statement because the is no colon like it expected.
#for magician in magicians
#    print(f"{magician.title()}, that was a great trick!")

