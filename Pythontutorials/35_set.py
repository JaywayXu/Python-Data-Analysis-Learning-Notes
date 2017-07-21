"""将所有重合的地方剔除掉只留下不重合的数据"""
char_list = ['a', 'b', 'c', 'c', 'd', 'd', 'd']

sentence = 'Welcome Back to This Tutorial'

print(set(char_list))  # {'d', 'a', 'c', 'b'}
print(set(sentence))
#  大小写区分，空格区分
#  {'r', 'T', 'm', 'l', 'o', 'h', 'e', 'a', ' ', 'i', 'W', 'B', 'k', 'u', 'c', 's', 't'}
"""下面这句话是错误的，不能在其中使用列表和列表的形式，只能使用单个的list或者是String"""
# print(set([char_list, sentence]))

unique_char = set(char_list)
unique_char.add('x')
print(unique_char)  # 但是只是加入进去了并不是按照原有的顺序
# unique_char.add(['y', 'z'])
# 只能单独加上数字，不能向其中添加一个List

# unique_char.clear()
#  set() 得到一个空的set

print(unique_char.remove('d'))
#  remove函数就算是执行之后返回值还是none,要是想要查看结果仍然需要使用print函数
#  但是如果想要删除的函数是在list中不存在的，就会报错,但是如果使用的是discard函数也不会报错，并且返回的是原有的数据
print(unique_char.discard('d'))
print(unique_char)

"""difference函数的使用"""
set1 = unique_char
set2 = {'a', 'e', 'i'}

print(set1.difference(set2))
#  找相同的地方
print(set1.intersection(set2))