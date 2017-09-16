import matplotlib.pyplot as plt
import numpy as np

# image data
a = np.array([0.313660827978, 0.365348418405, 0.423733120134,
              0.365348418405, 0.439599930621, 0.525083754405,
              0.423733120134, 0.525083754405, 0.651536351379]).reshape(3, 3)

plt.imshow(a, interpolation='nearest', cmap='bone', origin='lower')
# origin指定的是颜色的对应的顺序，interpolation控制的是滤镜，
#plt.colorbar(shrink=0.9)  #在图形旁边显示颜色过渡信息,,shrink函数表示缩放倍数。
plt.colorbar()
"""
for the value of "interpolation", check this:
http://matplotlib.org/examples/images_contours_and_fields/interpolation_methods.html
for the value of "origin"= ['upper', 'lower'], check this:
http://matplotlib.org/examples/pylab_examples/image_origin.html
"""
plt.xticks(())
plt.yticks(())
plt.show()