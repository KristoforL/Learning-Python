#Going ot copy the same thing over from 8-10 and instead take from a list then adding to an empty list and then print the list
#We will be copying the list and print both showing the orignal list was never removed

#This is an emepty list to append to while we remove items list argument
sent_messages = []
#This is the list of strings that we will be pulling from.
text = ['I like pie', 'I only wish I could have some red velvet cake',
        'I am not good at warzone']


def show_messages(messages):
    """Prints all the messages in a list"""
    print("Printing messsages:")

    #Used while instead of for loop because the for loop will pop the items and then leave us with 2 items printed at the end
    while messages:
        removed = messages.pop()
        print(f"{removed}")
        sent_messages.append(removed)

    print("\n")
    print(sent_messages)
    print("All messsages printed!")


show_messages(text[:])

print(f"The original list of messages is {text},\nand it was unchanged")
print(f"The new list the files were copied to for the program are here: {sent_messages}")
print(f"In the previous scripts the list was not copied and removed the files from the list emptying it.")
