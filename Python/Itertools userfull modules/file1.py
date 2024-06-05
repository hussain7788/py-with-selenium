
##########################################################################
##  itertools Group by
import itertools

data = [{'name': 'Alice', 'age': 25},
        {'name': 'Bob', 'age': 30},
        {'name': 'Charlie', 'age': 25},
        {'name': 'David', 'age': 30}]

# Sort data by age to use groupby
data.sort(key=lambda x: x['age'])

grouped = itertools.groupby(data, key=lambda x: x['age'])
for key, group in grouped:
    print(key, list(group))

# Output:
# 25 [{'name': 'Alice', 'age': 25}, {'name': 'Charlie', 'age': 25}]
# 30 [{'name': 'Bob', 'age': 30}, {'name': 'David', 'age': 30}]

##################################################
## itertools product

import itertools

colors = ['red', 'green']
sizes = ['S', 'M']
product = itertools.product(colors, sizes)
print(list(product))  

# Output: [('red', 'S'), ('red', 'M'), ('green', 'S'), ('green', 'M')]

##########################################################
## itertools repeat

import itertools

repeater = itertools.repeat('Hello', 3)
print(list(repeater))  # Output: ['Hello', 'Hello', 'Hello']


