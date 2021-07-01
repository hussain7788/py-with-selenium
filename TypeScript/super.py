class Employee:
    c_name = "tcs"
    c_add = "hyd"

    def get(self):
        self.emp_name = "hussain"
        self.emp_age = 23
    
    def set(self):
        print(self.emp_age, self.emp_name)

class Manager(Employee):
    def m_get(self):
        # self.m_name="manager"
        # self.m_age = 24
        super().get()

    def m_set(self):
        super().set()
    
m1 = Manager()
m1.get()
m1.set()
m1.m_get()
m1.m_set()

