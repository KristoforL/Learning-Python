#This is calling the function and manually testing 

from name_function import get_formated_name

print("Enter 'q' at any time to quit. ")
while True:
    first = input("\nPlease give me a first name: ")
    if first == 'q':
        break
    last = input("\nPlease gice me a last name: ")
    if last == 'q':
        break
    
    formatted_name = get_formated_name(first, last)
    print(f"\tNeatly Formatted name: {formatted_name}.")