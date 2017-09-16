"""柱状图"""
import  matplotlib.pyplot as plt
import numpy as np

n = 12
X = np.arange(n)  # 返回的是0~11的数值数组，默认的数据类型是float64
Y1 = (1-X/float(n))*np.random.uniform(0.5, 1.0, n)
"""numpy.random函数chisquare函数，
产生卡方分布的样本值
产生Gamma分布的样本值
产生在[0.5,1)中均匀分布的样本值"""
Y2 = (1-X/float(n))*np.random.uniform(0.5, 1.0, n)
"""生成条形柱状图"""
plt.bar(X, +Y1, facecolor='#9999ff', edgecolor='white')  # 表示正的，向上的，设置表面颜色和边框颜色
plt.bar(X, -Y2)  # 表示负的，向下的
"""设置X轴和Y轴的范围"""

for x, y in zip(X, Y1):  # zip函数即为将x,y1的值分别传到(x，y)组合当中
    # ha:horizotal alignment 对齐方式
    plt.text(x+0.4, y+0.05, '%.2f' % y, ha='center', va='bottom')  # 向下对齐
for x, y in zip(X, Y2):  # zip函数即为将x,y1的值分别传到(x，y)组合当中
    # ha:horizotal alignment 对齐方式
    plt.text(x+0.4, -y-0.05, '-%.2f' % y, ha='center', va='top')  # 向上对齐

plt.xlim(-5, n)
plt.xticks(())
plt.ylim(-1.25, 1.25)
plt.yticks(())

plt.show()