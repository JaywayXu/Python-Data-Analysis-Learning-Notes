file = open('my file.txt', 'r')  # 读取文件，这是讲整个文件存进file中，将其读取出来还需要其他操作
# content = file.read()
"""注意：如果直接用read函数就将全部文件内容都存入到content中，以后用readline函数读不出数据了"""
#  也可以将文件读到一个List中，readline函数每次读取一行
#  readlines函数每次读取多个行，将其全部存到List中
# first_read_time = file.readline()
# second_read_time = file.readline()
# print(first_read_time, second_read_time)
# print(content)

content = file.readlines()
print(content)
# ['This is my first test.\n', 'This is next line.\n', 'This is last line.\n', 'This is appended file.']
