#This is a script that will ask users for theri opinion on programming and store it in a file

poll = 'poll_response.txt'

cont = True

while cont:
    why = input("Why do you like programming. Enter q when done: ")
    if why == 'q':
        break
    else:
        with open(poll, 'a') as polls:
            polls.write(f"{why}\n")

with open(poll) as complete_poll:
    complete_poll.readlines()