class person:
    name = 'hussain'

    def display(self):
        print("this is person dis method")


class student(person):
    std_name = "valli"

    def display(self):
        print("this is student dis method")


class main:
    def m1(self):
        obj = student()
        obj.display()


m = main()
m1 = student()
m1.display()
# m.m1()
