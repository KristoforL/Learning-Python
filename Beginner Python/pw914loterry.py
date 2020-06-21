#Going to make a lottery ticket generator

from random import choice
from random import randint 

lottery = [34, 3, 5, 15, 21, 47, 20, 17, 25, 26, 'c', 'z', 'l', 'k', 'h']

number = 0
winning_ticket= []
while number<4:
    pick = choice(lottery)
    #originally I was going to put this but I realized that the check would help for making sure numbers and letters are not repeated
    # winning_ticket.append(pick)
    # number+=1

    #If we want to make sure the ticket is unique and the lottery is easier to hit
    if pick not in winning_ticket:
        print(f"We pulled a {pick}!")
        winning_ticket.append(pick)
    number+=1

print(f"Your winning lotto is\n{winning_ticket}")
