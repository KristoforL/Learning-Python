#Sandwich list and for while loops to determine if a sandwich is requested. This check and remove that sandwich from the list.


sandwiches = ['tuna', 'pastrami', 'chicken salad', 'pastrami', 'turkey', 'pbj', 'pastrami']

print("The deli is all out of pastrami. Sorry")
while 'pastrami' in sandwiches:
    sandwiches.remove('pastrami')

for sandwich in sandwiches:
    print(f"{sandwich.title()} is complete")