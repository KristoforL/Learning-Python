#This will show how to modify a list in a function

#Start with some designs that need to be printed.
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

#Simulate printing each desisgn, until none are left
#Move each dessign to completed_models after printing.
while unprinted_designs:
    current_design = unprinted_designs.pop()
    print(f"Printing model: {current_design}")
    completed_models.append(current_design)

#Display all completed models.
print("\nThe following models have been printed: ")
for completed_model in completed_models:
    print(completed_model)

print("\n")

#This is the same as above but placed in two functions and takes in the arguments and called to show the same results.
def print_models(unprinted_designs, completed_models):
    """Simulate printing each design, until none are left.
    Move eacah design to completed_models after printing."""
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """Show all the models that were printed"""
    print(f"\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)
    
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)