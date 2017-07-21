import numpy as np

a = np.array([2, 23, 4], dtype=np.int)
# print(a.dtype)
b = np.zeros((3, 4))
# print(b)
c = np.ones((2, 3))
# print(c)
d = np.empty((2, 3))
# print(d)
e = np.arange(10, 20, 2)  # [10,20)的间隔为2的区间
# print(e)
f = np.arange(12).reshape((3, 4))
# print(f)
g = np.linspace(1, 10, 6).reshape((2, 3))
# 以1为起点，10为终点，生成均等的5个数的数列
print(g)