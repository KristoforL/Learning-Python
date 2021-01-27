#Here we will import script content so that we do not have remake an entire script
import aribitrary_pizza
#It is not unusual for the import to be yellow underlined as it has not been used yet

aribitrary_pizza.make_pizza('pepperoni')
#This will print all the calls in the script already.
#This is usually for creating a script and calling it a lot in another script so the other information does not get lost in coding

#With this I am calling the specific function from the module so I will not have to usse the dot method
#You could also do this with multiple functions by sepertating them with commas
from aribitrary_pizza import make_pizza

make_pizza('stuffed crust')

#You can change the name of the module or the function like below for better readability or for understanding the purpose
#This way in whatever program I am writing I can tell what the function is supposed to do without looking at the module
import aribitrary_pizza as lotta_toppings
lotta_toppings.make_pizza('no cheese', 'no sauce', 'extra no bread', 'extra delivery box')

from aribitrary_pizza import make_pizza as pizza_pizza
pizza_pizza('thin crust')

#If there is sample code in your program for testing then you can just import all the functions and not the calls
from aribitrary_pizza import *
make_pizza('cheese', 'no pizza', 'just cheese')