s = 12345
s = str(s)
print(s[::-1])

#######################################
n = 12345
n = str(n)
total = 0
for i in n:
    if int(i) % 2 == 0:
        print(i, "even")
    total += int(i)
print(total)
###########################################
# sum of prime numbers
n = 123456789
sum_prime = 0
for i in str(n):
    if int(i) > 1:
        for j in range(2, int(i)):
            if int(i) % j == 0:
                break
        else:
            sum_prime += int(i)

print("sum of prime numbers::", sum_prime)

################################################

# armstrong number

n = 153
length = len(str(n))
str_n = str(n)
total = 0
for i in str_n:
    total += int(i) ** int(length)
if n == total:
    print(153, "is armstrong number")
else:
    print(153, "is not armstrong number")
