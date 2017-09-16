import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3, 3, 50)
y = 2*x + 1

plt.figure(num=1, figsize=(8, 5))
plt.plot(x, y)

ax = plt.gca()
# 隐藏右边和上面的边框线
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
# 将下面的边框作为横坐标轴,左边边框作为竖坐标轴
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data', 0))  # 可以去掉看看效果
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data', 0))  # 可以去掉看看效果

x0 = 1
y0 = 2*x0+1
plt.scatter(x0, y0, s=50, color='b')  # scatter函数表示的不是直线而是散点图的形式
#  设置大小为50，颜色为蓝色
'''利用plot函数画出直线'''
plt.plot([x0, x0], [y0, 0], 'k--', lw=2.5)  # 'k--'意味着黑色的虚线

# method 1
##################
plt.annotate(r'$2x+1=%s$' % y0, xy=(x0, y0), xycoords='data', xytext=(+30, -30), textcoords='offset points',
             fontsize=16, arrowprops=dict(arrowstyle='->', connectionstyle='arc3 ,rad=.2'))
"""xy=(x0,y0)表示从哪一点开始打印annotate,xycoords表示以这个点的值作为%s中的内容
arrowprops表示方向线,connectionstyle表示线条的弧度和角度"""
# method 2
#################
plt.text(-3.7, 3, r'$This\ is\ the\ some\ text.\ \mu\ \sigma_i\ \alpha_t$',
         fontdict={'size': 16, 'color': 'r'})
plt.show()