# Write a Python program to find the highest 3 values of corresponding keys in a dictionary.

my_dict = {'a': 500, 'b': 5874, 'c': 560, 'd': 400, 'e': 5874, 'f': 20}

# sort values
sort_vals = sorted([my_dict[key] for key in my_dict], reverse=True)[:3]

print(sort_vals)
# [5874, 5874, 560]

#////////////////////////

# sort values (map method)
sort_vals = sorted(list(map(lambda x: my_dict[x], my_dict)), reverse=True)[:3]

print(sort_vals)
# [5874, 5874, 560]

#////////////////////////

# sort keys
sort_keys = sorted(my_dict, key=lambda x: my_dict[x], reverse=True)[:3]

print(sort_keys)
# ['b', 'e', 'c']

#///////////////////////////////////////////////////////////////////////////

from heapq import nlargest

my_dict = {'a': 500, 'b': 5874, 'c': 560, 'd': 400, 'e': 5874, 'f': 20}

# Use the 'nlargest' function to find the three largest keys in the 'my_dict' dictionary based on their values.
# The 'key' argument specifies that the values should be used for comparison.
three_largest = nlargest(3, my_dict, key=my_dict.get)

print(three_largest)
# ['b', 'e', 'c']
