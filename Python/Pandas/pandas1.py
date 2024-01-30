import pandas as pd
import numpy as np


# a1 = np.array([1,2,3])
# a2 = np.array([[4,5,6], [7,8,9]])
# a3 = np.array([[[1,2,3], [4,5,6]], [[7,8,9],[10,20,30]]])



# print(a1, a1.size)
# print(a2, a2.ndim, a2.shape)
# print(a3, a3.size, a3.shape, a3.ndim)


data = {
    "name":pd.Series(['hussain','valli','hussain','sunil',None]),
    "age":pd.Series([25,26,27,28,None]),
    "salary":pd.Series([20000, None,30000,40000,40000]),
    "doj": ['2024-01-27', '2024-01-26', '2024-01-25', '2024-01-30', None]
}

df = pd.DataFrame(data)
# d1.dropna(inplace=True)
# d1.fillna('', inplace=True)
# print(df[df.duplicated('salary')])
# df.loc[4, 'name'] = 5
# df.loc[4, 'age'] = 29
# print(df.at[0, 'name'])
# print(df.loc[[0,1]])
# df.rename(columns={
#     'name': 'Name',
#     'age': 'Age',
#     'salary': 'Salary'
# }, inplace=True)
print(df.describe())
print('\n')
print(df)




