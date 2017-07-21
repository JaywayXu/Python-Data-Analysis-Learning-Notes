"""pandas数据可视化"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# plot data

# Series
data = pd.Series(np.random.randn(1000), index=np.arange(1000))
data = data.cumsum()  # 将1000个数字进行累加
data.plot()  # 第一张图片表示的是data的变化过程
# res=np.random.randn(1000,4)
# print(res)
# DataFrame
data = pd.DataFrame(np.random.randn(1000, 4), index=np.arange(1000), columns=list("ABCD"))
#  列表示属性A,B,C,D/np.random.randn(1000,4)表示生成1000行数据其中每行四个数据，并且设置列的抬头为ABCD
data = data.cumsum()
#  此时我们看看生成的data是怎样的一种数据格式
print(data)
data.plot()
plt.show()
# plot methods:
# 'bar', 'hist', 'box', 'kde', 'area', scatter', hexbin', 'pie'
#  这里表示的是图形的显示方式，bar类型指的是条形图，scatter指的是散点图
bx = data.plot.scatter(x='A', y='B', color='DarkBlue', label="Class 1")
#  并且将X设置为A的集合，Y设置为B的集合。所以Class 1表示的是A与B之间的关系
data.plot.scatter(x='A', y='C', color='LightGreen', label='Class 2', ax=bx)
#  ax表示的是图形显示的figure属性，这里设置两张图形在一张图片上显示
plt.show()
