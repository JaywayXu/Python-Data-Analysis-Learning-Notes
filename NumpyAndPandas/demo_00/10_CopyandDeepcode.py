import numpy as np
a = np.arange(4)
b = a
# python中数组的赋值就是把a的所有复制到b中，也就是说此时a和b完完全全就是一个数
c = a
d = b
a[0] = 11
print(a)
# 此时需要判断b和a是不是同一个数
print(b is a)
print(b)
print(c)
print(d)  # 并且此时我们会发现此时A,B,C,D是同样的一个值
"""但是如果此时使用的是deepcopy的方法，这时候就算改变a的值，b的值也不会进行改变"""
b = a.copy() #这时候只是将值复制了过去但是没有进行关联
a[3] = 44
print(a)
print(b)
