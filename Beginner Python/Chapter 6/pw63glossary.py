#Going to create a glossary of programming words that will also have a definition 

glossary = {'tuple:':'noun\n\tA list in python programming that cannot be altered once created. Tuples can only be restated/declared', 
'arguement:':'noun, adjectivce\n\tA perameter that is placed in the [],{}, or () to provide information for the method or function or operate with', 'boolean:':'noun\n\tA true or false output for a comparison statement', 
'sort():':'noun\n\tA function that when placing a list, dicionary, or tuple it will organize it ascending or descending based of perameters', 
'slice:':'noun\n\tA section of a list tuple or dictionary that allows you to only few a section of them', 
'apend():':'noun\n\tA function that allows you to add on to strings, integer, list, tuples, and dictionaries',}


for words in glossary:
    print(f"{words.title()} {glossary[words]}\n")