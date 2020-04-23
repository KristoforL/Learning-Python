#This is practice to declare a list and then list every element in the list

#Created a list of people I know
names = ["lorena", "toni", "lon", "kim", "brian"]

#Created variable messages that list every person 
message1 = "Some of the people I know inlcude: " 
message2 = f"{names[0].title()}, {names[1].title()}, {names[2].title()}, {names[3].title()}, and {names[4].title()}. Duh!"

#Concatanate the messages into one
print(message1 + message2)