import numpy as np
"""一维数组"""
# A = np.arange(3, 15)  # [ 3  4  5  6  7  8  9 10 11 12 13 14]
# print(A)
# print(A[3])  # 6
A = np.arange(3, 15).reshape((3, 4))
print(A)
"""二维数组"""
"""[[ 3  4  5  6]
 [ 7  8  9 10]
 [11 12 13 14]]
 """
# # 输出第二行
# print(A[2])  # [11 12 13 14]
# # 输出第二行第一列
# print(A[2][1])
# print(A[2, 1])
# # 输出第二行所有数
# print(A[2, :])
# # 输出第一列所有数
# print(A[:, 1])
# # 对于值的索引不包括上界
# print(A[1, 1:3])
# 行迭代模式，print所有的行
for row in A:
    print(row)
# 列迭代模式，print所有的列，即先将原有的数组进行转置
for column in A.T:
    print(column)
# 迭代输出所有的item,实现形式主要是将原有数组化为单行数组
for item in A.flat:
    print(item)