"""介绍numpy的基本知识"""
import numpy as np

"""[[1, 2, 3],[2, 3, 4]]只是列表形式"""
# 将列表转换为数组
array = np.array([[1, 2, 3], [2, 3, 4]])

print(array)
print('number of dim', array.ndim)  # 数组维数
print('shape', array.shape)  # 数组的形式
print('size', array.size)  # 数组的大小
"""
number of dim 2
shape (2, 3)
size 6
"""