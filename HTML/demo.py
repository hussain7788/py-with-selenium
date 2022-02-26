# # l1 = [5, 2, 8, 4, 8, 5, 4, 2, 3]

# # s1 = set(l1)
# # l2 = list(s1)
# # l2.sort(reverse=True)
# # print(l2[3])

# # n = 6
# # count = 0

# # for i in range(1, n):
# #     count += i


# import requests
# pincode = input("enter pincode::", )
# url = "https://api.postalpincode.in/pincode/" + pincode
# data = requests.get(url)
# # print(data.json())
# dt = data.json()
# count = 0
# for i, val in enumerate(dt):
#     # print(val['PostOffice'])
#     for i in val['PostOffice']:
#         if i['Pincode'] == pincode:
#             if count == 0:
#                 print(f"{pincode} circle is", i['Circle'])
#                 break
#         else:
#             print("no record found")
# a = [1,2,3,4,5,6]
# b = a
# b.append(6)
# print(a)

n = 8697855
s1 = len(str(n))
count = 0
while count < s1:
    count += 1

print(count)