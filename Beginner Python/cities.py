#Going to request cities tha the use wants to visit and use break to leave a code instead of it continuing to run

prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.)"

while True:
    city = input(prompt)

    if city.lower() == 'quit':
        break
    else:
        print(f"I'd love to go to  {city.title()}!")