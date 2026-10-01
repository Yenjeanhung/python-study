test = {
    'a': 1,
    'color': 'red',
    'c': 3,
    'd': 4
}
# print(test)
# print(test['color'])

# # 在末尾添加一个元素
# test['score'] = 100
# print(test)

# # 修改元素的值
# test['d'] = 40
# print(test)


# print("==========通过pop删除元素==========")
# test2 = test.pop('color')
# print(test)
# print(test2)


print("==========通过del删除元素==========")
del test['c']
print(test)