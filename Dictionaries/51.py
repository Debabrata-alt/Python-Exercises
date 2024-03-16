# Write a Python program to find the specified number of maximum values in a given dictionary.
# Original Dictionary:
# {'a': 5, 'b': 14, 'c': 32, 'd': 35, 'e': 24, 'f': 100, 'g': 57, 'h': 8, 'i': 100}
# 1 maximum value(s) in the said dictionary:
# ['f']
# 2 maximum value(s) in the said dictionary:
# ['f', 'i']
# 5 maximum value(s) in the said dictionary:
# ['f', 'i', 'g', 'd', 'c']

myDict = {'a': 5, 'b': 14, 'c': 32, 'd': 35, 'e': 24, 'f': 100, 'g': 57, 'h': 8, 'i': 100}

def func(inp_dict, n):
  return sorted(inp_dict, key=lambda x: inp_dict[x], reverse=True)[:n]

print(func(myDict, 1))
# ['f']

print(func(myDict, 2))
# ['f', 'i']

print(func(myDict, 5))
# ['f', 'i', 'g', 'd', 'c']

