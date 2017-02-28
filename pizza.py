# pizza
def mix_and_cook():
    print("Flatten out dough")
    print("put tomato sauce on dough")
    print("put cheese and ingredients on dough")
    print("put pizza in oven")
    print("take pizza out of oven in 20 minutes")
def make_pizza(ingredient):
    print("How to make an pizza:")
    mix_and_cook()
    pizza = 'a {} pizza!'.format(ingredient)
    return pizza
def fancy_pizza(*ingredients):
    mix_and_cook()
    fancy_pizza = ' a fancy pizza with {} ingredients.'.format(len(ingredients))
    return fancy_pizza
print(make_pizza('cheese'))
print(make_pizza('pepperoni'))
print(make_pizza('Mushroom'))
print(make_pizza('spinach'))
print(fancy_pizza('sausage', 'onion', 'pepper', 'spinach', 'mushroom', 'tomato',))

