num_1 = 1_000_000
num2 = True
print(num_1)


print(type(num_1))
print(type(num2))


print(isinstance(num_1, int))
print(isinstance(num2, int))
print(isinstance(num2, bool)) # Python3中，bool是int的子类

# ==========================3）小整数池==================================
# num1 = 30
# num2 = 50

# print(id(num1))
# print(id(num2))


num1 = 9999
num2 = 9999

print(id(num1))
print(id(num2))