#We are going to import from sorting.py in multiple way
#Import all cotents of sorting.py
import sorting

numbers = [1, 0, 15, -4, 32, 99, -4]
print(sorting.bubble(numbers))

#Import function soritng from sorting so no need for dot notation
from sorting import sorting

print(sorting(numbers))

#Import sorting from sorting as sort for an alias
from sorting import sorting as sort
print(sort(numbers))

#Import sorting module with alias of sort_all
import sorting as sort_all
print(sort_all.bubble(numbers))

#Imports all functions from module sorting
from sorting import*

