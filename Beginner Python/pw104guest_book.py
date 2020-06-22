#Going to create a while loop that will continue to add users to a list

guest = '/Users/kris/Desktop/Github/Learning Python/Learning-Python/Beginner Python/guestbook.txt'

cont = True
while cont:
    user = input("What is you name. Enter q to quit: ")
    if user == 'q':
        break
    else:
        print(f"Hello {user.title()}")
        with open(guest,'a') as guestbook:
            guestbook.write(f"{user.title()}\n")

with open(guest) as book:
    lines = book.readlines()
    for line in lines:
        print(f"{line.rstrip()}")