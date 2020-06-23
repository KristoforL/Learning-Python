

def count_word(filename):
    """Coutning the words of any file"""

#We are using the encoding because the encoding is different than the systems default
#With this we will try and catch an exception for file not found
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        #You can pass the error and the code will not post that there is a problem
        pass
        #print(f"Sorry but {filename} does not exist")
    #You can place an else at the end of the try exceptions as well
    else:
        #Since there was nothing done in the try then we added an else to do something if the exception did not show
        #Count the appropriate number of words in the file
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words.")


filename = 'alice.txt'
filename1 = 'pi_million_digits.txt'
filename2 = 'little_women.txt'
filename3 = '/little_women.txt'

count_word(filename)
count_word(filename2)
count_word(filename2)

filenames = [filename, filename1, filename3, filename2]
for filename in filenames:
    count_word(filename)



