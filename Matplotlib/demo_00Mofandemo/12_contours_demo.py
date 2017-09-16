"""等高线"""
import matplotlib.pyplot as plt
import numpy as np
#  生成高度的函数


def f(x, y):
    return(1 - x / 2 + x**5 + y**3)*np.exp(-x**2 -y**2)

n = 256
x = np.linspace(-3, 3, n)  #linespace函数将范围均分,左右都是闭区间
y = np.linspace(-3, 3, n)
X, Y = np.meshgrid(x, y)
# use plt.contourf to filling contours
# X,Y and value for (x,y)
"""填充颜色contourf函数"""
plt.contourf(X, Y, f(X, Y), 8, alpha=0.75, cmap=plt.cm.hot)
"""plt.cm.hot是一个hot cmp图，也可以设置为cm.cool"""
#use plt,contour to add contour lines
"""画等高线"""
C = plt.contour(X, Y, f(X, Y), 8, colors='black', linewidth=.5)
"""plt.contour函数是用于画等高线的线
数字8代表着分成多少部分，0代表两部分，8代表10部分"""
plt.clabel(C, inline=True, fontsize=10)
#  表示画在等高线上的数字，C表示等高线，inline表示画在等高线中，否则等高线会穿过数字
# adding label
plt.xticks(())
plt.yticks(())
plt.show()