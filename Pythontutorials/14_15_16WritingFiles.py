"""文件读写_1"""
# 转行符\n
text = 'This is my first test.\nThis is next line.\nThis is last line.'
print(text)
# This is my first test.
# This is next line.
# This is last line.
append_text = '\nThis is appended file.'
my_file = open('my file.txt', 'w')  # w表示只写，r表示只读，如果没有这个文件的话会创建一个这样的文件
"""注意：打开文件后一定要将其关闭"""
my_file.write(text)
my_file.close()
my_file = open('my file.txt', 'a')  # a表示append
my_file.write(append_text)
my_file.close()