"""python 中的copy分为浅复制和深复制"""
import copy

#
# a = [1, 2, 3]
# b = a  # 这时候a和b指向的是硬盘中的同一片区域，用id显示的话即使id(a)==id(b)
# b[1] = 22  # 改变a中值b中值会同时被改变
# print(a)  # [1, 22, 3]
# print(id(a) == id(b))  # True
#
# # deep copy
# c = copy.deepcopy(a)
# print(id(a) == id(c))  # False
# c[1] = 2
# print(a)  # [1, 22, 3]  改变c中值，a中值不会改变
# a[1] = 111
# print(c)  # [1, 2, 3] 改变a中值，C中值不会改变

# shallow copy
a_list = [1, 2, 3]
a_tuple = (1, 2, 3)
a1_list = [1, 2, (1, 2, 3), [1, 2, 3]]
a1_tuple = (1, 2, (1, 2, 3), [1, 2, 3])

a_shallow_list = copy.copy(a_list)
a_shallow_tuple = copy.copy(a_tuple)
a1_shallow_list = copy.copy(a1_list)
a1_shallow_tuple = copy.copy(a1_tuple)

a_deep_list = copy.deepcopy(a_list)
a_deep_tuple = copy.deepcopy(a_tuple)
a1_deep_list = copy.deepcopy(a1_list)
a1_deep_tuple = copy.deepcopy(a1_tuple)

# 比较基本可变对象，深复制和浅复制区别
# print("id of a_list", id(a_list), "id of a_shallow_list", id(a_shallow_list), "a_deep_list", id(a_deep_list))
# id of a_list 2249250705672 id of a_shallow_list 2249201900552 a_deep_list 2249201900424
# 实验表明均指向一个新的地址
# 其中不可变对象地址
# print("id of a_list[0]", id(a_list[0]), "id of a_shallow_list[0]", id(a_shallow_list[0]), "a_deep_list[0]", id(a_deep_list[0]))
# id of a_list[0] 1887096560 id of a_shallow_list[0] 1887096560 a_deep_list[0] 1887096560
# 基本可变对象中不可变对象的地址不会改变

# 比较基本不可变对象，深复制和浅复制区别
# print("id of a_tuple", id(a_tuple), "a_shallow_tuple", id(a_shallow_tuple), "a_deep_tuple", id(a_deep_tuple))
# print("id of a_tuple[0]", id(a_tuple[0]), "a_shallow_tuple[0]", id(a_shallow_tuple[0]), "a_deep_tuple[0]",
#       id(a_deep_tuple[0]))
# id of a_tuple 2344837083280 a_shallow_tuple 2344837083280 a_deep_tuple 2344837083280
# id of a_tuple[0] 1885130480 a_shallow_tuple[0] 1885130480 a_deep_tuple[0] 1885130480

# 复合嵌套不可变元素的深复制和浅复制区别
# print("id of a1_tuple", id(a1_tuple), "a1_shallow_tuple", id(a1_shallow_tuple), "a1_deep_tuple", id(a1_deep_tuple))
# print("id of a1_tuple[3]", id(a1_tuple[3]), "a1_shallow_tuple[3]", id(a1_shallow_tuple[3]), "a1_deep_tuple[3]",
#       id(a1_deep_tuple[3]))

# id of a1_tuple 2498218636296 a1_shallow_tuple 2498218636296 a1_deep_tuple 2498218638776
# id of a1_tuple[3] 2498267415048 a1_shallow_tuple[3] 2498267415048 a1_deep_tuple[3] 2498218716040

# 复合嵌套可变元素的深复制和浅复制区别
print("id of a1_list", id(a1_list), "id of a1_shallow_list", id(a1_shallow_list), "a1_deep_list", id(a1_deep_list))
print("id of a1_list[3]", id(a1_list[3]), "id of a1_shallow_list[3]", id(a1_shallow_list[3]), "a1_deep_list[3]",
      id(a1_deep_list[3]))
# id of a1_list 1453555407752 id of a1_shallow_list 1453555447432 a1_deep_list 1453555477384
# id of a1_list[3] 1453604277640 id of a1_shallow_list[3] 1453604277640 a1_deep_list[3] 1453555448968