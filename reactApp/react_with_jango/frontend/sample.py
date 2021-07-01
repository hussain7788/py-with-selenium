def sample(*args, **kwargs):
    #for i in args:
    #print(args[0])

    for k,v in kwargs.items():
        print(k)
        

l1 = [1,2,3,4]
d1 = {1:"name", 2:"age", 3:"address"}
sample(l1, d1)
