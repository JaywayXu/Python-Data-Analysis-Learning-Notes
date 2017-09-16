"""3D plot教程"""
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()  # 新建一个figure
ax = Axes3D(fig)  # 新建3D坐标轴
#  X, Y value
X = np.arange(-4, 4, 0.25)
Y = np.arange(-4, 4, 0.25)
X, Y = np.meshgrid(X, Y)  # 将X，Y坐标填充到底面的坐标系
R = np.sqrt(X**2+Y**2)
# height value
Z = np.sin(R)  # 计算空间高度值为Z

ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=plt.get_cmap('rainbow'))
"""rstride表示线条的跨度，cstride表示颜色的跨度
前者值越小横向线条跨度越小，后者值越小纵向颜色线条跨度越密
cmap设定颜色，这里使用rainbow颜色~
"""
ax.contourf(X, Y, Z, zdir='z', offset=-2, cmap='rainbow')  # 填充等高线的图
# 设置等高线的高度范围，zdir='z'表示将图形投影到z轴，如果这里设置成为'X'表示将图形投影到X轴，
# offset表示将图形压到Z='-2'的位置
ax.set_zlim(-2, 2)
plt.show()
