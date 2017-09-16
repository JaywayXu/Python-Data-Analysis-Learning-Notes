"""散点图"""
import matplotlib.pyplot as plt
import numpy as np
#  产生数据
n = 1024
X = np.random.normal(0, 1, n)  # 随机产生方差是1的分布，产生n个数
Y = np.random.normal(0, 1, n)
T = np.arctan2(Y, X)  # for color value..生成颜色彩色颜色值

# plt.scatter(X, Y, s=75, c=T, alpha=0.5)
# """s=75数字大小是75，c是指颜色值,alpha设置透明度"""
# #  设置坐标范围
# plt.xlim((-1.5, 1.5))
# plt.ylim((-1.5, 1.5))
"""散点图的一般用法"""
plt.scatter(np.arange(5), np.arange(5))
plt.xticks(())  # 隐藏x坐标轴
plt.yticks(())  # 隐藏y坐标轴
plt.show()