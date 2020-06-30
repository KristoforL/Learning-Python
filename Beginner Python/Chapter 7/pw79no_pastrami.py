sandwiches = ['tuna', 'pastrami', 'chicken salad', 'pastrami', 'turkey', 'pbj', 'pastrami']

print("The deli is all out of pastrami. Sorry")
while 'pastrami' in sandwiches:
    sandwiches.remove('pastrami')

for sandwich in sandwiches:
    print(f"{sandwich.title()} is complete")