#This time we will be the alien python script but with no points and an error

#This will produce a key value error and show a trace that nothing is there
#Uncomment the print to see the trace to the error
alien_0 = {'color':'green', 'speed':'fast'}
#print(alien_0['points'])

#You can use a different method and get the value you want with a cleaner return if the value does not exist 
#You can use the get() meethod and it only needs one argument but if you put in a second argument then you that will be your output

point_value = alien_0.get('points', 'No point value assigned.')
print(point_value)

#You would use this type of get() method when you know there might be chance to have something fail to retrieve

