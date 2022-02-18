# flag = False
# num = int(input("enter number"))
# # prime numbers are greater than 1
# if num > 1:
#     # check for factors
#     for i in range(2, num):
#         if (num % i) == 0:
#             flag = True
#             break

# # check if flag is True
# if flag:
#     print(num, "is not a prime number")
# else:
#     print(num, "is a prime number")

##########################################################
# program for prime in range
# for n in range(1, 100):
#     if n > 1:
#         for j in range(2, n):
#             if n % j == 0:
#                 break
#         else:
#             print(n)

#############################################################################

# # while condition for prime numbers
# req = "y"
# while req == "y":

#     n = int(input("enter number::"))
#     if n>1:
#         for i in range(2, n):
#             if n%i ==0:
#                 print(n, "is not prime")
#                 break
#         else:
#             print(n, "is prime")
#     req = input("do u want again(yes/no)::")


n = 7
if n > 1:
    for i in range(2, n):
        if n % i == 0:
            print(n, "is not prime")
            break
    else:
        print(n, "is prime")

# n1 = list(eval(input("enter")))
# n2 = input("enter string::")
# n2 = n2.split()
# print(n1, n2)
