"""
    该案例演示了几个关键字的用法
"""
# 打印0-9，跳过偶数。
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)



# 求0-9每个数自己幂自己的加和，如果大于10000000则循环终止
def m1():
    sum = 0
    for i in range(10):
        sum = sum + i**i
        if sum > 10000000:
            # break
            return
        print(f"当前i的值是:{i}sum是: {sum}")
    print("马上下课")

m1()


"""  
pass是空语句，是为了保持程序结构的完整性。
pass不做任何事情，一般用做占位语句。
例如：在一个循环中，如果循环体为空，语法会提示报错，
这个时候我们就可以使用pass占位
"""
for i in range(10):
    pass