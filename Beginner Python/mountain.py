#Going to use a few inputs to get what a cleaner concise code like I did with movie script in 7-5 exercise

responses = {}

#Set a flag to indicate that polling is active

polling_active = True

while polling_active:
    #Prompt for the persons name
    name = input("\nWhat is your name: ")
    response = input("Which moountain would you like to climb someday: ")

    #Store the reesponse in the dictionary
    responses[name] = response

    #Find out if anyone else is going to take the poll
    repeat = input("Would you like to let another person respond? yes/no: ")

    if repeat =='no':
        polling_active = False

#Polling complete so now we show the results
print("\n----Poll Results----")
for name, response in responses.items():
    print(f"{name.title()} would like to climb {response}.")