#This is practice declaring variables, and printing them when they have quotations in them

#Declaring variables for each string I will need
#I will add it into a string and use single quotes for this since it uses double quotation marks. 
first_name = "winston"
last_name = "churchill"
fullname =  f"{first_name} {last_name}"

#This is a success and there are other ways you can do this
print(f'{fullname.title()} once said, "Never, never, never give up"!')

#You can provide the quote as a variable since I am sure this quote will not change and that being the case is a constant 
quote = '"Never, never, never give up"!'

#I will change out the actual quote with the variable replacement and there you go it is there.
print(f'{fullname.title()} once said, '  + quote)

#You could also just type this all out
print('Winston Churchill once said, "Never, never, never give up"!')