
""" 
当 Python 读取这个文件时，代码行 import pizza 会让 Python 打开文件 pizza.py，并将其中的所有函数都复制到这个程序中。
你看不到复制代码的过程，因为 Python 会在程序即将运行时在幕后复制这些代码。你只需要知道，在 making_pizzas.py 中，可通过导入的模块，使用pizza.py 中定义的所有函数。 
"""

import pizza

pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')