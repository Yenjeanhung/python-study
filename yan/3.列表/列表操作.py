from sqlalchemy import true


bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[0].title())

# 取最新一个元素
print(bicycles[-1])

# 在列表末尾插入元素
bicycles.append('a')
print(bicycles)

# 在指定位置前插入元素
bicycles.insert(0, 'b')
print(bicycles)

# 删除第一次出现的元素
bicycles.remove("a")
print(bicycles)

print("========删除指定位置的元素,使用del=========")
# del bicycles[0]
# print(bicycles)

# 删除指定元素，使用pop，pop能将删除元素放到指定变量中
# 不指定索引时删除最后一个元素
popedBicycle = bicycles.pop()
# 弹出指定位置的元素
# popedBicycle = bicycles.pop(0)
print("=================")
print(bicycles)
print(popedBicycle)

# 对元素进行排序，永久生效
# bicycles.sort()
# print(bicycles)

print("=======倒置排序==========")
bicycles.sort(reverse=true)
print(bicycles)

# 临时排序
# print(sorted(bicycles))
# print(bicycles)
