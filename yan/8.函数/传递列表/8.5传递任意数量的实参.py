# """ def make_pizza(*toppings): 
#     """打印顾客点的所有配料""" 
#     print(toppings) """


def make_pizza(*toppings): 
    """打印顾客点的所有配料""" 
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')