# import string


# def sum(s1):
#     if len(s1) <= 1:
#         return string
#     f1 = s1[0]
#     l1 = s1[1:len(string)]
#     return l1+f1


# print(sum("hussain"))

# import queue
# import threading


# q = queue.Queue()

# for i in [3, 2, 1]:
#     def f():
#         q.put(i)
#     threading.Thread(target=f).start()
# print(q.get())


# def f1(l1):
#     root = {}
#     for sen in l1:
#         base = root
#         for word in sen.split(' '):
#             if not base.get(word):
#                 base[word] = {}
#             base = base[word]
#     return root


# print(f1(["hello world", "Hello there"]))


# def func(a, b):
#     a += 1
#     b.append(1)


# a, b = 0, []
# func(a, b)
# print(a, b)


# def f(n): return 1 if n <= 1 else n * f(n-1)


# print(f(4))

# def has(num):
#     has_p = False
#     has_n = False
#     for n in num:
#         has_p = num > 0
#         has_n = num < 0
#     return (has_p,  has_n)


# print(has([]))

# def _(func, items):
#     i = 0
#     for i in items:
#         if func(i):
#             items[i] = i
#             i += 1
#     del items[i:]

# print(sorted([1, 2, 0, 4, 40, 30, 100]))
A = [("a", "groot"), ("1", "stadium"), ("b", "school")]

for i in A:
    print(i[1])
