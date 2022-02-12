import math


def add(a, b): return a+b


print(add(10, 2))
x = math.sqrt(9)
print(x)

l1 = [1, 2, 3, 4, 5, 6]
f1 = list(filter(lambda a: a % 2 == 0, l1))
print(f1)


f2 = list(map(lambda a: a*2, l1))
f3 = f2.copy()
f3.insert(6, [7, 8])
print(f3)
print(f2.index(4))
print(f2, f3)
