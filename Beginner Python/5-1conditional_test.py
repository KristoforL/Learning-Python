#This is a set of conditional statements to practice 

name = 'Jacquawn'
print("Is name == 'jacquawn'? I predict false")
print(name == '=jacquawn')

#Since this is an integer you do not need to use quotation and if you do it will read it as a string in the comparison and will consider it false even if it is true
year = 2099

print("Is year == '2099'? I predict true")
print(year == 2099)

print("Is year == '2099' and name == 'jacquawn'? I predict false")
print(year == 2099 and name == 'jacquawn')

print("Is name == 'Jacquawn' and year == 2099? I predict true")
print(name == 'Jacquawn' and year == 2099)

print("Is year == '2099' or name == 'jacquawn'? I predict true")
print(year == 2099 or name == 'jacquawn')

print("Is name == 'jacquawn' or year == 2098? I predict false")
print(name == 'jacquawn' or year == 2098)

print("Is name == 'jacquawn' or year == 2099? I predict true")
print(name == 'jacquawn' or year == 2099)

print("Is name == 'jacquawn'? I predict true")
print(name.lower() == 'jacquawn')

print("Is year == '2099'? I predict false")
print(year == '2099')

print("Is name == 'JACQUAWN'? I predict false")
print(name == 'JACQUAWN')
