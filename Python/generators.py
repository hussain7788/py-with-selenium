# # # sample program for generator
# # def sample():
# #     yield 'a'
# #     yield 'b'
# #     yield 'c'


# # s = sample()
# # print(next(s))
# # print(next(s))
# # print(next(s))

# # ###


# def sample1(num):
#     count = 0
#     while count < num:
#         yield count
#         count += 1


# s1 = sample1(3)
# print(next(s1))
# print(next(s1))
# print(next(s1))

#### tuple comprehensions for generators
t1 = (x*x for x in range(1000))
print(next(t1))
print(next(t1))
print(next(t1))
print(list(t1))
