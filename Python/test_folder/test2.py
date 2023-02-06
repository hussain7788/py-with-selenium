# from test_folder.test1 import person

class person():
    name = "hussain"

    def __init__(self, age: int, address:str):
        self.age = age
        self.address = address

    def get_data(self):
        return self.age, self.address



class Employee(person):
    
    def __init__(self):
        super().__init__(23, "kadapa")

    def sample(self):
        data = self.get_data()
        return (data)


d1 = Employee()
print(d1.name)
print(d1.age)
print(d1.address)
print(d1.sample())
