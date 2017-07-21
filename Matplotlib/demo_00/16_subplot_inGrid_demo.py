"""分格显示"""
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

# method 1: subplot2grid
############################
# plt.figure()
# ax1 = plt.subplot2grid((3, 3), (0, 0), colspan=3, rowspan=1)
# ax1.plot([1, 2], [1, 2])  # 表示plot位置从横坐标范围1~2，纵坐标范围1~2。
# ax1.set_title('ax1_title')
# # 第一个参数表示这个grid中有三行三列
# # 第二个参数表示从（0,0）表示第一行第一列开始进行排列
# # 第三个参数表示横向跨度是3，纵向跨度是1
# ax2 = plt.subplot2grid((3, 3), (1, 0), colspan=2, rowspan=1)
# ax3 = plt.subplot2grid((3, 3), (1, 2), colspan=1, rowspan=2)
# ax4 = plt.subplot2grid((3, 3), (2, 0), colspan=1, rowspan=1)
# ax5 = plt.subplot2grid((3, 3), (2, 1), colspan=1, rowspan=1)
# method 2:gridspec
"""这个方法和numpy数组的分组和切片有关"""
############################
# plt.figure()
# # gs = gridspec.GridSpec(3, 3)  # 将整个figure分为3行3列
# # ax1 = plt.subplot(gs[0, :])  # 第一行整行
# # ax2 = plt.subplot(gs[1, :2])  # 第二行第0列和第一列，不包括右边界
# # ax3 = plt.subplot(gs[1:, 2])  # 第二行最后一列
# # ax4 = plt.subplot(gs[-1, 0])  # 在python数组索引中-1代表从后往前的值，相当于是2，-2相当于是1
# # ax5 = plt.subplot(gs[-1, -2])
#
# gs = gridspec.GridSpec(3, 3)
# ax1 = plt.subplot(gs[0, :])
# ax2 = plt.subplot(gs[1, :2])
# ax3 = plt.subplot(gs[1:, 2])
# ax4 = plt.subplot(gs[2, 0])
# ax5 = plt.subplot(gs[2, 1])

# method 3:easy to define structature
############################
f, ((ax11, ax12), (ax21, ax22)) = plt.subplots(2, 2, sharex=True, sharey=True)
ax11.scatter([1, 2], [1, 2])
# 代表两行两列,设置共享X轴，共享Y轴，并且返回一个定义有不同ax的figure

plt.tight_layout()
plt.show()