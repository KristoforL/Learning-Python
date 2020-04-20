#This textt will explain how you can format the strings you are coding

# \t is for adding a tab to the strings you have.
#Adding multiple tabs will tab more
#You can even add tabs between textt
print("\tPython")
print("\t\t\tPython")
print("\tPython is\tthe best")

# \n is for going to the next line and much like \t you can use it the same way when writing code to perform the same task
print("\nPython")
print("\n\n\nPython")
print("\nPython is\nthe best")

#You can mix and combine these to achieve whatever it is you are trying to achieve
print("\nPython is\tthe best")

#Sometimes you do not want there to be white space when checking strings so you can use rstrip, lstrip, or strip
#rstrip will remove all whitespace on the right side of the string
#lstrip will remove all whitespace on the left side of the string
#strip will remove the whitespaces from both side of the string

favorite_language = " python "
#Each case below will show you if there is any spaces on either side of 'pyhton' after being printed
#From the output you will see that each strip does its job by removing the spaces on either side of the word
print("spaces?->"+ favorite_language.rstrip()+ "<-spaces?")
print("spaces?->"+ favorite_language.lstrip()+ "<-spaces?")
print("spaces?->"+ favorite_language.strip()+ "<-spaces?")