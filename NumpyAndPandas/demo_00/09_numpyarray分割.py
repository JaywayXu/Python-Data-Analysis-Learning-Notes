import numpy as np
A = np.arange(12).reshape((3, 4))
"""对列进行分割，将列分成两部分"""
print(np.split(A, 2, axis=1))
"""对行进行分割，将其分成三部分"""
print(np.split(A, 3, axis=0))
# 这是这个函数只能把数组分成均等的部分
# 但如果应用array_split函数能够将其分解为不相等的部分。
print(np.array_split(A, 3, axis=1))
print(np.vsplit(A, 3))  # 将其进行纵向的分割
print(np.hsplit(A, 4))  # 将其进行横向的分割