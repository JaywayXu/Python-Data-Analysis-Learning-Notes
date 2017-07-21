"""数组合并
维度为0的合并是行数改变但是列数不变
维度为1的合并是列数改变但是行数不变"""
import numpy as np
# A = np.array([1, 1, 1])
# # print(A)
# B = np.array([2, 2, 2])
# """行合并"""
# print(np.vstack((A, B)))  # vertical stack
# """[[1 1 1]
#  [2 2 2]]"""
# """列合并"""
# print(np.hstack((A, B)))
# """[1 1 1 2 2 2]"""
# print(A[np.newaxis, :])  # 对A在行方向上增加一个维度[[1 1 1]]
# print(A[:, np.newaxis])
# """[[1]
#    [1]
#    [1]]"""
# """纵向合并"""
# 将以上结合起来表示就是
A = np.array([1, 1, 1])[:, np.newaxis]
"""
[[1]
 [1]
 [1]]
 """
B = np.array([2, 2, 2])[:, np.newaxis]
"""
[[2]
 [2]
 [2]]
"""
# print(A)
# print(B)
# C = np.vstack((A, B))
"""
[[1]
 [1]
 [1]
 [2]
 [2]
 [2]]
 """
# D = np.hstack((A, B))
"""
[[1 2]
 [1 2]
 [1 2]]
 """
# np.hstack和np.vastack的方法也可以进行三个或者三个元素以上的合并
C = np.concatenate((A, B, B, A), axis=0)  # 这个方法的好处是可以定义axis进行不同维数的合并
print(C)
# [[1]
#  [1]
#  [1]
#  [2]
#  [2]
#  [2]
#  [2]
#  [2]
#  [2]
#  [1]
#  [1]
#  [1]]
D = np.concatenate((A, B, B, A), axis=1)
print(D)
# [[1 2 2 1]
#  [1 2 2 1]
#  [1 2 2 1]]
