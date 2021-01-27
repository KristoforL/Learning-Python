#Going to to write to a file in the script and this will overwrite what is in the file every time it is ran.

file = 'programming.txt'

with open(file,'w') as filename:
    filename.write("I love programming\n")
    #Here you can add another string to the file and have two lines
    #It will still overwrite what is already in the file
    filename.write("I love programming\n")

#Here you can append to the file and above it will rewrite the file but now you can append to the file as you need to
with open(file, 'a') as filename:
    filename.write("I love pie\n")
    #Here you can add another string to the file and have two lines
    #It will still overwrite what is already in the file
    filename.write("I love my dogs\n")
