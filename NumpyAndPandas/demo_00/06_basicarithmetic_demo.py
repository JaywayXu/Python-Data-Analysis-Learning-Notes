import numpy as np
A = np.arange(2, 14).reshape((3, 4))
B = np.arange(14, 2, -1).reshape((3, 4))  # -1代表步长
print(A)
print(np.argmin(A))  # 计算最小值索引
print(np.argmax(A))  # 计算最大值索引
print(np.mean(A))  # 计算平均值
print(A.mean())
print(np.average(A))  # 计算平均值
print(np.median(A))  # 计算中位数
print(np.cumsum(A))  # 数组个数仍然一样，但是第二个数是前两数之和，第三数是前三数之和以此类推
#  [ 2  5  9 14 20 27 35 44 54 65 77 90]
print(np.diff(A))  # 后一个数减去前一个数的差
"""[[1 1 1]
 [1 1 1]
 [1 1 1]]"""
print(np.nonzero(A))
"""(array([0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2], dtype=int64), 
array([0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3], dtype=int64)) 前面一个数组代表横坐标后一个数组代表纵坐标"""
print(np.sort(A))
"""[[ 2  3  4  5]
 [ 6  7  8  9]
 [10 11 12 13]]"""
print(A.T.dot(A))  # 矩阵转置
print(np.clip(A, 5, 9))  # 将小于5的数划归到5，大于9的数划归到9，范围之中的数保持不变
print(np.mean(A, axis=0))  # axis表示维数，0表示列，1表示行进行计算mean代表平均数值
