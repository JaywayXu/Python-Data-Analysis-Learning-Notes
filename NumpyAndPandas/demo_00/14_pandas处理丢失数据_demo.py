"""处理没有数据的数据模块"""
import pandas as pd
import numpy as np

dates = pd.date_range('20130101', periods=6)
df = pd.DataFrame(np.arange(24).reshape((6, 4)), index=dates, columns=['A', 'B', 'C', 'D'])
df.iloc[0, 1] = np.nan
df.iloc[1, 2] = np.nan
#  如果一行中有Nan的无效数据就将其丢弃掉
# print(df.dropna(axis=0, how='any'))  # 如果这一行中有任何一个Nan就将其丢弃掉
#  默认情况就是how='any'
print(df.dropna(axis=0, how='all'))  # 只有在这一行中所有的都是Nan时就将其扔掉，如果axis是1则此时是列
#  此种方法是将NaN值转换成0
# print(df.fillna(value=0))
#  返回是否有Nan的值，返回时True,False
print(df.isnull())
#     A      B      C      D
# 2013-01-01  False   True  False  False
# 2013-01-02  False  False   True  False
# 2013-01-03  False  False  False  False
# 2013-01-04  False  False  False  False
# 2013-01-05  False  False  False  False
# 2013-01-06  False  False  False  False
"""至少有一个是丢失了的数据，也就是其中包含有Nan的值"""
print(np.any(df.isnull()) == True)
