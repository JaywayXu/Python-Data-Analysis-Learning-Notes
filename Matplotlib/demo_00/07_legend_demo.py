"""图例-在图中区别不同曲线的名称"""
import matplotlib.pyplot as plt  # 大部分情况下不需要加载matplotlib所有的包，比如这里只需要加载pyplot这个包就足够了
import numpy as np
"""制造数据"""
"""Figure指的是图层的显示框每个数据可以在不同的数据框中显示"""
x = np.linspace(-3, 3, 50)  # 意为将-1~1之间评平分成50个点
y1 = 2 * x + 1
y2 = x**2  # 表示x的2次幂

plt.figure(num=3, figsize=(8, 5))  # num设置的是figure序号，figsize设置的是长和宽度
plt.xlim((-1, 2))  # 设置x坐标轴的范围
plt.ylim((-2, 3))  # 设置y坐标轴的范围
"""设置x,y轴的lable即坐标轴上将要显现的文字"""
plt.xlabel("I am x")
plt.ylabel("I am y")
new_ticks = np.linspace(-1, 2, 5)
plt.xticks(new_ticks)
plt.yticks([-2, -1.8, -1, 1.22, 3],
           [r'$really\ bad$', r'$bad\ \alpha$', r'$normal$', '$good$', '$really\  good$'])  # 数学表示的美观字体

"""线的lable属性标记线的名字"""
l1 = plt.plot(x, y2, label='up')  # 默认颜色是蓝色，利用这个方法可以将两条图线装载到一个figure中
l2 = plt.plot(x, y1, color='red', linewidth=1.0, linestyle='--', label='down')  # 这里设置颜色为红色，设置线宽度为1
# plt.legend(handles=[l1, l2, ], labels=['straight', 'curve'], loc='best')
plt.legend()
# 设置图例,loc='best'意味着自动找一个好的地方生成图例，loc中可以添加许多种形式
# handle可以添加进入线的例子
# 如果这里设置了lables的话，那么原先单独设定的lables就会被覆盖掉
plt.show()