import pandas as pd
import numpy as np


a1 = np.array([1,2,3])
a2 = np.array([[4,5,6], [7,8,9]])
a3 = np.array([[[1,2,3], [4,5,6]], [[7,8,9],[10,20,30]]])



print(a1, a1.size)
print(a2, a2.ndim, a2.shape)
print(a3, a3.size, a3.shape, a3.ndim)


data = {
    "name":pd.Series([1,2,3,4,5]),
    "age":pd.Series([25,26,27,28,29]),
    "salary":pd.Series([20000, 10000,30000,40000,50000])
}

d1 = pd.DataFrame(data)
print(d1)




