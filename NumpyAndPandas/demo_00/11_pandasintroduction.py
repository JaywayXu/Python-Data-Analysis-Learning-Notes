"""如果说numpy相当于列表的话，那么pandas就相当于是字典，可以为一组数组进行命名"""
import pandas as pd
import numpy as np
s = pd.Series([1, 3, 6, np.nan, 44, 1])
print(s)
# 0     1.0
# 1     3.0
# 2     6.0
# 3     NaN
# 4    44.0
# 5     1.0
# dtype: float64

dates = pd.date_range('20160101', periods=6)
print(dates)
# DatetimeIndex(['2016-01-01', '2016-01-02', '2016-01-03', '2016-01-04',
#                '2016-01-05', '2016-01-06'], dtype='datetime64[ns]', freq='D')

"""DataFrame相当于是一个二维的数组，但是可以自定义索引
此处行索引为dates，列索引是[a,b,c,d]"""
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=['a', 'b', 'c', 'd'])
print(df)
"""
np.random.randn表示的是标准正态曲线随机生成函数，利用正态分布的概率密度函数表达式可知
p(x)=1/[√(2π)σ]e^{-(x-u)²/(2σ²)} 
可知曲线关于x=u对称,且在对称轴上取得最大值为1/[√(2π)σ]
其中u为平均值,即数学期望,σ为标准差
因此,曲线顶点坐标为(u,1/[√(2π)σ])
"""
df1 = pd.DataFrame(np.arange(12).reshape(3, 4))
print(df1)
df2 = pd.DataFrame(
    {'A': 1.,
     'B': pd.Timestamp('20130102'),
     'C': pd.Series(1, index=list(range(4)), dtype='float32'),
     'D': np.array([3]*4, dtype='int32'),
     'E': pd.Categorical(["test", "train", "test", "train"]),
     'F': 'foo'
     })

print(df2)
print(df2.dtypes)
print(df2.index)  # Int64Index([0, 1, 2, 3], dtype='int64')
print(df2.columns)  # Index(['A', 'B', 'C', 'D', 'E', 'F'], dtype='object')
print(df2.values)
print(df2.describe())
"""
         A    C    D
count  4.0  4.0  4.0
mean   1.0  1.0  3.0
std    0.0  0.0  0.0
min    1.0  1.0  3.0
25%    1.0  1.0  3.0
50%    1.0  1.0  3.0
75%    1.0  1.0  3.0
max    1.0  1.0  3.0
"""
#  也可以对其进行转置操作
print(df2.T)
#  排序操作
print(df2.sort_index(axis=1, ascending=False))
# 这里表明是按照index进行排序,axis=1表示对列进行排序，ascending表示按照倒序的方式进行排序
"""也可以按照数组中列的value的值进行排序"""
# print(df2.sort_values(by='E'))
