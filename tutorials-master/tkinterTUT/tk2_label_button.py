# View more python learning tutorial on my Youtube and Youku channel!!!

# Youtube video tutorial: https://www.youtube.com/channel/UCdyjiB5H8Pu7aDTNVXTTpcg
# Youku video tutorial: http://i.youku.com/pythontutorial

import tkinter as tk

window = tk.Tk()
window.title('my window')  # 标题
window.geometry('500x400')  # 大小，长x宽，小写X

var = tk.StringVar()
l = tk.Label(window, textvariable=var, bg='green', font=('Arial', 12), width=15, height=2)  # 设定Label信息
# l = tk.Label(window, text='OMG! this is TK!', bg='green', font=('Arial', 12), width=15, height=2)
# 当静态显示时，使用text参数；而当动态显示时，使用textvariable参数。
# 当没有点击时，var中初始化为一个空值，而当按钮被点击，激活hit_me函数，修改on_hit
l.pack()  # 设定Label的安放位置
on_hit = False

def hit_me():
    global on_hit
    if on_hit == False:
        on_hit = True
        var.set('you hit me')
    else:  # 此种情况下，表示on_hit==True的情况
        on_hit = False
        var.set('')  # var的值设置为空值


b = tk.Button(window, text='hit me', width=15, height=2, command=hit_me)  # 按一下就会调用hit_me的函数
b.pack()

window.mainloop()  # 不断刷新主窗口
