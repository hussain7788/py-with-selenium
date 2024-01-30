data = [
    {"name": "hussain", "age": 23, "address": "kadapa"},
    {"name": "valli", "age": 24, "address": "hyd"},
    {"name": "ajay", "age": 25, "address": "bang"}
]

d1 = [{"name": val['name'], "age":val['age'], "address":val['address']}
      for i, val in enumerate(data) if val['age'] >= 18]

print(d1)


d2 = [{k: v} if v.startswith('h') else {k: 'ajay'} 
      for i, val in enumerate(data) 
         for k, v in val.items() 
            if v in ['hussain', 'ajay']]
print(d2)