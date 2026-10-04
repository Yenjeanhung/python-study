"""
    该案例演示了运算符
"""

# ================算术运算符=====================
# a = 20
# b = 7
# c = a + b
# print(a , "+" , b , "的结果为" , c)
# c = a - b
# print(a , "-" , b , "的结果为" , c)
# c = a * b
# print(a , "*" , b , "的结果为" , c)
# c = a / b  #注意：结果为浮点类型
# print(a , "/" , b , "的结果为" , c)
# c = a % b
# print(a , "%" , b , "的结果为" , c)
# a = 2
# b = 3
# c = a ** b
# print(a , "的" , b , "次方结果为" , c)

# a = -10
# b = 3
# print(a % b)
# c = a // b
# print(a , "//" , b , "的结果为" , c)
# print("-" * 30) # 输出30次-

# ================赋值运算符=====================
# a = 10
# # a = a + 5
# # a += 5
# # print(a)

# print( (b := 20) > a)

# ================比较运算符=====================
# a = 10
# b = 20
# str1 = "15"
# str2 = "6"
# print(str1 > str2)

# ================逻辑运算符=====================
# b1 = True
# b2 = False
# # print(b1 and b2)
# # print(b1 or b2)

# num1 = 8
# num2 = 5
# print(num1 and num2) # 5
# print(not num2) # False

# num1 = 17
# num3 = -12

# print(f"有负数的与运算: {num3} & {num1}: {num1 & num3:08b}")



# ================成员运算符=====================
# list1 = [11,22,33,44]
# print(11 not in list1)


#================身份运算符=====================
list1 = [10,20,30]
list2 = list1

list2 = list1[:]

print(id(list1),id(list2))

print(list1 is list2)
print(list1 == list2)
print(list1)
print(list2)

# =====================海象运算符：赋值同时运算==============================
# num1 = 20
# print((num2 := 3**2) > num1)
# print(num2)


# # -10=-4*3+2
# a = -10
# print(a%3)

# # -8 = -3*3+1
# a = -8
# print(a%3)