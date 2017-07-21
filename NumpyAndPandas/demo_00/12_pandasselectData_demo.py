import pandas as pd
import numpy as np

dates = pd.date_range('20130101', periods=6)
# 表示生成日期属性的六个数值
df = pd.DataFrame(np.arange(24).reshape((6, 4)), index=dates, columns=['A', 'B', 'C', 'D'])
print(df)
#              A   B   C   D
# 2013-01-01   0   1   2   3
# 2013-01-02   4   5   6   7
# 2013-01-03   8   9  10  11
# 2013-01-04  12  13  14  15
# 2013-01-05  16  17  18  19
# 2013-01-06  20  21  22  23
# # 选择出A列的元素
# print(df.A, df['A'])
# #  或者利用切片的形式
# print(df[0:3], df['20130102':'20130104'])
# select by label:loc
print(df.loc['20130102'])
# A    4
# B    5
# C    6
# D    7
# Name: 2013-01-02 00:00:00, dtype: int32
# 对列的名称进行筛选
print(df.loc[:, ['A', 'B']])  # 打印出'A'和'B'列的所有行
# select by position :iloc 根据位置进行选择
print(df.iloc[3])  # 得到第三行的数据
# A    12
# B    13
# C    14
# D    15
# Name: 2013-01-04 00:00:00, dtype: int32
print(df.iloc[3, 1])  # 得到第三行第一位数据
# 13
print(df.iloc[3:5, 1:3])
print(df.iloc[[1, 3, 5], 1:3])  # 此种方式进行不连续的筛选
# mixed selection :ix 混合选择
# 可以将行作为数列进行筛选但是列作为数列名进行筛选
print(df.ix[:3, ['A', 'C']])

# Boolean indexing  条件筛选
print(df[df.A > 8])
