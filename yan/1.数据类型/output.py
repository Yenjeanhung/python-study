"""
    该案例演示了输出
"""

# 普通输出
# print("hello world")
# name = "zs"
# age = 20
# print(name , age)

# 默认是\n换行结尾
# print("hello world",end="")
# print("welcome")

# 格式化输出
# 使用%进行占位
# int1 = 11
# float1 = 3.14159
# str1 = "int1 = %d  ,float1 = %.2f" %(int1,float1)
# print(str1)

# 字符串的format方法
# 方式1：不设置指定位置，按默认顺序
# int1 = 11
# float1 = 3.14159
# str1 = "整数是：{}，浮点数是:{}".format(int1,float1)
# # str2 = "整数是：{}，浮点数是:{}".format(float1,int1)
# print(str1)
# print(str2)


# 方式2：设置指定位置，不能和方式1混合使用
# str1 = "整数是：{1}，浮点数是:{0}".format(float1,int1)

# 方式3：设置参数
int1 = 11
float1 = 3.14159
# str1 = "整数是：{aa}，浮点数是:{bb}".format(aa = int1,bb = float1)
str1 = "{aa}, {bb}".format(aa=float1,bb=int1)
print(str1)


# float1 = 31415.9
# str2 = "{:*^20,.2f}".format(float1)
# print(str2)


# print ("{0} 对应的位置是 {0}".format("hello"))   #hello 对应的位置是 hello
# print ("{} 对应的位置是 {{}}".format("hello"))




# int1 = 10
# float1 = 3.14159
# str1 = f"整数是:{int1},浮点数是:{float1}"
# print(str1)

# name = "zsf"
# age = 20
# print(f"我叫{name}，今年{age}岁")

# print("~~~~")
# print(f"int1 ={int1},{{float1=}}")