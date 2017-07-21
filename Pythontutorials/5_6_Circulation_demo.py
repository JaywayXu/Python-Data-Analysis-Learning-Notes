"""python循环教程"""
#  while循环语句教程
condition = 1
while condition < 10:  # while循环
    print(condition)
    condition = condition +1
# for循环语句教程
"""python 是一个十分注重语言形式的语言
    即在python循环中下一行开头会空出四格，
    在这四格中的语句都会认为是在循环中的语句"""
example_list = [1, 2, 3, 4, 5, 6, 7, 12, 543, 876, 12, 3, 2, 5]
for i in example_list:
    print(i)
#  利用range()函数进行for循环注意range的边界，其中左边是闭区间，右边是开区间
for i in range(1, 10, 2):  # 其中2表示步长
    print(i)
