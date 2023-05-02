l1 = ['a','b','c']
l2 = ['d','e','f']

from itertools import product

data = list(product(l1,l2))
print(data)