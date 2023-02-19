
# The primary difference between the list sort() function and the sorted() function is that the sort() function will modify the list it is called on.
# The sorted() function will create a new list containing a sorted version of the list it is given. ... Once the sort() function is called on it, the list is updated.

# Initializing list of dictionaries
lis = [{"name": "Nandini", "age": 20},
       {"name": "Manjeet", "age": 20},
       {"name": "Nikhil", "age": 19}]

# using sorted and lambda to print list sorted
# by age
print("The list printed sorting by age: ")
print(sorted(lis, key=lambda i: i['age']))

print("\r")

# using sorted and lambda to print list sorted
# by both age and name. Notice that "Manjeet"
# now comes before "Nandini"
print("The list printed sorting by age and name: ")
print(sorted(lis, key=lambda i: (i['age'], i['name'])))

print("\r")

# using sorted and lambda to print list sorted
# by age in descending order
print("The list printed sorting by age in descending order: ")
print(sorted(lis, key=lambda i: i['age'], reverse=True))
######################################################################

print("The list printed sorting by name in descending order: ")
data = sorted(lis, key=lambda x: x['name'], reverse=True)
print(data)

# imp question
# sorting list of tuple
t1 = [
    ("name", 'n'),
    ("age", 'a'),
    ("address", 'd'),
]

s1 = sorted(t1, key=lambda x: (x[1], x[0]))
print(s1)
