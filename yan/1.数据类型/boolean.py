bool1 = True
bool2 = False

print(bool1, bool2) # True False

""" Python3中，bool 是 int 的子类，True 和 False 可以和数字相加。 """
print(bool1 == 1)
print(bool2 == 0)

print("bool1 + 2 = ", bool1 + 2) # 10

""" 
is 运算符用于比较两个对象的身份（即它们是否是同一个对象，是否在内存中占据相同的位置），而不是比较它们的值。 
"""
print(bool1 is True) # False
print(bool2 is False) # False

""" 
在Python中，能够解释为假的值不只有False，还有：
None
0
0.0
False
所有的空容器（空列表、空元组、空字典、空集合、空字符串）
"""

