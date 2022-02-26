# a = [
#     {"name":"anil", "age":30},
#     {"name":"sunil", "age":10},
#     {"name":"vijay", "age":20},

# ]

# data = list(filter(lambda a: a['age'] > 10, a))
# print(data)

num_list = [1, 2, 5, 4, 5, 6, 4]
num_list.sort()
# # print(num_list.count(4))
# # print(num_list)
# # l1 = list(set(num_list))
# # print(l1.sort())
# val = 0
# for i in num_list:
#     val = i
#     if i == val:
#         print(i)

for i in num_list:
    if num_list.count(i) > 1:

        print(i)
    # set(num_list)
print(list(num_list))
