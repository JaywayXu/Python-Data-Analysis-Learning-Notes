import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

fig, ax = plt.subplots()
x = np.arange(0, 2*np.pi, 0.01)
line, = ax.plot(x, np.sin(x))

def animate(i):
    line.set_ydata(np.sin(x+i/10.0))
    return line,

def init():
    line.set_ydata(np.sin(x))
    return line,


ani = animation.FuncAnimation(fig=fig, func=animate, frames=100, init_func=init,
                              interval=20, blit=False)
"""frames设定帧数,100个update，init_func设定初始函数图像, interval设置更新间隔此处设置为20毫秒
如果是变化了的就更新设置为True,如果是全部更新的话就设置为False
"""
plt.show()