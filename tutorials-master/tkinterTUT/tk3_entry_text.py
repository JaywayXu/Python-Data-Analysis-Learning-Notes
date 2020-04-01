# View more python learning tutorial on my Youtube and Youku channel!!!

# Youtube video tutorial: https://www.youtube.com/channel/UCdyjiB5H8Pu7aDTNVXTTpcg
# Youku video tutorial: http://i.youku.com/pythontutorial

import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('500x500')
e = tk.Entry(window, show="*")
# 表示所输入的文字会使用"*"号加以掩盖
# e = tk.Entry(window, show=None)
# 可以通过设置为None取消掩盖模式

e.pack()

def insert_point():
    var = e.get()  # 获取输入的值
    t.insert('insert', var)  # 从指针位置处输入


def insert_end():
    var = e.get()
    t.insert('end', var)  # 从末尾处输入
    # t.insert(2.2, var)  # 从第三行第三列输入


b1 = tk.Button(window, text='insert point', width=15,
               height=2, command=insert_point)
b1.pack()
b2 = tk.Button(window, text='insert end',
               command=insert_end)
b2.pack()
t = tk.Text(window, height=2)  # 表示两个字符高
t.pack()

window.mainloop()
