#Adding a while loop to the arsenal of python code and printing out a counting number

current_number = 1

while current_number <= 5:
    print(current_number)
    current_number += 1


#Here we can use Continue to check and then continue from the beginning of code

current_number = 0

while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue

    print(current_number)


print("\n")

#Do not forget that the counter is in place so that you do not create infinite loops

x = 1

while x <= 5:
    print(x)
    x += 1

print("\n")

#This will run forever if not stopped
#Uncomment and run to see tha that it will continually print 1 non stop

x = 1 
#while x <= 5:
    #print(x)