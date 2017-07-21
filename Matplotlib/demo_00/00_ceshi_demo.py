"""测试linspace,meshgrid函数"""
import matplotlib.pyplot as plt
import numpy as np
nx, ny = (3, 2)
x = np.linspace(0, 1, nx)
y = np.linspace(0, 1, ny)
xv, yv = np.meshgrid(x, y)
# print(x)
# print(y)
# print(xv)
# print(yv)