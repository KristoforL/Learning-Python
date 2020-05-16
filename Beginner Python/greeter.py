#I am making a greeter script that will return a message to an input collected from the user

name = input("Please enter your name: ")
print(f"\nHi {name}!")

#You can add to a string so that you can save space in the code and not worry about the length of the string for reading purposes

prompt = "\nIf you tell us who you are, we can personlize the message you see."
prompt += "\nWhat is your first name? "

name = input(prompt)
print(f"\nHello, {name}")

#Input is by default taking in as a string and must converted to an integer using the int() method
#This is what it looks like when you do not convert the string to a integer

age = input("\nHow old are you? ")
print(age)
#Because of this when you try to do comparisons to other integers it will fail and this cause errors like below
#age >= 21 

#This is what it looks like when you convert it to an integer
age = int(age)
print(age >= 21)