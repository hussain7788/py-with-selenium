context = {}

for i in range(1, 10):
    context.update({f"loop {i}":i})

print(context)