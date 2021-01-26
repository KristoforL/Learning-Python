#This is practice with getting rid of white space before and after a string

#Declare string with white space before and after
#You could just use spaces but I am using tab and nextline to exaggerate the white space being removed
word = "\tspaces?\n"

#Printing string with space and showing there is space on either side
print("----->" + word + "<------")

#All of these now show no spaces on either side or both as you proceed down the printing
print("----->" + word.lstrip() + "<------")
print("----->" + word.rstrip() + "<------")
print("----->" + word.strip() + "<------")
