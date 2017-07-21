a = [1, 2, 3]
b = [4, 5, 6]

# for zip
print(list(zip(a, b)))  # [(1, 4), (2, 5), (3, 6)]
print(list(zip(a, a, b)))  # [(1, 1, 4), (2, 2, 5), (3, 3, 6)]
for i, j in zip(a, b):
    print(i/2, j*2)


# for lambda  主要用途是定义比较简单的方程
def f1(x, y):
    return x + y


f2 = lambda x, y: x + y
print(f1(1, 2))
print(f2(1, 2))

# for map
# map 是将值和函数封装起来进行操作，并且和zip,lambda,一样只有使用过list函数之后才能输出
print(list(map(f1, [1], [2])))  # x=1, y=2
print(list(map(f2, [2, 3], [4, 5])))  # [6, 8] 第一个表示将2+4 第二个表示3+5
