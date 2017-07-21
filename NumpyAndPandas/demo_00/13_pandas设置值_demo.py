import pandas as pd
import numpy as np

dates = pd.date_range('20130101', periods=6)
df = pd.DataFrame(np.arange(24).reshape((6, 4)), index=dates, columns=['A', 'B', 'C', 'D'])

print(df)
df.iloc[2, 2] = 1111
df.loc['20130101', 'B'] = 2222
# df[df.A > 4] = 0  # 但是这样会让A>4的整行全部变为0
# print(df)
df.A[df.A > 4] = 0  # 如果只是想使df.A这一列中的值大于4的变成0，这是df.A~
print(df)
"""添加列"""
df['F'] = np.nan  # 加上一个全部为nan的列
df['E'] = pd.Series([1, 2, 3, 4, 5, 6], index=pd.date_range('20130101', periods=6))  # 加上一个指定数值的列
print(df)