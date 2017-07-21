"""pandas各种合并方式"""
import pandas as pd
import numpy as np

# #  首先创建三个DataFrame
# df1 = pd.DataFrame(np.ones((3, 4))*0, columns=['a', 'b', 'c', 'd'])
# df2 = pd.DataFrame(np.ones((3, 4))*1, columns=['a', 'b', 'c', 'd'])
# df3 = pd.DataFrame(np.ones((3, 4))*2, columns=['a', 'b', 'c', 'd'])
# print(df1)
# print(df2)
# print(df3)
# # 对数据集进行合并操作,用axis表示合并的方向，其中axis=0表示竖直方向上的合并，axis=1表示横向上的合并
# res = pd.concat([df1, df2, df3], axis=0, ignore_index=True)
# print(res)

# join,['inner','outer']
#  可以处理要合并行中和列中不一样的部分
# df1 = pd.DataFrame(np.ones((3, 4))*0, columns=['a', 'b', 'c', 'd'], index=[1, 2, 3])
# df2 = pd.DataFrame(np.ones((3, 4))*1, columns=['b', 'c', 'd', 'e'], index=[2, 3, 4])
# print(df1)
# print(df2)

# res = pd.concat([df1, df2], join='outer')  # 直接进行合并,默认合并模式'outer'
# print(res)
# a    b    c    d    e
# 1  0.0  0.0  0.0  0.0  NaN
# 2  0.0  0.0  0.0  0.0  NaN
# 3  0.0  0.0  0.0  0.0  NaN
# 2  NaN  1.0  1.0  1.0  1.0
# 3  NaN  1.0  1.0  1.0  1.0
# 4  NaN  1.0  1.0  1.0  1.0
# 如果使用inner模式的话，得到的结果不同
"""只寻找两组数据中相同的部分，把不同的部分裁减掉"""
"""ignore_index=True表示的是将index重复的部分重新排列"""
# res = pd.concat([df1, df2], join='inner', ignore_index=True)
# print(res)
#      b    c    d
# 0  0.0  0.0  0.0
# 1  0.0  0.0  0.0
# 2  0.0  0.0  0.0
# 3  1.0  1.0  1.0
# 4  1.0  1.0  1.0
# 5  1.0  1.0  1.0
# res = pd.concat([df1, df2], axis=1, join_axes=[df1.index])
# print(res)
# 进行左右合并，并且以df1的index项作为标准，df2中没有的用Nan代替，对方中多出来的则删除掉
#      a    b    c    d    b    c    d    e
# 1  0.0  0.0  0.0  0.0  NaN  NaN  NaN  NaN
# 2  0.0  0.0  0.0  0.0  1.0  1.0  1.0  1.0
# 3  0.0  0.0  0.0  0.0  1.0  1.0  1.0  1.0
# res = pd.concat([df1, df2], axis=1)
# print(res)
"""如果不设置join_axes的话，则是全连接的方式，df1和df2的index都做考虑"""
#  a    b    c    d    b    c    d    e
# 1  0.0  0.0  0.0  0.0  NaN  NaN  NaN  NaN
# 2  0.0  0.0  0.0  0.0  1.0  1.0  1.0  1.0
# 3  0.0  0.0  0.0  0.0  1.0  1.0  1.0  1.0
# 4  NaN  NaN  NaN  NaN  1.0  1.0  1.0  1.0
"""append 在行后再加上一行元素，或者在列中添加列元素"""
"""DataFrame上进行操作"""
# df1 = pd.DataFrame(np.ones((3, 4))*0, columns=['a', 'b', 'c', 'd'])
# df2 = pd.DataFrame(np.ones((3, 4))*1, columns=['a', 'b', 'c', 'd'])
# df3 = pd.DataFrame(np.ones((3, 4))*2, columns=['a', 'b', 'c', 'd'])
# res = df1.append([df2, df3], ignore_index=True)
# print(res)
# a    b    c    d
# 0  0.0  0.0  0.0  0.0
# 1  0.0  0.0  0.0  0.0
# 2  0.0  0.0  0.0  0.0
# 3  1.0  1.0  1.0  1.0
# 4  1.0  1.0  1.0  1.0
# 5  1.0  1.0  1.0  1.0
# 6  2.0  2.0  2.0  2.0
# 7  2.0  2.0  2.0  2.0
# 8  2.0  2.0  2.0  2.0
"""append在Series上进行操作"""
df1 = pd.DataFrame(np.ones((3, 4))*0, columns=['a', 'b', 'c', 'd'])
s1 = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
# a    1
# b    2
# c    3
# d    4
res = df1.append(s1, ignore_index=True)
print(df1)
print(s1)
print(res)

