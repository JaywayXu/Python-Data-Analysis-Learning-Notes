import tensorflow as tf

BATCH_SIZE = 400
NUM_THREADS = 2
MAX_NUM = 5


def read_data(file_queue):
    reader = tf.TextLineReader(skip_header_lines=1)
    key, value = reader.read(file_queue)
    defaults = [[0], [0.], [0.]]
    NUM, C, Tensile = tf.decode_csv(value, defaults)
    vertor_example = tf.stack([C])
    vertor_label = tf.stack([Tensile])
    vertor_num = tf.stack([NUM])

    return vertor_example, vertor_label, vertor_num


def create_pipeline(filename, batch_size, num_threads):
    file_queue = tf.train.string_input_producer([filename])  # 设置文件名队列
    example, label, no = read_data(file_queue)  # 读取数据和标签

    example_batch, label_batch, no_batch = tf.train.batch(
        [example, label, no], batch_size=batch_size, num_threads=num_threads, capacity=MAX_NUM)

    return example_batch, label_batch, no_batch


x_train_batch, y_train_batch, no_train_batch = create_pipeline('test_tf_train_batch.csv', batch_size=BATCH_SIZE,
                                                               num_threads=NUM_THREADS)

init_op = tf.global_variables_initializer()
local_init_op = tf.local_variables_initializer()
with tf.Session() as sess:
    sess.run(local_init_op)
    sess.run(init_op)
    coord = tf.train.Coordinator()
    threads = tf.train.start_queue_runners(coord=coord)
    # 同时运行的方式
    example, label, num = sess.run([x_train_batch, y_train_batch, no_train_batch])
    print('The first mode to load data')
    print('example', example)
    print('label', label)
    print('num', num)

    # 分别运行的方式
    # example = sess.run(x_train_batch)
    # label = sess.run(y_train_batch)
    # num = sess.run(no_train_batch)
    # print('The second mode to load data')
    # print('example', example)
    # print('label', label)
    # print('num', num)

    coord.request_stop()
    coord.join(threads)
