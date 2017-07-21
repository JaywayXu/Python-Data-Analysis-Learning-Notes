import tensorflow as tf
import numpy as np


def add_layer(inputs, in_size, out_size, activation_function=None):  # def最后在import之后有两个空行
    # 要将Weights定义为随机变量
    weights = tf.Variable(tf.random_normal([in_size, out_size]))  # 这是一个有in_size行，out_size列的矩阵
    # tf.random_normal(shape, mean=0.0, stddev=1.0, dtype=tf.float32, seed=None, name=None)标准差函数
    # Create a tensor of shape [2, 3] consisting of random normal values, with mean
    #  -1 and standard deviation 4.
    # norm = tf.random_normal([2, 3], mean=-1, stddev=4)
    # 参见云笔记中关于np.random.normal()的介绍
    biases = tf.Variable(tf.zeros([1, out_size]) + 0.1)
    """biases一般定义为一个列表的形式,biases只有一行但是有out_size这么多列,但是tensorFlow中认为biases的值最好不要设置成为0
    所以此处改为加上0.1的形式"""
    wx_plus_b = tf.matmul(inputs, weights) + biases  # input和weights相乘的值加上biases以后的值就是Wx_plus_b
    """下面的代码极度不理解"""
    if activation_function is None:
        outputs = wx_plus_b
    else:
        outputs = activation_function(wx_plus_b)
    return outputs


"""这里的意思是从-1到1区间并且有300个单位
在00_ceshi_demo中可以看到x_data,noise,y_data都是300*1的二维数组"""
x_data = np.linspace(-1, 1, 300)[:, np.newaxis]  # 参见云笔记中关于np.newaxis的介绍加上列的一维
#  自己设置原始数据，采用噪点的方式
noise = np.random.normal(0, 0.05, x_data.shape)
y_data = np.square(x_data) - 0.5 + noise
# print(x_data)
# print(noise)
# print(y_data)
xs = tf.placeholder(tf.float32, [None, 1])
"""tf.placeholder(dtype, shape=None, name=None),设置的shape是不控制行数的二位数组，其中列数为1，也就是说无论设置多少个例子都可以"""
ys = tf.placeholder(tf.float32, [None, 1])
"""因为我们只需要预测一个属性，所以我们的输入和输出都只有一个神经元，设置隐藏层有10个神经元"""
#  定义隐藏层
l1 = add_layer(xs, 1, 10, activation_function=tf.nn.relu)  # 作者更加倾向于用这个激励方程
"""输入是x_data，输入一个参数，隐藏层有10个神经元所以有10个输出，"""
#  定义输出层，输出是l1所以把其作为输出层的输入，
prediction = add_layer(l1, 10, 1, activation_function=None)
"""数据来源是l1，有10个输入数据，有一个输出数据"""

"""此时计算预测值和真实值的差别"""
loss = tf.reduce_mean(tf.reduce_sum(tf.square(ys - prediction), reduction_indices=[1]))
#  对于每一个例子计算tf.square(ys-prediction),并且使用tf.reduce_sum函数将每一例子算出的差值进行求和
#  关于tf.reduce_sum函数见有道笔记归纳函数
"""定义Optimizer Function优化函数
0.1,learningrate
minimize(loss)用途是减少误差，减少loss的值
"""
train_step = tf.train.GradientDescentOptimizer(0.1).minimize(loss)
"""对所有变量进行初始化"""
init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)
"""上面的代码都没有进行运算，直到sess.run指定程序开始运行处才会开始运算"""

#  学习1000次
for i in range(1000):
    sess.run(train_step, feed_dict={xs: x_data, ys: y_data})
    if i % 50 == 0:
        print(sess.run(loss, feed_dict={xs: x_data, ys: y_data}))
