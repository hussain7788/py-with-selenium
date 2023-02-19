# A shallow copy constructs a new compound object and then (to the extent possible) inserts references into it to the objects found in the original.

# A deep copy constructs a new compound object and then, recursively, inserts copies into it of the objects found in the original.

# Shallow Copy stores the copy of the original object and points the references to the objects.
# Deep copy stores the copy of the original object and recursively copies the objects as well.
import copy
############################################################################################
# deep copy
# if u deep copied a list and if u modified deep copied list then original list remain same.
# initializing list 1
li1 = [1, 2, [3, 5], 4]

# using deepcopy to deep copy
li2 = copy.deepcopy(li1)

# original elements of list
print("The original elements before deep copying")
for i in range(0, len(li1)):
    print(li1[i], end=" ")

print("\r")

# adding and element to new list
li2[2][0] = 7

# Change is reflected in l2
print("The new list of elements after deep copying ")
for i in range(0, len(li2)):
    print(li2[i], end=" ")

print("\r")

# Change is NOT reflected in original list
# as it is a deep copy
print("The original elements after deep copying")
for i in range(0, len(li1)):
    print(li1[i], end=" ")
##################################################################################################

# shallow copy
# if u shallow copy a list .then if u modify any data in shallow copy list then it reflect in original list
# initializing list 1
li1 = [1, 2, [3, 5], 4]

# using copy to shallow copy
li2 = copy.copy(li1)

# original elements of list
print("The original elements before shallow copying")
for i in range(0, len(li1)):
    print(li1[i], end=" ")

print("\r")

# adding and element to new list
li2[2][0] = 7

# checking if change is reflected
print("The original elements after shallow copying")
for i in range(0, len(li1)):
    print(li1[i], end=" ")
############################################################################################################
import copy
l1 = [1, 2, [3, 4], 5]
l2 = copy.copy(l1)

l2[2][0] = 31
print(l1, l2)

l3 = copy.deepcopy(l1)
l3[2][0] = 41
print(l1, l3)
