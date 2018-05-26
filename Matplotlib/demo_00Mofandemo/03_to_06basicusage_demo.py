import matplotlib.pyplot as plt  # 大部分情况下不需要加载matplotlib所有的包，比如这里只需要加载pyplot这个包就足够了
import numpy as np
"""制造数据"""
"""Figure指的是图层的显示框每个数据可以在不同的数据框中显示"""
x = np.linspace(-3, 3, 50)  # 意为将-3~3之间评平分成50个点
y1 = 2 * x + 1
y2 = x**2  # 表示x的2次幂
"""这里很奇怪，x，y都是数据的集合"""
"""设置figure"""
# 由于是解释性语言，即figure下的所有数据都是属于最近的figure
# plt.figure()
# plt.plot(x, y1)  #设置x,y的数据源

# plt.figure(num=3, figsize=(8, 5))  # num设置的是figure序号，figsize设置的是长和宽度
plt.plot(x, y2)  # 默认颜色是蓝色，利用这个方法可以将两条图线装载到一个figure中
plt.plot(x, y1, color='red', linewidth=1.0, linestyle='--')  # 这里设置颜色为红色，设置线宽度为1.0，设置线为虚线的形式
"""设置坐标轴"""
plt.xlim((-1, 2))  # 设置x坐标轴的范围
plt.ylim((-2, 3))  # 设置y坐标轴的范围
"""设置x,y轴的lable即坐标轴上将要显现的文字"""
plt.xlabel("I am x")
plt.ylabel("I am y")
new_ticks = np.linspace(-1, 2, 5)
print(new_ticks)
plt.xticks(new_ticks)  # 改变x坐标轴的坐标，这里是设置为从-1~2，并且分成5个单位
# plt.yticks([-2, -1.8, -1, 1.22, 3], ['really bad', 'bad', 'normal', 'good', 'really good'])  # 普通字体
plt.yticks([-2, -1.8, -1, 1.22, 3], [r'$really\ bad$', r'$bad\ \alpha$', r'$normal$', '$good$', '$really\  good$'])  # 数学表示的美观字体
# plt.show()

# gca = 'get current axis'..axis轴线
"""改变坐标轴"""
ax = plt.gca()  # 取出图的轴线
ax.spines['right'].set_color('none')  # 图片的四个边框
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')  # 用下面的坐标轴代替x轴
ax.yaxis.set_ticks_position('left')  # 用左边的坐标轴代替y轴
"""对坐标轴进行位移"""
ax.spines['bottom'].set_position(('data', 1))
ax.spines['left'].set_position(('data', 0))
plt.show()