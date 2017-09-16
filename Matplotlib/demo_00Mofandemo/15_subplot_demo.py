import matplotlib.pyplot as plt
import numpy as np

"""如何在一个figure中添加多个图片"""
plt.figure()  # 创建一个figure
#  创建一个subplot并且给定一个位置坐标
plt.subplot(2, 1, 1)  #将这个figure分成两行两列并且在第一个位置创建这个subplot
plt.plot([0, 1], [0, 1])  # 表示的X轴坐标跨度是[0,1]Y轴坐标跨度是[0,1]

plt.subplot(2, 3, 4)
plt.plot([0, 1], [0, 2])  # 表示的X轴坐标跨度是[0,1]Y轴坐标跨度是[0,2]

plt.subplot(2, 3, 5)
plt.plot([0, 1], [0, 3])  # 表示的X轴坐标跨度是[0,1]Y轴坐标跨度是[0,3]

plt.subplot(2, 3, 6)
plt.plot([0, 1], [0, 4])  # 表示的X轴坐标跨度是[0,1]Y轴坐标跨度是[0,4]
"""表示被分成了两行，第二行有三列"""
plt.show()