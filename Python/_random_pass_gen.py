import string as s
import random

digits = s.digits
all_letters = s.ascii_letters
lower = s.ascii_lowercase
upper = s.ascii_uppercase
sybmols = s.punctuation
all_strings = s.printable


p = digits + lower + upper + sybmols

num_length = 8

p1 = ''
for i in range(num_length):
    p1 += ''.join(random.choices(list(p)))

print(p1)




