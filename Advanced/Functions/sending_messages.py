#Going ot copy the same thing over from 8-9 and instead take from a list add to an empty list and then print the list

#This is an empty list to append to while we remove items list argument
sent_messages = []
#This is the list of strings that we will be pulling from.
text = ['I like pie', 'I only wish I could have some red velvet cake',
        'I am not good at warzone']

def show_messages(messages):
    """Prints all the messages in a list"""
    print(messages)
    print("Printing messsages:")

    #Used while instead of for loop because the for loop will pop the items and then leave us with 2 items printed at the end 
    while messages:
        removed = messages.pop()
        print(f"{removed}")
        sent_messages.append(removed)

    print("\n")
    print(sent_messages)
    print("All messsages printed!")



show_messages(text)
