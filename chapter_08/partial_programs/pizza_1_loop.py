
"""
星号 * 让 Python 创建一个名为 toppings 的元组，其中包含函数收到的所有（余下的）位置实参。
"""


def make_pizza(*toppings):
    """Summarize the pizza we are about to make."""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')