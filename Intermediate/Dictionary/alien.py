#Working with dictionaries for the first time


#To create a dictionary you mark curly braces and then have a colon to separate key and values. 
#You separate key value pairs with commas
#If your key value pairs are integers do not put quotes around them unless you expect to output them as strings
alien_0 = {'color': 'green', 'points':5}

#This will print out the value for color and points
#You can do this with the f strings as well
print(alien_0['color'])
print(alien_0['points'])
print(f"{alien_0['color']}")
print(f"{alien_0['points']}")

alien_0 = {'color': 'green', 'points': 5}
new_points = alien_0['points']
print(f"You just earned {new_points} points!")

#We are adding new key value pairs to the dictionary
alien_0 = {'color': 'green', 'points': 5}

alien_0['x-position'] = 0
alien_0['y-position'] = 25
print(alien_0)


#Starting with a empty dictionary

alien_0 = {}

alien_0['color'] = 'green'
alien_0['points'] = 5

print(f"The alien color is {alien_0['color']}")

#Changing the color of the values in the dictionary
alien_0['color'] = 'yellow'

print(f"The alien color is now {alien_0['color']}")


#Adding speed to the alien

alien_0 = {'x-position': 0, 'y-position': 25, 'speed':'medium'}
print(f"Original position {alien_0['x-position']}")

#Move the alien to the right
#Determin how far to move the alien based on its current speed.

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment =2
else:
    #This must be a fast alien
    x_increment = 3

#The new position is the old position plus the increment.
alien_0['x-position'] = alien_0['x-position'] + x_increment

print(f"New position: {alien_0['x-position']}")


#You can use the del function to remove kay value pairs from the dictionary
#When you delete the key pair you do so permanently
alien_0 = {'x-position': 0, 'y-position': 25, 'speed': 'medium'}
print(alien_0)
del(alien_0['x-position'])
print(alien_0)

