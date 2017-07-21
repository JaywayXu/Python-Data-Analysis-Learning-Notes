"""merge是一种更加高级的合并方式，对于key也能做出操作"""
import pandas as pd

# merging two df by key/keys.(may be used in databases)
# simple example
left = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                     'A': ['A0', 'A1', 'A2', 'A3'],
                     'B': ['B0', 'B1', 'B2', 'B3']})
right = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                      'C': ['C0', 'C1', 'C2', 'C3'],
                      'D': ['D0', 'D1', 'D2', 'D3']})

print(left)
print(right)

"""基于一个key值将两者合并在一起"""
res = pd.merge(left, right, on='key')
print(res)
#     A   B key   C   D
# 0  A0  B0  K0  C0  D0
# 1  A1  B1  K1  C1  D1
# 2  A2  B2  K2  C2  D2
# 3  A3  B3  K3  C3  D3
"""基于两个key将数组合并到一起"""
# consider two keys
left = pd.DataFrame({'key1': ['K0', 'K0', 'K1', 'K2'],
                     'key2': ['K0', 'K1', 'K0', 'K1'],
                     'A': ['A0', 'A1', 'A2', 'A3'],
                     'B': ['B0', 'B1', 'B2', 'B3']})
right = pd.DataFrame({'key1': ['K0', 'K1', 'K1', 'K2'],
                      'key2': ['K0', 'K0', 'K0', 'K0'],
                      'C': ['C0', 'C1', 'C2', 'C3'],
                      'D': ['D0', 'D1', 'D2', 'D3']})
print(left)
print(right)
#     A   B key1 key2
# 0  A0  B0   K0   K0
# 1  A1  B1   K0   K1
# 2  A2  B2   K1   K0
# 3  A3  B3   K2   K1
#     C   D key1 key2
# 0  C0  D0   K0   K0
# 1  C1  D1   K1   K0
# 2  C2  D2   K1   K0
# 3  C3  D3   K2   K0
res = pd.merge(left, right, on=['key1', 'key2'], how='inner')  # default for how='inner'
print(res)
#     A   B key1 key2   C   D
# 0  A0  B0   K0   K0  C0  D0
# 1  A2  B2   K1   K0  C1  D1
# 2  A2  B2   K1   K0  C2  D2
"""内连接，只有所有key一模一样的时候才能连接成功~"""
res = pd.merge(left, right, on=['key1', 'key2'], how='outer')
print(res)
""""外连接，从笛卡尔积中查找"""
#      A    B key1 key2    C    D
# 0   A0   B0   K0   K0   C0   D0
# 1   A1   B1   K0   K1  NaN  NaN
# 2   A2   B2   K1   K0   C1   D1
# 3   A2   B2   K1   K0   C2   D2
# 4   A3   B3   K2   K1  NaN  NaN
# 5  NaN  NaN   K2   K0   C3   D3
"""当 how是inner时表示内连接，outer时表示外连接，left表示左连接，right表示右连接"""
res = pd.merge(left, right, on=['key1', 'key2'], how='left')
print(res)
"""左连接"""
#     A   B key1 key2    C    D
# 0  A0  B0   K0   K0   C0   D0
# 1  A1  B1   K0   K1  NaN  NaN
# 2  A2  B2   K1   K0   C1   D1
# 3  A2  B2   K1   K0   C2   D2
# 4  A3  B3   K2   K1  NaN  NaN
# indicator
df1 = pd.DataFrame({'col1': [0, 1], 'col_left': ['a', 'b']})
df2 = pd.DataFrame({'col1': [1, 2, 2], 'col_right': [2, 2, 2]})
print(df1)
print(df2)
res = pd.merge(df1, df2, on='col1', how='outer', indicator=True)
#  当indicator表示成为True的时候，显示连接方式
#  give the indicator a custom name，给予连接方式一个名称
res = pd.merge(df1, df2, on='col1', how='outer', indicator='indicator_column')
print(res)
"""left index和right index  index其实是最左边的一列
一般的都是考虑key属性，但是如果是利用index合并的话，考虑的是index
"""
# left_index and right_index
res = pd.merge(left, right, left_index=True, right_index=True, how='outer')
# res = pd.merge(left, right, left_index=True, right_index=True, how='inner')
print(res)
#     A   B key1_x key2_x   C   D key1_y key2_y
# 0  A0  B0     K0     K0  C0  D0     K0     K0
# 1  A1  B1     K0     K1  C1  D1     K1     K0
# 2  A2  B2     K1     K0  C2  D2     K1     K0
# 3  A3  B3     K2     K1  C3  D3     K2     K0
# handle overlapping
boys = pd.DataFrame({'k': ['K0', 'K1', 'K2'], 'age': [1, 2, 3]})
girls = pd.DataFrame({'k': ['K0', 'K0', 'K3'], 'age': [4, 5, 6]})
res = pd.merge(boys, girls, on='k', suffixes=['_boy', '_girl'], how='inner')
print(boys)
print(girls)
print(res)
# handle overlapping
boys = pd.DataFrame({'k': ['K0', 'K1', 'K2'], 'age': [1, 2, 3]})
girls = pd.DataFrame({'k': ['K0', 'K0', 'K3'], 'age': [4, 5, 6]})
res = pd.merge(boys, girls, on='k', how='inner')
print(res)