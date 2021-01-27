#This will read a file and introduce an encoding type

filename = 'alice.txt'

#We are using the encoding because the encoding is different than the systems default
#With this we will try and catch an exception for file not found
try:
    with open(filename, encoding='utf-8') as f:
        contents =f.read()
except FileNotFoundError:
    print(f"Sorry but {filename} does not exist")
#You can place an else at the end of the try exceptions as well
else:
    #Since there was nothing done in the try then we added an else to do something if the exception did not show
    #Count the appropriate number of words in the file
    words = contents.split()
    num_words = len(words)
    print(f"The file {filename} has about {num_words} words.")


title = "Alice in Wonderland"
#This splits the title and makes it a list but does nto keep the changes
title.split()
print(title)
#You would have to print the split to see the changes that occurs in the split
print(title.split())

