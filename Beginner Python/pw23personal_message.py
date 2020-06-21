#Delcared a variable
first_name = "kim"
last_name = "neal"

#wrapped this in quotations because it is still a string and thus needs to be wrapped in quotes
fullname = f"{first_name} {last_name}"

#I added the title method in here to make sure the name is properely formatted with capital letters
print(f"Hello Ms. {first_name.title()} {last_name.title()}. I hope that you have been doing well.")
print(f"{fullname.title()}")

"------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"

#Testing to see if I can use single quotes and get the same results

#Delcared a variable in SINGLE QUOTES
first_name = "kim"
last_name = "neal"

#Wrapped this in SINGLE quotations because it is still a string and thus needs to be wrapped in quotes
fullname = f"{first_name} {last_name}"

print(f"Hello Ms. {fullname.title()}. I hope that you have been doing well.")
print(f"{fullname.title()}")

#I can do single quotes but I would only do them for strings that would do not contain apostrophes or just use double quotes and save yourself the headache
#Also make sure you are consistent with the naming convention because I ended up having my code print out the first name twice and I realized I typed first_name and fullname in my print statement