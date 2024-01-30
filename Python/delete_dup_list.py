# # without using count

arr = [1, 7, 2, 3, 4, 2, 7, 8, 8, 3, 1]
# # arr = [1,1,2,2]

print("Duplicate elements in given array: ")
l1 = []
for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        if arr[i] == arr[j]:
            l1.append({'value':arr[j], "index": j})
print(arr)
l1 = sorted(l1, key=lambda x: x['index'], reverse=True)
print(l1)
for i in l1:
    arr.pop(i['index'])

print(arr)



# # with using count to print duplicate values in list l3 else filtered duplicated list l4
# l3 = []
# l4 = []
# for i in arr:
#     count = arr.count(i)
#     if count > 1:
#         if i not in l3:
#             l3.append(i)
#     else:
#         l4.append(i)

# print(l3,l4)

# ############ another method to delete duplicates ####
# l1 = []
# for index, num in enumerate(arr):
#     if arr.count(num) > 1:
#         arr.pop(index)
#         # duplicate elements in list
#         l1.append(num)
    
# # after deleting duplicates 
# print(arr)
# # duplicates elements stored in l1
# print(l1)

# ################ another method ###############
# l1 = [1,2,3,1,1,2,4,4]
# print(list(dict.fromkeys(l1)))