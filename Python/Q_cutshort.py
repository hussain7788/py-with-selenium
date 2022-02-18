st = 'ab-cd-ef'


def main(st):
    l1 = [ch for ch in st if ch.isalpha()]
    print(l1)
    return ''.join(l1.pop() if ch.isalpha() else ch for ch in st)


print(main(st))


x = "abcdef"
i = "a"
while i in x:
    x = x[1:]
    print(i, end=" ")


def my_func(nums):
    count = 0
    for i, j in enumerate(nums):
        if i > count:
            return False
        count = max(count, i + j)
    return True


print(my_func([3, 2, 1, 0, 4]))

############################
st = 'ab-cd-ef'
l1 = [ch for ch in st if ch.isalpha()]
print(l1)  # [a,b,c,d,e,f]
d = ''.join(l1.pop() if ch.isalpha() else ch for ch in st)
print("data:", d)
