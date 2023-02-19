from functools import reduce
import math


# def add(a, b): return a+b


# print(add(10, 2))
# x = math.sqrt(9)
# print(x)

# l1 = [1, 2, 3, 4, 5, 6]
# f1 = list(filter(lambda a: a % 2 == 0, l1))
# print(f1)


# f2 = list(map(lambda a: a*2, l1))
# f3 = f2.copy()
# f3.insert(6, [7, 8])
# print(f3)
# print(f2.index(4))
# print(f2, f3)


# # g1 = list(map(lambda a: a*2, l1))
# # print(g1)

# g2 = list(filter(lambda a: a % 2 == 0, l1))
# print(g2)

##############
# tables = [lambda x=x: x for x in range(1, 11) if x > 5]
# for table in tables:
#     print("value is::", table())

lis = [{"name": "ajay", "age": 20},
       {"name": "sunil", "age": 30},
       {"name": "Nikhil", "age": 19}]

g1 = sorted(lis, key=lambda x: x['name'], reverse=True)
print(g1)

t1 = [
    ("name", 'n'),
    ("age", 'a'),
    ("address", 'd'),
]

s1 = sorted(t1, key=lambda x: x[1])
print(s1)
