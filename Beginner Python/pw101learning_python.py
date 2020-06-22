#In this script I will read in a file and print out what the file has

python_file = '/Users/kris/Desktop/Github/Learning Python/Learning-Python/Beginner Python/python_studies.txt'

#This will read the contents of the file with the read method and printing it out as it is in the file
with open(python_file) as file:
    lines = file.read()

print(lines.strip())


#This creates a list and prints the contents of the file and cleans it up
with open(python_file) as file:
    lines = file.readlines()

for line in lines:
    print(line.strip())


#This loops through the lines of the file and creates a list then appends them to a file to read out from that file
with open(python_file) as file:
    lines = file.readlines()

file_string = ''
for line in lines:
    file_string += line

print(file_string)




