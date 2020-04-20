#Declaring string variables (Don't forget the quotations)
first_name = "ada"
last_name = "lovelace"

#The f right before the quotations is too let python know to insert the string value in place of the variable name and this is call an f-string. f is for format and python then knows to use the value of the string in the braces instead of the string name itself
full_name = f"{first_name} {last_name}"

print(full_name)
print(f"Hello, {full_name.title()}!")

#I am not using the f-string to show you how it prints
#Also do no forget that this has changed the full_name string so it will not work with f-string pass this point
full_name = "{first_name} {last_name}"

#As you can tell this is what happens when you do not use the f-string format. It then prints the actual string in the quatation marks
print(full_name)

#This integrates using the f-string to format a string
print(f"Hello, full_name.title()!")

#I figured out the last push. I was not reading the code from top to bottom and missed that the string was changed. ¯\_(ツ)_/¯