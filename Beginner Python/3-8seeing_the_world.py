#This is practice for organizing list forwards backwards temp and permanent.

vacay = ['spain', 'hawaii', 'japan', 'canada', 'california']

#Print the original list
print(vacay)
#Print the sorted list
print(sorted(vacay))
#Print the original list showing it was a temp sort
print(vacay)
#Print a list using sorted() in the reverse order. You must use the reverse key in sorted arguement
print(sorted(vacay, reverse=True))
#Print vacay to show that it is still in original order
print(vacay)
#Reverse the list
vacay.reverse()
#Print the reverse list
print(vacay)
#Reverse the list back to the original list
vacay.reverse()
#Show that list is back in original order
print(vacay)
#Permanently sort the list and then print it
vacay.sort()
print(vacay)
#Permenantly sort the list and reverse the order so it is Z-A
vacay.sort(reverse=True)
print(vacay)