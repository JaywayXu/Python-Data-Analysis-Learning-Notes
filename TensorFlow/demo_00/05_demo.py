import tensorflow as tf
import numpy as np

#create data
x_data = np.random.rand(100).astype(np.float32)  #np.random.rand(100)表示的是生成100个0~1之间的float32位的浮点数
y_data = x_data*0.1+0.3


###create tensorflow structure start###
#定义weight
Weights = tf.Variable(tf.random_uniform([1], -1.0, 1.0))  #设置tf的值为一个一维数组并且值从-1.0到1.0
biases = tf.Variable(tf.zeros([1]))
"""定义为0
Creates a tensor with all elements set to zero.
tf.zeros([3, 4], int32) ==> [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]"""

y = Weights*x_data+biases#将其设置为一维线性拟合
loss = tf.reduce_mean(tf.square(y-y_data))  #loss函数计算的是(y-y_data)^2的平均值
#优化程序，优化控制器使用梯度下降策略，优化器使用梯度下降算法
optimizer = tf.train.GradientDescentOptimizer(0.5)
"""tf.train.GradientDescentOptimizer.__init__(learning_rate, use_locking=False, name='GradientDescent')
梯度下降算法 设置0.5位leanningrate"""
train = optimizer.minimize(loss)
init = tf.global_variables_initializer()  #前面是搭建结构，下面是初始化神经网络的结构
###create tensorflow structure end###

sess = tf.Session()   #Session就像是一个指针指向我想要处理的位置~
sess.run(init)  #此时init激活 Very important
#训练神经网络,此处设定训练201步
for step in range(201):  #注意python是解释性的语言所以每一行的前面是不能加上空格的。
    sess . run(train)
    if step % 20 == 0:
        print(step, sess.run(Weights), sess.run(biases))

