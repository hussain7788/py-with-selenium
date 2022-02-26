from operator import index
import pandas as pd
import numpy as np
d1 = {"a": 1, "b": 2, "c": 3}
df = pd.Series(d1)
print(df)
print(df["a"], df["b"], df['c'], df[0])

data = {
    "company": ["google", "tata", "tcs", "infosys"],
    "person": ["hussain", "ajay", "vijay", "sunil"],
    "sales": [200, 120, 140, 340]

}

dt = pd.DataFrame(data, index=[1, 2, 3, 4])
# print(dt)

# print(dt['company'], dt.loc[[1, 2]])
# dt.drop('company', axis=1, inplace=True)
# print(dt)
# new = dt['sales'] + 100
# dt['new'] = new
# print(dt)

################################

employee_details = {
    "idno": pd.Series([101, 102, 103, 104, 105]),
    "name": pd.Series(["Ravi", "Kumar", "Mohan", "Krishna", "Prasad"]),
    "salary": pd.Series([185000.00, 285000.00, 125000.00, 225000.00, 100000.00])
}

print(employee_details['idno'])
df = pd.DataFrame(employee_details)
print(df)
print(df.loc[0])
print(df['name'])
new = df['salary'] + df['idno']
df['new_column'] = new
print(df)
# get single value by giving index
print(df.loc[0][1])

# 33
