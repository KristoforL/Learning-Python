filename = '/Users/kris/Desktop/Github/Learning Python/Learning-Python/Beginner Python/cocoa_and_chocolate.txt'
filename1 = '/Users/kris/Desktop/Github/Learning Python/Learning-Python/Beginner Python/little_women.txt'
filename2 = '/Users/kris/Desktop/Github/Learning Python/Learning-Python/Beginner Python/alice.txt'


def count_words(book, word):
    """Going to count the words in the file"""
    #Simple open a file
    #Read the file
    #Count the word appearance in the file
    with open(book, encoding='utf-8') as f:
        lines = f.read()

        count = lines.lower().count(word)
    print(count)


count_words(filename, 'cake')
count_words(filename1, 'women')
count_words(filename2, 'wonderland')