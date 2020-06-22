
filename = 'pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = '' 
for line in lines:
    #In this case we would use strip because without strip it will print the pi digits with spaces between each line that is added to the string
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))

print("\n")

#It did work with relative path but for some reason now it is only working with absolute path
filename1 = '/Users/kris/Desktop/Github/Learning Python/Learning-Python/Beginner Python/pi_million_digits.txt'
with open(filename1) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    #In this case we would use strip because without strip it will print the pi digits with spaces between each line that is added to the string
    pi_string += line.strip()

print(f"{pi_string[:52]}...")
print(len(pi_string))


print("\n")

#You can check the contents of a document to see if it contains a string within it

birthday = input("What is your birthday mmddyy: ")
#you have to search your birthday in the newly created pi_string
if birthday in pi_string:
    print(f"You birthday is in the first million digits of pi\n{birthday}")
else:
    print(f"{birthday} is not in the first million digits of pi")
