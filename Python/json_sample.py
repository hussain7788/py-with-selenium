import json
from textwrap import indent

# Data to be written
dictionary = {
    "name": "sathiyajith",
    "rollno": 56,
    "cgpa": 8.6,
    "phonenumber": "9976770500"
}

json_data = '''{
    "j_name":"hussain",
    "j_age":23,
    "j_address":"kadapa"
}'''

with open("sample1.json", 'w') as s1:
    s1.write(json_data)
d1 = {"name": "valli", "age": 23}
# dump will take py dict and convert to json and save into json file
with open("sample30.json", 'w') as f2:
    json.dump(dictionary, f2, indent=4)

# reading the json file sample30.json
with open("sample30.json", 'r') as f1:
    r = json.load(f1)
    print(r, type(r))

# storing py dict into sample30.json by dumping
with open("sample30.json", 'a') as f3:
    json.dump(d1, f3)
    with open("sample30.json", 'r') as f4:
        r1 = json.load(f4)
        print("r1::", r1, type(r1))

# file1 = open("sample30.json", 'a')
# j1 = json.dumps(d1)
# print(j1, type(j1))
# j2 = json.loads(j1)
# print(j2, type(j2))
# file1.write(j1)
# file1.close()
# print(data)
# print(file1.read())

# functions is used for to convert py dict into json obj
# 1. json.dump()
# 2. json.dumps()

# functions is used for to convert json obj into py dict
# 1. json.load()
# 2. json.loads()

####################################################
# dump is used for to read the data
# with open("sample30.json", "r") as outfile:
# 	print("hello")
# json.dump(dictionary, outfile)


##############################################
# dumps is used for convert directly
# json_object = json.dumps(dictionary, indent = 4)
# print(json_object)
# print(type(json_object))

##################################################
# convert json object into py dictinary
# with open("sample30.json") as json_file:
# 	j1 = json.load(json_file)
# 	print(j1, type(j1))

###################################################
# open sample30.json and read
# with open("sample30.json") as json_file:
#     j2 = json_file.read()
#     print(j2)


# with open("sample30.json", 'r') as f:
#     data = json.load(f)
#     for i, v in data.items():
#         for value in v:
#             print(value['name'])
#     f.close()

# with open("sample30.json", 'r') as f:
#     data = json.loads(f.read())
#     print(data, type(data))
