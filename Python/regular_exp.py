import copy
import math
import re

# pattern = re.compile("[abc]")
# match = pattern.finditer("i am hussain valli")
# for i in match:
#     print(i.start(), "......", i.end(), "......", i.group())

ptn = re.compile("hussain")
mat = ptn.match("hussain and vallli")
print(mat.group())
l2 = [1, 2, 3, 4]
l3 = [5, 6, 7, 8]
l2[1] = 10
print(l2.index(1))
print(l2)
s1 = {"hussain", "valli"}
print(len(s1))
