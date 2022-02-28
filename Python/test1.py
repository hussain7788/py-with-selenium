# a = [
#     {"name":"anil", "age":30},
#     {"name":"sunil", "age":10},
#     {"name":"vijay", "age":20},

# ]

# data = list(filter(lambda a: a['age'] > 10, a))
# print(data)

# num_list = [1, 2, 5, 4, 5, 6, 4]
# num_list.sort()

# for i in num_list:
#     if num_list.count(i) > 1:
#         # print(i)
#         print(f"duplicate value is{i} and index is {num_list.index(i)}")

# lis = set(num_list)
# print(list(lis))

# name = "hussai   n"

# # n = list(name)
# count = ''
# for i in name:
#     if i != ' ':
#         count += i
# print(count)


##################
n1 = "huss  ain"
l1 = list(n1)
ff = str(l1)
print("str", ff, type(ff))
print(l1)
l2 = []
for i in l1:
    if i != ' ':
        l2.append(i)

print(l2)
