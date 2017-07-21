"""基础运算"""
import numpy as np
# a = np.array([10, 20, 30, 40])
# b = np.arange(4)
# # print(a, b)
# # c = a - b
# # c = a + b
# # c = a * b
# # c = b ** 2  # 表示b的平方
# # c = 10*np.sin(a)
# # print(c)
# # print(b < 3)  # [ True  True  True False]
# print(b == 3)  # [False False False  True]
a = np.array(([[1, 1], [0, 1]]))
b = np.arange(4).reshape((2, 2))
# c = a*b
# print(c)  # [[0 1] [0 3]],只是普通的对应位置上相乘
# c_dot = np.dot(a, b)
# c_dot_2 = a.dot(b)
# print(c_dot)  # [[2 4] [2 3]],利用的是矩阵的乘法
# print(c_dot_2)  # 第二种矩阵乘法表示方式
a = np.random.random((2, 4))  # 生成特定shape中的0~1之间的数字
# print(a)
print(np.sum(a, axis=1))  # axis表示对维度求和，其中axis=1表示对列求和，axis=0表示对行求和
print(np.min(a, axis=0))
print(np.max(a, axis=1))