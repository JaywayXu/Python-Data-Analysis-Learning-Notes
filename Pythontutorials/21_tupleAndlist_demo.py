"""元组和列表"""
# 元组利用（）进行表示
# 列表用[]进行表示
a_tuple = (12, 3, 5, 15, 6)  # 元祖的表示也可以不加上()
another_tuple = 2, 4, 6, 7, 8
a_list = (12, 3, 67, 7, 82)
#  遍历
for content in a_list:
    print(content)
for content in a_tuple:
    print(content)
for index in range(len(a_list)):
    print('index=', index, 'number of index', a_list[index])