def sample(*args, **kwargs):
    for i in args:
        print(i)

    kwargs.clear()
    print('key', kwargs['name'])
    data = {"empname": "valli", "empdegn": "python"}
    kwargs.update(data)
    print(kwargs)


# l1 = [1,2,3,4]
# d1 = {1:"name", 2:"age", 3:"address"}
sample(1, 2, 3, 4, name="hussain", age=23, add="hyd")
