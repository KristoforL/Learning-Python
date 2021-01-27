#In this program we will look at defining a function and calling it

#This is a block of code that can be called any where in this code or even in another code
def greet_user():
    """Display a simple greeting."""
    print("Hello")

#We call the block of code here and it return the hello message
greet_user()

#This is the same block of code and as you can see it has a argument in it that now take a name in and uses it in the return
def greet_user(username):
    """Display a simple greeting."""
    print(f"Hello {username.title()}")

#We put in a string in the argument and the return is greeting the user
greet_user('JQ')


#A test to myself is to try and loop this type of function where I ask what the name is and greet the people in the group and end the program when the person says done

#This is an empty list to add names to and a indicator to tell weather to continue later
users = []
asking = True

#While loop that is going to continue while asking is true
while asking:
    
    #Asking for a name 
    your_name = input("What is your name\nEnter done when you are finish: ")
    #Checking to see if the name is actually done before continuing and setting it to lower so it will match whether they use uppercase or lowercase letters
    
    if your_name.lower() != 'done':
        #Appends entries to empty list for later and greets individual user
        users.append(your_name)
        print(f"Greetings {your_name.title()}")
    
    else:
        #This is in case your_name is empty and then we greet all the users stored in users list with a for loop
        print(f"Welcome all the following users")
        for user in users:
            print(f"{user.title()}")
            asking = False
            
