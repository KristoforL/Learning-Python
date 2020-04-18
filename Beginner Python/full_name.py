#Declaring string variables (Don't forget the quotations)
first_name = "ada"
last_name= "lovelace"

#The f right before the quotations is too let python know to insert the string value in place of the variable name and this is call an f-string. f is for format and python then knows to use the value of the string in the braces instead of the string name itself
full_name = f"{first_name} {last_name}"

print(full_name)

#I am not using the f-string to show you how it prints
full_name= "{first_name} {last_name}"

#As you can tell this is what happens when you do not use the f-string format. It then prints the actual string in the quatation marks
print(full_name)