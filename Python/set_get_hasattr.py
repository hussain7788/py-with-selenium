class Person:
    name = "hussain"
    age = 23
    address = "kadapa"
print(Person.age)

# setattr() func is used to set attr to the current class object
setattr(Person, "age", 25)

# getattr() function is used to get attributes from the class object 
print(getattr(Person, "age"))

# hasattr() func is used to check whether class object having that attribute or not
print(hasattr(Person, "address"))

# delattr() func is used to delete attribute of that current Person class
delattr(Person, "address")
print(hasattr(Person, "address"))