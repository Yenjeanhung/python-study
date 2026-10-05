

# 遍历列表
# for num in [1,2,3,4,5,6,7,8,9,10]:
#     print(num)

# 遍历字符串
# for ch in "hello":
#     print(ch)

# 遍历range数列
# for i in range(10):
#     print(i)

# 遍历range数列，从10到1，步长为-2，左闭右开
# for i in range(10, 1, -2):
#     print(i)

# 打印乘法口诀表
print("乘法口诀表")
for i in range(1, 10):
    for j in range(1, i+1):
        print(f"{i}*{j}={i*j}", end="\t")
    print()