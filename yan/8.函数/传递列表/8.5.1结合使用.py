

""" 
    如果要让函数接受不同类型的实参，必须在函数定义中将接受任意数量实参的形参放在最后，例如我们可以在制作前，要求顾客提供尺寸信息： 
"""

def make_pizza(size, *toppings): 
    """概述要制作的披萨""" 
    print(f"\nMaking a {size}-inch pizza with the following toppings:") 
    for topping in toppings: 
        print(f"- {topping}")


make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')