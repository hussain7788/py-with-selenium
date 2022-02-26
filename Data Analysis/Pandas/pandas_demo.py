from numpy.random import randn as rn
from operator import index
import pandas as pd
import numpy as np

labels = ["a", "b", "c"]
data = [1, 2, 3]
arr = np.array(data)
d = {"a": 1, "b": 2, "c": 3}

# print(arr, type(arr))

# print(pd.Series(d))
s1 = pd.Series([1, 2, 3], ["cs", "cd", "cv"])
s2 = pd.Series(data, labels)

s3 = pd.Series([4, 5, 6])
# print(pd.DataFrame(s3))

# print(s1,  s1["cs"], s1[2], s1[1:])

# ################################
# # adding and merging two series with common indices
# # here it will work based on alphabitical order starting index
# ser1 = pd.Series([1, 2, 3, 4], ["ca", "or", "co", "az"])
# ser2 = pd.Series([1, 2, 3, 4], ["ca", "or", "oc", "az"])
# ser3 = ser1+ser2
# print(ser3)

# ###########################################

# Data Frame is mainly usefull
np.random.seed(101)
matrix_data = rn(5, 4)
row_labels = ["A", "B", "C", "D", "E"]
col_labels = ["W", "X", "Y", "Z"]
df = pd.DataFrame(data=matrix_data, index=row_labels, columns=col_labels)
print("the data frame looks like\n", "-"*50, sep=' ')
print(df)
# accessing data using columns
print(df['X'], df['Y'])

# adding new column by combining two existing columns
df['new'] = df['X'] - df['Z']
print(df)

# deleting column using drop
# axis and inplace must to drop a column
df.drop("new", axis=1, inplace=True)
print(df)

# accessing single row
print(df.loc['A'])
print(df.loc[['A', "B"]])

# accessing only Subsetting DataFrame means specific row and column
print(df.loc[["A", 'B'], ['X', 'Y']])

# greater than and less than values
# this will give boolean results
print(df > 0)
# if dont want boolean result then do like this
d = df > 0
print(df[d])
# Accessing rows with greater than zero values
print(df.loc[["A", "B", "C"]] > 0)

###################################
# deleting null values
df1 = pd.DataFrame(
    {"a": [1, 2, np.nan],  "b": [5, np.nan, np.nan],  "c": [1, 2, 3]}
)
df1['States'] = "CA NV AZ".split()
df1.set_index('States', inplace=True)
print(df1)

# will drop row null values because axis=0 (axis=0 will delete row values)
print(df1.dropna(axis=0))
# will drop column null values because axis=0 (axis=0 will delete column values)
print(df1.dropna(axis=1))
# display two rows by using thresh
print(df1.dropna(axis=0, thresh=2))

# filling null values
print(df1.fillna("filled"))
# mean is middle value
print(df1.fillna(value=df1['a'].mean()))

###########################################################
data = {
    "company": ["google", "tata", "tcs", "infosys"],
    "person": ["hussain", "ajay", "vijay", "sunil"],
    "sales": [200, 120, 140, 340]

}
df2 = pd.DataFrame(data=data, index=["A", "B", "C", "D"])
print(df2)
