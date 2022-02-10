# find the 5th biggest number in the list
from math import factorial


n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n.sort(reverse=True)
print(n[:5][-1])
#################################################

# sum of prime numbers
sum_prime = 0
for i in range(1, 101):
    if i > 1:
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            sum_prime += i
print("sum of prime numbers between 1 to 100::", sum_prime)

########################

n = 1234
s = str(n)
length = len(s)
add = int(s[1]) + int(s[length-2])
print(add)
#####################################
n = "145"
total = 0
fact1 = 1
fact4 = 1
fact5 = 1
for i in n:
    for j in range(1, int(i) + 1):
        if i == "1":
            fact1 = fact1 * int(j)
        if i == "4":
            fact4 = fact4 * int(j)
        if i == "5":
            fact5 = fact5 * int(j)
total += fact1 + fact4 + fact5
print("factorial::", fact1, fact4, fact5, total)

################################################

total = 0
for i in range(1, 5):
    total += i
    # print(total)
    print(total + i, end=" ")

################################################
# find out prime number from 100 to 1000 and in that prime numbers find out armstrong number if any--
# armstrong numbers from 100 to 1000 are [153, 370, 371, 407]
count = 0
res_list = []  # all prime numbers stored in list
for i in range(100, 1000):
    if i > 1:
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            print(i, "prime")
            count += 1
            res_list.append(i)


fact = 0
armstrong_list = []
# iterating prime numbers list to find out armstrong number if any
for val in res_list:  # 153
    len_num = len(str(val))  # 2
    for digit in str(val):  # 3
        fact = fact + int(digit) ** len_num
        print("factorial ::", fact)  # 0+1**2 = 1
        # 1+ 5**3 = 126
        # 126 + 3**3 = 153
    if fact == val:
        armstrong_list.append(val)
    fact = 0

print("count of prime::", res_list, count)
print("armstrong number list::", armstrong_list)
if 153 and 370 and 371 and 407 in res_list:
    print("yes")
else:
    print("no")
