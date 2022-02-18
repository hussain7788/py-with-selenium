def sample(*args, **kwargs):
    for i in args:
        print(i)

    print('key', kwargs['kwargs']['name'])
    data = {"empname": "valli", "empdegn": "python"}
    kwargs.update(data)
    print(kwargs)


# l1 = [1,2,3,4]
# d1 = {1:"name", 2:"age", 3:"address"}
sample(1, 2, 3, 4, kwargs={"name": "hussain", "age": 23})


# def h(n):
#     s = 0
#     count = 0
#     for i in range(2, n):
#         if n % i == 0:
#             count += 1
#             s += i
#             print("i", i)
#     return(s)


# print(h(60)-h(45))
