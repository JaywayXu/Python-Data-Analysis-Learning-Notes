"""用于将上次的数据加以保存方便下次进行计算和操作"""
import pickle

a_dict = {'da': 111, 2: [23,1,4], '23': {1:2,'d':'sad'}}

# pickle a variable to a file
file = open('pickle_example.pickle', 'wb')  # b表示二进制形式，wb表示写入二进制
pickle.dump(a_dict, file)
file.close()

# reload a file to a variable
with open('pickle_example.pickle', 'rb') as file:  # with语句就是当执行完毕后自动将其关闭
    a_dict1 = pickle.load(file)

print(a_dict1)







