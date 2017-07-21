"""讲解关于类的定义和使用"""


class Calculator:
    name = 'Good calculator'  # 固有属性，但是如果在init函数中被赋值的话则固有属性会被覆盖掉
    price = 18
    # 定义类的属性

    def __init__(self, name, price, height, width, weight):
        self.name = name
        self.price = price
        self.h = height
        self.wi = width
        self.we = weight

    def add(self, x, y):
        # 定义类的方法,其中self是一个保留参数
        print(x+y)

    def minus(self, x, y):
        print(x-y)

    def times(self, x, y):
        print(x*y)

    def divide(self, x, y):
        print(x/y)
"""init"""
