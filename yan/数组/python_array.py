# python形成数组

# v = [0.5, 0.75, 1.0, 1.5, 2.0]
# m = [v, v, v]
# # [[0.5, 0.75, 1.0, 1.5, 2.0], [0.5, 0.75, 1.0, 1.5, 2.0], [0.5, 0.75, 1.0, 1.5, 2.0]]
# print(m)
# print(m[1])
# print(m[1][0])

# 3维数组
# v1 = [0.5, 1.5]
# v2 = [1, 2]
# m = [v1, v2]
# c = [m, m]
# print(c[1][1][0])

# v = [0.5, 0.75, 1.0, 1.5, 2.0]
# m = [v, v, v]
# print(m)

# # 改变v第一个元素
# v[0] = 'python'
# print(m)

# 使用deepcopy深度拷贝
from copy import deepcopy
v = [0.5, 0.75, 1.0, 1.5, 2.0]
m = 3 * [deepcopy(v), ]
print(m)
v[0] = 'python'
print(m)
