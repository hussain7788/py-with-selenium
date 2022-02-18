data = [
    {"name": "hussain", "age": 23, "address": "kadapa"},
    {"name": "valli", "age": 24, "address": "hyd"},
    {"name": "ajay", "age": 25, "address": "bang"}
]

d1 = [{"name": val['name'], "age":val['age'], "address":val['address']}
      for i, val in enumerate(data) if val['age'] <= 18]

print(d1)
