class person ():
    # def __init__(self, name, age):
    #     self.name = name
    #     self.age = age

    def set(self):
        print("this is person get method")
        # print(f"name is {self.name} age is {self.age}")


# p = person("hussain", 25)
# p.get()
class sample():
    def get(self):
        print("this is sample class get method")


class inheriting_class(person, sample):
    def get(self):
        print("this is inheriting class get method")


a = inheriting_class()
a.set()
a.get()


def args_func(*args, **kwargs):
    total = 0
    for arg in args:
        total += arg

    for k, v in kwargs.items():
        print(f"key is {k} value is {v}")


l1 = [10, 20, 30]
d1 = {"name": "hussain", "age": 23}
args_func(*l1, **d1)
