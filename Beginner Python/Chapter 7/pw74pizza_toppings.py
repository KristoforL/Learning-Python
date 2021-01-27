#Going to request someone tell me what they want on their pizza
#I will store it in a list and then return it at the end of the order with final statement that will print out each topping

req_toppings = "What do you want on your pizza: "
req_toppings += "\nEnter quit to stop the program.\n"
final_order = []
active = True

while active:
    request = input(req_toppings)
    
    if request.lower() == 'quit':
        print("You ordered the following toppings: ")
        for topping in final_order:
            print(f"{topping}")
        
        active = False

    else:
        final_order.append(request)
