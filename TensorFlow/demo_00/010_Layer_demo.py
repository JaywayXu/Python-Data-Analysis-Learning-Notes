import tensorflow as tf


def add_layer(inputs, in_size, out_size, activation_function=None):  # def最后在import之后有两个空行
    # 要将Weights定义为随机变量
    weights = tf.Variable(tf.random_normal([in_size, out_size]))  # 这是一个有in_size行，out_size列的矩阵
    biases = tf.Variable(tf.zeros([1, out_size])+0.1)
    """biases一般定义为一个列表的形式,biases只有一行但是有out_size这么多列,但是tensorFlow中认为biases的值最好不要设置成为0
    所以此处改为加上0.1的形式"""
    wx_plus_b = tf.matmul(inputs, weights) + biases  #input和weights相乘的值加上biases以后的值就是Wx_plus_b
    """下面的代码极度不理解"""
    if activation_function is None:
        outputs = wx_plus_b
    else:
        outputs = activation_function(wx_plus_b)
    return outputs
