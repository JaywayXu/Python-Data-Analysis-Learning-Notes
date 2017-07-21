import tensorflow as tf
# matrix意思就是矩阵
matrix1 = tf.constant([[3, 3]])  # 设置其为一个一行两列的矩阵,并且值是3,3
matrix2 = tf.constant([[2], [2]])  # 设置其为一个两行一列的矩阵，并且值是2,2

product = tf.matmul(matrix1, matrix2)  # matrix multiply 意思是矩阵乘法

# # method1
# sess = tf.Session()
# result = sess.run(product)
# print(result)
# sess.close()  # 其实close函数有和没有差别不是很大,但是有的话代码更加简洁一点


# method 2
with tf.Session() as sess:
    # 在with之内的语句，并用sess代表tf.Session函数，这样在最后不用写end函数而是直接回关闭session,这段注释前一定要空四个空格
    result2 = sess.run(product)
    print(result2)



