# import requests


# print("hello")
# url = "http://api.open-notify.org/astros.json"

# req = requests.get("http://api.open-notify.org/astros.json")
# print(req.json())
from tkinter import Tk
import tkinter
import sys
import os
import datetime
import math
import math
import random
import json

# these are the OS methods
# os = ["mkdir", "chdir", "rmdir", "remove", "os.path.join", "getcwd()"]
# print(sys.version)
# print(sys.argv)
# os.chdir("D:\DjangoProjects")
# os.mkdir("new")
# os.rmdir("new")
# os.remove("D:\EntireProjects\Python\csv1.csv")
# print(os.getcwd())

# print(os.path.join("D:\EntireProjects\Python",
#       "D:\EntireProjects\Python\csv.ex1.py"))
# print(os.getcwd().split("Python")[0])

# print(random.randrange(10, 100, 10))
# print(range(2))

#######################################
dt = datetime.datetime.today()
dt2 = datetime.datetime(1996, 12, 13)
print((dt-dt2)/30/12)

from datetime import date

# date object of today's date
today = date.today()

print("Current year:", today.year)
print("Current month:", today.month)
print("Current day:", today.day)



# root = Tk()
# root.title("first")
# root.mainloop()

import os
base = os.path.dirname(__file__)
file_name = os.path.join(base, "decorators.py")
print(os.path.join(base, "decorators.py"))

last = file_name.split("\\")[-1]
print(last)
st = f"python {last}"
print(st)
os.chdir(base)
os.system(st)
