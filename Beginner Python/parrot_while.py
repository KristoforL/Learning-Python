#Going to add to this parrot script adn have it not end until someone says quit

prompt = ("Tell me something, and I will repeat it back to you. ")
prompt += "Enter 'quit' to end the program: "

message = ""

while message != 'quit':
    message = input(f"{prompt}\n")
    if message.lower() == 'quit':
        break
    else:    
        print(f"\n{message}\n")


#You can use a flag which is a boolena basically that if true continues the code and if false stops the code from executing

prompt = ("Tell me something, and I will repeat it back to you. ")
prompt += "Enter 'quit' to end the program: "

active = True

while active:
    message = input(f"{prompt}\n")
    if message.lower() == 'quit':
        active = False
    else:
        print(f"\n{message}\n")
