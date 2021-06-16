def sample(*args, **kwargs):
    for i in args:
        print(i)

    print('sdfa',kwargs)

l1 = [1,2,3,4]
d1 = {1:"name", 2:"age", 3:"address"}
sample(*l1, None)


