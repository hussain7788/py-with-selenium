from matplotlib import pyplot as plt
import pandas as pd
import numpy as np

data = {
    "company": ["google", "tata", "tcs", "infosys"],
    "person": ["hussain", "ajay", "vijay", "sunil"],
    "sales": [200, 120, 140, 340]

}
emp_data = {
    "first_year": pd.Series([45, 78, 98, 65, 32, 45]),
    "second_year": pd.Series([85, 88, 45, 65, 25, 41]),
    "third_year": pd.Series([68, 25, 36, 47, 89, 50]),
    "fourth_year": pd.Series([98, 74, 52, 51, 44, 69])
}
# df = pd.DataFrame(data)
df2 = pd.DataFrame(emp_data)

# using lines
# df2.plot()
# plt.show()

# # using bar
# df2.plot.bar()
# plt.show()

# # using box
# df2.plot.box()
# plt.show()

# # using area
# df2.plot.area()
# plt.show()

# using pie
df2.plot.pie(subplots=True)
plt.show()
