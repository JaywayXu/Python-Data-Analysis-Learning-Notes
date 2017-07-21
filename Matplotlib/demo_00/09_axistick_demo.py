import matplotlib.pyplot as plt
import numpy as np
"""用于为了避免"""
x = np.linspace(-3, 3, 50)
y = 0.1 * x

plt.figure()
plt.plot(x, y, linewidth=10)
plt.ylim(-2, 2)  # 设置y从-2到2
ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
# 将下面的边框作为横坐标轴,左边边框作为竖坐标轴
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data', 0))  # 可以去掉看看效果
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data', 0))  # 可以去掉看看效果
#  获取图像中所有的label，并且设置图像中的label
for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_fontsize(12)  # 设置字体大小为12
    label.set_bbox(dict(facecolor='white', edgecolor='None', alpha=0.7))
    # 设置label颜色是白色，edgecolor边框颜色无，透明度为0.7


plt.show()