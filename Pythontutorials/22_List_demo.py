"""关于List的操作"""
a = [1, 2, 3, 4, 2, 3, 1, 1]
a.append((0))  # 表示在列表的最后添加上0这个数据
# 指定位置添加上指定值
a.insert(0, 0)  # 表示在第一个位置添加上0的数据，默认索引从0开始
# remove函数将要remove掉的是value值，并且是列表中第一次出现的值
a.remove(2)
print(a)
# 对于python的索引如果是负数则是表示从后往前开始计数
print(a[-2])
# 对于数组索引
print(a[0: 3])
print(a[5:])
# 列表中第一次出现某值的索引值
print(a.index(4))
# 列表中出现某值的次数
"""对List进行排序"""
# a.sort()  # 对List进行从小大排序，会覆盖掉原有的a list
# print(a)
#  a.sort(reverse = True)表示对List从大到小进行排序，也会覆盖掉原有的aList
print(a.count(1))


