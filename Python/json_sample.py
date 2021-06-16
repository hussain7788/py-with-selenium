import json 
	
# Data to be written 
dictionary ={ 
	"name" : "sathiyajith", 
	"rollno" : 56, 
	"cgpa" : 8.6, 
	"phonenumber" : "9976770500"
} 
	
file2 = open("sample30.json", 'r')
file1 = open("sample30.json", 'r')
d1 = {"name" :"hussain", "age" : 23}
j1 = json.dumps(d1)
print(j1, type(j1))
j2 = json.loads(j1)
print(j2, type(j2))
# file1.write(j1)
# file1.close()
# print(data)
# print(file1.read())
 
 # functions is used for to convert py dict into json obj 
 # 1. json.dump()
 # 2. json.dumps()

 ## functions is used for to convert json obj into py dict
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
# 	j2 = json_file.read()
# 	print(j2)



