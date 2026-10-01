# 浮点数
num1 = 0.1
num2 = 0.2
print(num1 + num2) # 0.30000000000000004

""" 
Python将所有带小数点的数称为浮点数。要注意在使用浮点数进行计算时可能会存在微小误差，可以通过导入decimal解决
"""
from decimal import Decimal

num1 = Decimal('0.1')
num2 = Decimal('0.2')
print(num1 + num2) # Decimal('0.3')

""" 也可以使用科学计数法表示浮点数。 """
num3 = 1.3e7
print(num3) # 1300000.0