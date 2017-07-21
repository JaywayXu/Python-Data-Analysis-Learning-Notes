"""利用pandas导入和导出数据"""
import pandas as pd
data = pd.read_csv('student.csv')
print(data)
data.to_pickle('student.pickle')
