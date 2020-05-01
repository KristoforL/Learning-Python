#Going to generate a list of the first 10 cubed numbers but with one line of code
#This is called a list comprehension

cubed = [cube**3 for cube in range(1,11)]
print(cubed)