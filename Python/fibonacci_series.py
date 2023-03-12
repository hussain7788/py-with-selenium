# # Program to display the Fibonacci sequence up to n-th term

# # nterms means this is length of fibonancci series
# # if we need 3 values then give 3
# nterms = int(input("How many terms? "))

# n1, n2 = 0, 1
# count = 0

# # check if the number of terms is valid
# if nterms <= 0:
#     print("Please enter a positive integer")
# # if there is only one term, return n14
# elif nterms == 1:
#     print("Fibonacci sequence upto", nterms, ":")
#     print(n1)
# # generate fibonacci sequence
# else:
#     print("Fibonacci sequence:")
#     while count < nterms:
#         print(n1)
#         nth = n1 + n2  # 1
#         # update values
#         n1 = n2  # 1
#         n2 = nth  #
#         count += 1
# print("#" * 30)
# nterms = 5
# n1, n2 = 0, 1
# count = 0

# while count < nterms:
#     print(n1)
#     nth = n1 + n2
#     n1 = n2
#     n2 = nth
#     count += 1
# print("*"*30)

# nterm = int(input("enter term::,"))
# n1, n2 = 0, 1
# count = 0

# if nterm <= 0:
#     print("positve")
# elif nterm == 1:
#     print("fibonanci series ", n1)
# else:
#     while count < nterm:
#         print(n1)
#         nth = n1+n2
#         n1 = n2
#         n2 = nth
#         count += 1

##########################################################################################
# by using Generators we can easily findout fibonacci series


def fibonacci(num):
    a, b = 0, 1
    count = 0
    while count < num:
        yield a
        a, b = b, a+b
        count += 1


func = fibonacci(5)
print(list(func))

### another type
def func(n):
    for i in range(0,n):
        yield i
    
f1 = func(5)
print(type(f1))
print(next(f1))
print(next(f1))      
print(next(f1))      
print(next(f1))      
print(next(f1))      

