from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

x = np.array([1, 8])
y = np.array([3, 10])
plt.bar(x, y)
plt.show()


data = [
    {"name": "hussain", "age": 23, "address": "kadapa"},
    {"name": "valli", "age": 24, "address": "hyd"},
    {"name": "ajay", "age": 25, "address": "bang"}
]

df = pd.DataFrame(data)
print(df)
