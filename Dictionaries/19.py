# Write a Python program to find the highest 3 values of corresponding keys in a dictionary.

my_dict = {'a': 500, 'b': 5874, 'c': 560, 'd': 400, 'e': 5874, 'f': 20}

sort_list_3 = sorted([my_dict[key] for key in my_dict], reverse=True)[:3]

print(sort_list_3)
# [5874, 5874, 560]

keys = list(key for key in my_dict if my_dict[key] in sort_list_3)

print(keys)
# ['b', 'c', 'e']

#///////////////////////////////////////////////////////////////////////////

from heapq import nlargest

my_dict = {'a': 500, 'b': 5874, 'c': 560, 'd': 400, 'e': 5874, 'f': 20}

# Use the 'nlargest' function to find the three largest keys in the 'my_dict' dictionary based on their values.
# The 'key' argument specifies that the values should be used for comparison.
three_largest = nlargest(3, my_dict, key=my_dict.get)

print(three_largest)
# ['b', 'e', 'c']
