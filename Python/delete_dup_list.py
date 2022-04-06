# without using count

arr = [1, 1, 2, 3, 4, 2, 7, 8, 8, 3]

# print("Duplicate elements in given array: ")
# # Searches for duplicate element
# for i in range(0, len(arr)):
#     for j in range(i+1, len(arr)):
#         if(arr[i] == arr[j]):
#             print(arr[j])

# with using count
l3 = []
for i in arr:
    count = arr.count(i)
    if count > 1:
        if i not in l3:
            l3.append(i)

print(l3)
