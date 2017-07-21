"""python 中的copy分为浅复制和深复制"""
import copy
"""默认其实就是深复制"""
a = [1,2,3]
b = a  # 这时候a和b指向的是硬盘中的同一片区域，用id显示的话即使id(a)==id(b)
b[1] = 22  # 改变a中值b中值会同时被改变
print(a)  # [1, 22, 3]
print(id(a) == id(b))  # True

# deep copy
c = copy.deepcopy(a)
print(id(a) == id(c))  # False
c[1] = 2
print(a)  # [1, 22, 3]  改变c中值，a中值不会改变
a[1] = 111
print(c)  # [1, 2, 3] 改变a中值，C中值不会改变

# shallow copy
a = [1,2,[3,4]]
d = copy.copy(a)
print(id(a) == id(d))  # False
print(id(a[2]) == id(d[2]))  # True
