#This will read the pi_digits text file and return contents of it

#You can have the file in the same folder and reference it
#with open('/pi_digits.txt') as file_object:

#You can have the file in a relative folder and use absolute path to the file
with open('/Users/kris/Desktop/Github/Learning Python/Learning-Python/pi_digits.txt') as file_object:

#You chould be able to get the same results with relative path finding as well as long as you know where the 
#with open('../pi_digits.txt') as file_object:

   contents = file_object.read()

#Using strip to get rid of spaces that are placed in the print statement by python
#Could use strip() but it depends on what your desireable outcome is
print(contents.rstrip())
print("\n")

#You can also print it out line by line
with open('pi_digits.txt') as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())


