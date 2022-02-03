from random import randrange


for i in range(1, 6):
    for j in range(1, 6):
        print(i, end="")
    print()
##################################################################

print("\n")
for i in range(1, 6):
    for j in range(1, 6):
        print(j, end="")
    print()
print("\n")
##################################################################

for i in range(5):
    for j in range(2, 7):
        print(j+i, end="")
    print()
print("\n")
##################################################################

for i in range(5):
    for j in range(0, -5, -1):
        print(j+i, end="  ")
    print()

print("\n")
##################################################################

for i in range(1, 6):
    for j in range(i, i*6, i):
        print(j, end="")
    print()
print("\n")
##################################################################
n = 6
c = 1
for i in range(1, n):
    for j in range(c, n):
        print(j, end="  ")
    c = c+5
    n = n+5
    print()
print("\n")
##################################################################
for i in range(6):
    for j in range(1, i+1):
        print(j, end=" ")
    print()
print("\n")
##################################################################

for i in range(1, 6):
    for j in range(1, i+1):
        print(i, end=" ")
    print()
print("\n")
##################################################################
for i in range(1, 6):
    for j in range(1, i+1):
        print(j+i, end=" ")
    print()
print("\n")
##################################################################
for i in range(1, 6):
    for j in range(1, i+1):
        print(j*i, end=" ")
    print()
print("\n")
##################################################################
n = 5
for i in range(5, 0, - 1):
    for j in range(i):
        print("*", end=" ")
    print()
print("\n")
##################################################################
for i in range(6):
    for j in range(6-i-1):
        print(end=" ")
    for k in range(i+1):
        print("*", end=" ")
    print()
print("\n")
##################################################################

for i in range(1, 6):
    for j in range(1, i+1):
        print(chr(64+j), end=" ")
    print()
print("\n")
##################################################################
for i in range(1, 6):
    for j in range(1, i+1):
        print(chr(64+i), end=" ")
    print()
