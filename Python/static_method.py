

class sample():
    name = str()
    age = int()

    def __init__(self, name, age):
        self.name = name
        self.age = age

# static method does not require class instance to call. so it doesnot require 'self'.
    @staticmethod
    def getData(obj):
        print("class bj::", sample.name, sample.age)
        print("obj::", obj.name, obj.age)

    def testM(self):
        print("test method")


class data_class():
    name = "hussain"
    age = 23


d = data_class()
# s1 = sample("hussain", 23).testM()

s = sample("hussain", 23).getData(d)
