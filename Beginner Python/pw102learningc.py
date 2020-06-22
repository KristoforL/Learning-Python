#This script will replace words in my python studies file

python = '/Users/kris/Desktop/Github/Learning Python/Learning-Python/Beginner Python/python_studies.txt'

with open(python) as py_file:
    lines = py_file.readlines()

#Takes it in as a list replaces Python with C and then prints off each line
for line in lines:
    line = line.strip()
    print(line.replace('Python','C'))
