# View more python learning tutorial on my Youtube and Youku channel!!!

# Youtube video tutorial: https://www.youtube.com/channel/UCdyjiB5H8Pu7aDTNVXTTpcg
# Youku video tutorial: http://i.youku.com/pythontutorial

import time
print(time.localtime())

import time as t
print(t.localtime())

from time import localtime, time
print(localtime())
# 这种表示方式相当于
# import time
# print(time.localtime())
print(time())

from time import *
# 表示import所有的函数
print(localtime())
