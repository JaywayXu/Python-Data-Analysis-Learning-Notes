# View more python learning tutorial on my Youtube and Youku channel!!!

# Youtube video tutorial: https://www.youtube.com/channel/UCdyjiB5H8Pu7aDTNVXTTpcg
# Youku video tutorial: http://i.youku.com/pythontutorial

import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('500x500')

var1 = tk.StringVar()
l = tk.Label(window, bg='yellow', width=4, textvariable=var1)
l.pack()


def print_selection():
    value = lb.get(lb.curselection())
    var1.set(value)


b1 = tk.Button(window, text='print selection', width=15,
               height=2, command=print_selection)
b1.pack()

# 设置默认列表元素值
var2 = tk.StringVar()
var2.set((11, 22, 33, 44))  # listbox中的值，此处传入值为列表或者元组均可
lb = tk.Listbox(window, listvariable=var2)

# 插入列表中元素
list_items = [1, 2, 3, 4]
for item in list_items:
    # 从尾部逐个插入list_items中元素
    lb.insert('end', item)

# 使用索引逐个插入元素
lb.insert(1, 'first')
lb.insert(2, 'second')
lb.delete(2)
lb.pack()

window.mainloop()
