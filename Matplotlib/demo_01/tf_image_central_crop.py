import tensorflow as tf
import matplotlib.pyplot as plt

image_raw_data_jpg = tf.gfile.FastGFile('./test_images/test_2.jpg', 'rb').read()

with tf.Session() as sess:
    img_data_jpg = tf.image.decode_jpeg(image_raw_data_jpg)
    img_data_jpg = tf.image.convert_image_dtype(img_data_jpg, dtype=tf.float32)
    crop = tf.image.central_crop(img_data_jpg, 1)  # 原图
    pad = tf.image.central_crop(img_data_jpg, 0.5)  # 原图的一半

    plt.figure(1)
    plt.imshow(crop.eval())
    plt.figure(2)
    plt.imshow(pad.eval())
    plt.show()
