# Write a Python script to merge two Python dictionaries.

d1 = {'a': 100, 'b': 200}
d2 = d2 = {'x': 300, 'y': 200}

new_dict = {**d1, **d2}

print(new_dict)
# {'a': 100, 'b': 200, 'x': 300, 'y': 200}