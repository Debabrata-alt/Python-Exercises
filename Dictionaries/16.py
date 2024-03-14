# Write a Python program to combine two dictionary by adding values for common keys.
# d1 = {'a': 100, 'b': 200, 'c':300}
# d2 = {'a': 300, 'b': 200, 'd':400}
# Sample output: Counter({'a': 400, 'b': 400, 'd': 400, 'c': 300})

d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}

new_dict = {}

for key in d1:
  if key in d2:
    new_dict[key] = d1[key] + d2[key]
  else:
    new_dict[key] = d1[key]

for key in d2:
  if key not in new_dict:
    new_dict[key] = d2[key]

print(new_dict)
# {'a': 400, 'b': 400, 'c': 300, 'd': 400}

#////////////////////////////////////////////////////////////////

from collections import Counter

d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}

# Use the 'Counter' class to create counter objects for 'd1' and 'd2', which count the occurrences of each key.
# Then, add the counters together to merge the key-value pairs and their counts.

counter_d1 = Counter(d1)
counter_d2 = Counter(d2)

print(counter_d1)
# Counter({'c': 300, 'b': 200, 'a': 100})
print(counter_d2)
# Counter({'d': 400, 'a': 300, 'b': 200})

d = counter_d1 + counter_d2

print(d)
# Counter({'a': 400, 'b': 400, 'd': 400, 'c': 300})