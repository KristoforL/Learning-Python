#Going to just take my loop from the previous assignment and add more terms to it because I have already made a loop

glossary = {
    'tuple:': 'noun\n\tA list in python programming that cannot be altered once created. Tuples can only be restated/declared',
    'argument:': 'noun, adjective\n\tA perameter that is placed in the [],{}, or () to provide information for the method or function or operate with', 'boolean:': 'noun\n\tA true or false output for a comparison statement',
    'sort():': 'noun\n\tA function that when placing a list, dictionary, or tuple it will organize it ascending or descending based of perameters',
    'slice:': 'noun\n\tA section of a list tuple or dictionary that allows you to only few a section of them',
    'append():': 'noun\n\tA function that allows you to add on to strings, integer, list, tuples, and dictionaries' 
}

#This is different because in my previous assignment I basically used the new variable in the for loop and then placed as an argument to get the value for that key
for key, value in glossary.items():
    print(f"{key}, {value}")