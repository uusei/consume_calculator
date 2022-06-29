# 增加点数
def addit(a, b):
    a = a + b
    return a


# 线缆时间
def ex_addtime(a):
    return a * 5


# 附加点数计算
def ex_add(a):
    return a * 15


# 计算所需时间(分钟)
def enoughtime(a, b):
    a = (a + b) * 0.8
    return a


# 分段处理设置时间
def changeit(x):
    if (x - int(x)) < 0.25:
        return int(x) + 0.5
    elif ((x - int(x)) >= 0.25) & ((x - int(x)) < 0.5):
        return int(x) + 0.75
    elif ((x - int(x)) >= 0.5) & ((x - int(x)) < 0.75):
        return int(x) + 1
    elif (x - int(x)) >= 0.75:
        return int(x) + 1.25


# 分段加时
def time_extra(x):
    if x < 30:
        return 0
    elif (x >= 30) & (x < 50):
        return 15
    elif (x >= 50) & (x < 70):
        return 30
    elif (x >= 70) & (x < 90):
        return 45
    elif (x >= 90) & (x < 110):
        return 60
    elif x >= 110:
        return 75
