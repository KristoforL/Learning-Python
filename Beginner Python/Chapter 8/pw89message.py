#This is a code that will take in a list and return everything in a list and returns each in a printt statement

def show_messages(messages):
    """Prints all the messages in a list"""
    print("Printing messsages")
    for message in messages:
        print(f"{message}")
    print("\nAll messsages printed!")

text = ['I like pie', 'I only wish I could have some red velvet cake', 'I am not good at warzone']
show_messages(text)
