""" while 循环测试 """


import time


# 模拟进度条加载
# num = 1
# while num  < 100:
#     print("\r" + "=" * num, end="")
#     num += 1
#     time.sleep(0.05)


# while还可以加else语句
rabbit = 2
week = 1
while week < 10:
    rabbit = rabbit + rabbit * 2
    week += 1
else:
    print(f"第{week}周有{rabbit}只兔子")