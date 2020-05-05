#This is another practice where I will grab a list from the practice in 4-1

pizzas = ['cheese', 'pepperoni', 'italian sausage']
friends_pizzas = pizzas[:]
print(pizzas)
print(friends_pizzas)

pizzas.append('italian sausage')
print("My favorite pizzas are ")
print(pizzas)

friends_pizzas.append('pineapple')
print("My friends favorite pizzas are ")
print(friends_pizzas)

print("\nMy favorite pizzas are ")
for pizza in pizzas:
    print(pizza)

print("\nWhile my friends pizzas are ")
for pizza in friends_pizzas:
    print(pizza)