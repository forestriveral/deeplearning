
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# s = pd.Series([1, 3, 6, np.nan, 44, 1])
# print(s)
# dates = pd.date_range('20180101', periods=6)
# print(dates)
# df = pd.DataFrame(np.random.rand(6, 4), index=dates, columns=['a', 'b', 'c', 'd'])
# print(df)
# df1 = pd.DataFrame(np.arange(12).reshape(3, 4))
# print(df1)
# df2 = pd.DataFrame()
# d = {'col1': [1, 2], 'col2': [3, 4]}
# df = pd.DataFrame(data=d)
# print(df)
# student = np.dtype([('name', 'S20'),  ('age',  'i1'),  ('marks',  'f4')])
# a = np.array([('abc',  21,  50), ('xyz',  18,  75)], dtype=student)
# print(a)

# dates = pd.date_range('20180101', periods=6)
# df = pd.DataFrame(np.arange(24).reshape((6, 4)), index=dates, columns=['A', 'B', 'C', 'D'])
# print(df['A'], df.A)
# print(df[0:3])
# print(df['20180102':'20180104'])

# select by label:loc
# print(df.loc['20180102'])
# print(df.loc[:, ['A', 'B']])
# print(df.loc['20180102', ['A', 'B']])

# select by position:iloc
# print(df.iloc[3, 1])
# print(df.iloc[3:5, 2:5])
# print(df.iloc[[1, 3, 5], 2:5])

# mixed selection:ix
# print(df.ix[:3, ['A', 'C']])

# boolean indexing
# print(df[df.A > 8])

# assign values
# df.iloc[2, 2] = 1111
# df.loc['20180103', 'B'] = 2222
# df.A[df.A > 4] = 0
# df['F'] = np.nan
# df['E'] = pd.Series([1, 2, 3, 4, 5, 6], index=pd.date_range('20180110', periods=6))
# print(df)

# df.iloc[0, 1] = np.nan
# df.iloc[1, 2] = np.nan
# print(df.dropna(axis=0, how='any'))  # how = {"any", "all"}
# print(df.fillna(value=0))
# print(np.any(df.isnull()) == True)

# data = pd.read_csv('student.csv')
# print(data)
# data.to_pickle()

# concatenating
# df1 = pd.DataFrame(np.ones((3, 4))*0, columns=['a', 'b', 'c', 'd'])
# df2 = pd.DataFrame(np.ones((3, 4))*1, columns=['a', 'b', 'c', 'd'])
# df3 = pd.DataFrame(np.ones((3, 4))*2, columns=['a', 'b', 'c', 'd'])
# print(df1)
# print(df2)
# print(df3)
# res = pd.concat([df1, df2, df3], axis=0, ignore_index=True)
# print(res)

# join, ['inner', 'outer']
# df1 = pd.DataFrame(np.ones((3, 4))*0, columns=['a', 'b', 'c', 'd'], index=[1, 2, 3])
# df2 = pd.DataFrame(np.ones((3, 4))*1, columns=['b', 'c', 'd', 'e'], index=[2, 3, 4])
# print(df1)
# print(df2)
# res = pd.concat([df1, df2], join='outer', ignore_index=True)  # join = inner
# print(res)

# res = pd.concat([df1, df2], axis=1, join_axes=[df1.index])  # join = inner
# print(res)

# append
# df1 = pd.DataFrame(np.ones((3, 4))*0, columns=['a', 'b', 'c', 'd'])
# df2 = pd.DataFrame(np.ones((3, 4))*1, columns=['b', 'c', 'd', 'e'])
# df3 = pd.DataFrame(np.ones((3, 4))*1, columns=['b', 'c', 'd', 'e'])
# res = df1.append(df2, ignore_index=True, sort=True)
# res_1 = df1.append([df2, df3])
# s1 = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
# res_2 = df1.append(s1, ignore_index=True)
# print(res)
# print(res_1)
# print(res_2)

# s2 = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
# res = df1.append(s2, ignore_index=True)
# print(res)

# left = pd.DataFrame({'key1': ['K0', 'K0', 'K1', 'K2'],
#                      'key2': ['K0', 'K1', 'K0', 'K2'],
#                      'A': ['A0', 'A1', 'A2', 'A3'],
#                      'B': ['B0', 'B1', 'B2', 'B3'],
#                      })
# right = pd.DataFrame({'key1': ['K0', 'K1', 'K1', 'K2'],
#                       'key2': ['K0', 'K0', 'K0', 'K0'],
#                       'C': ['C0', 'C1', 'C2', 'C3'],
#                       'D': ['D0', 'D1', 'D2', 'D3'],
#                      })
# print(left)
# print(right)
# res = pd.merge(left, right, on=['key1', 'key2'], how='inner')
# how = ['left', 'right', 'inner', 'outer']

# plot data
# data = pd.Series(np.random.randn(1000), index=np.arange(1000))
# data = data.cumsum()

# Series
# data.plot()
# data.show()

# DataFrame
data_1 = pd.DataFrame(np.random.randn(1000, 4),
                    index=np.arange(1000),
                    columns=list("ABCD"))
data_1 = data_1.cumsum()
print(data_1.head())
data_1.plot()
plt.show()

# plot methods:
# 'bar', 'hist', 'box', 'kde', 'area', 'scatter', 'hexbin', 'pie'
ax = data_1.plot.scatter(x='A', y='B', color='DarkBlue', label='Class_1')
data_1.plot.scatter(x='A', y='C', color='DarkGreen', label='Class_2', ax=ax)
plt.show()



