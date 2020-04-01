# View more python learning tutorial on my Youtube and Youku channel!!!

# Youtube video tutorial: https://www.youtube.com/channel/UCdyjiB5H8Pu7aDTNVXTTpcg
# Youku video tutorial: http://i.youku.com/pythontutorial

import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('500x500')

l = tk.Label(window, bg='yellow', width=20, text='empty')
l.pack()


def print_selection(v):
    l.config(text='you have selected ' + v)

# 注意：
# length表示的不是字符的宽度而是像素的宽度
# showvalue 指横轴上方是否显示当前数字，选择0是不显示，选择1是显示
# tickinterval 标签的单位长度 5-7-9-11
# resolution 表示精度，0.01表示保留两位小数
# command 表示调用的函数，默认传入值为scale标签标注的值

s = tk.Scale(window, label='try me', from_=5, to=11, orient=tk.HORIZONTAL,
             length=200, showvalue=0, tickinterval=2, resolution=0.01, command=print_selection)
s.pack()

window.mainloop()
