import tensorflow as tf
"""相当于是一种动态传入参数的形式"""
input1 = tf.placeholder(tf.float32)  # 大部分情况下处理的是float32形式的数据
"""placeholder第一个参数是数据的类型，第二个参数是数据的结构"""
input2 = tf.placeholder(tf.float32)

output = tf.multiply(input1, input2)  # 视频中是mul方法，但是这里报错了，所以这里应该是multiply方法

with tf.Session() as sess:
    print(sess.run(output, feed_dict={input1: [7.], input2: [2.]}))
    """placeholder和feed_dict这两个其实是绑定的~"""