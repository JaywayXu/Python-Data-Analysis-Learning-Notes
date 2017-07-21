import tensorflow as tf

state = tf.Variable(0, name='counter')
"""tf和Py不同之处在于必须要是讲变量主动声明成为变量才能是变量，可以给定变量初始值，第一个参数就是初始值
也可以赋给name属性
"""
#  print(state.name)
one = tf.constant(1)

new_value = tf.add(state, one)  # 此处表示一个变量和一个常量相加
update = tf.assign(state, new_value)  # 此处表示讲new_value赋给state

# 如果程序中有变量的话一定要注意，init操作
init = tf.initialize_all_variables()  # 只有初始化所有的变量才会在程序中将这些变量激活
'''有变量的话一定要加上这一句话'''
with tf.Session()as sess:
    sess.run(init)   # 需要运行程序时一定要添加上这句话~表示程序从此处开始运行。
    for _ in range(3):  # 此函数表示循环，其中括号中的数值表示循环的次数。
        sess.run(update)
        # print(state)  # 这句话显示的是stage的shape和dtype，但是不是其数值
        print(sess.run(state))

