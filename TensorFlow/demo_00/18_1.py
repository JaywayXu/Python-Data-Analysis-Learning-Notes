"""
Please note, this code is only for python 3+. If you are using python 2+, please modify the code accordingly.
"""
from __future__ import print_function
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

# number 1 to 10 data
mnist = input_data.read_data_sets('MNIST_data', one_hot=True)


def compute_accuracy(v_xs, v_ys):
    global prediction
    y_pre = sess.run(prediction, feed_dict={xs: v_xs, keep_prob: 1})
    correct_prediction = tf.equal(tf.argmax(y_pre, 1), tf.argmax(v_ys, 1))
    accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
    result = sess.run(accuracy, feed_dict={xs: v_xs, ys: v_ys, keep_prob: 1})
    return result


def weight_variable(shape):
    initial = tf.truncated_normal(shape, stddev=0.1)
    # 截取正太分布随机输出，正态分布标准差1
    return tf.Variable(initial)


def bias_variable(shape):
    initial = tf.constant(0.1, shape=shape)
    # 设置其初始bias为0.1
    return tf.Variable(initial)


def conv2d(x, W):
    # x表示输入的值，W表示weight,strides表示步[1,.,.,1]注意第一个和最后一个参数一定要保证值为1，
    # 然后第二个参数表示在x轴上的步长，第三个参数表示在y轴上的步长
    # stride [1, x_movement, y_movement, 1]
    # Must have strides[0] = strides[3] = 1
    # padding表示为valid则是指只选取有效的部分，得到的卷积层比原来的小
    # padding表示为same则是指选取的部分不够的地方填充为0，得到的卷积层和原来的大小一样
    return tf.nn.conv2d(x, W, strides=[1, 1, 1, 1], padding='SAME')


def max_pool_2x2(x):
    # stride [1, x_movement, y_movement, 1]
    # ksize表示维度上窗口大小对应值，strides表示窗口移动的步长，也就是说我们这里设置窗口大小为[2,2]，
    # 步长也设置为右移2和下移2，这样窗口在移动过程中不会重复捕捉。
    return tf.nn.max_pool(x, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME')


# define placeholder for inputs to network
xs = tf.placeholder(tf.float32, [None, 784])  # 28x28
ys = tf.placeholder(tf.float32, [None, 10])
keep_prob = tf.placeholder(tf.float32)

## conv1 layer ##

## conv2 layer ##

## func1 layer ##

## func2 layer ##


# the error between prediction and real data
cross_entropy = tf.reduce_mean(-tf.reduce_sum(ys*tf.log(prediction),
                                              reduction_indices=[1]))  # loss
train_step = tf.train.AdamOptimizer(1e-4).minimize(cross_entropy)

sess = tf.Session()
# important step
# tf.initialize_all_variables() no long valid from
# 2017-03-02 if using tensorflow >= 0.12
if int((tf.__version__).split('.')[1]) < 12 and int((tf.__version__).split('.')[0]) < 1:
    init = tf.initialize_all_variables()
else:
    init = tf.global_variables_initializer()
sess.run(init)

for i in range(1000):
    batch_xs, batch_ys = mnist.train.next_batch(100)
    sess.run(train_step, feed_dict={xs: batch_xs, ys: batch_ys, keep_prob: 0.5})
    if i%50 == 0:
        print(compute_accuracy(
            mnist.test.images, mnist.test.labels))
