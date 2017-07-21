# x = 1
# y = 2
# z = 3
# if x < y < z:
#     print('x is less tha y ,and y is less than z')
# x is less tha y ,and y is less than z

# x = 1
# y = 2
# z = 0
# if x < y > z:
#     print('x is less than y, and y is less than z')
# x is less than y, and y is less than z

# x = 2
# y = 2
# z = 0
#
# if x != y:  # x == y
#     print('x is equal to y')

x = 4
y = 2
z = 3
if x > y:
    print('x is greater than y')
else:
    print('x is less or equal to y')

"""多重选择if elif else"""
x = 1
if x > 1:
    print('x > 1')
elif x < 1:
    print('x < 1')
else:
    print('x = 1')
x = -2
if x > 1:
    print('x>1')
elif x < 1:
    print('x<1')
elif x < -1:
    print('x<-1')
else:
    print('x=1')
print('finish running')
#  只是会从前面的开始匹配，遇到满足的条件就不会进行下面的判断了
# x is greater than y
# x = 1
# x<1
# finish running
