# Write a Python program to print a dictionary in table format.

my_dict = {'C1': [1, 2, 3], 'C2': [5, 6, 7], 'C3': [9, 10, 11]}

# Sort the items (key-value pairs) in the 'my_dict' dictionary based on their keys.
# The 'zip' function yields tuples.

for row in zip(*([key] + value for key, value in sorted(my_dict.items()))):
  
  print(row)
  # ('C1', 'C2', 'C3')
  # (1, 5, 9)
  # (2, 6, 10)
  # (3, 7, 11)
  
  print(*row)
  # C1 C2 C3
  # 1 5 9
  # 2 6 10
  # 3 7 11


#//////////////////////////////////////////////////////////////////////////

myDict = {'C1': [1, 2, 3], 'C2': [5, 6, 7], 'C3': [9, 10, 11]}

print(sorted(myDict))
# ['C1', 'C2', 'C3']

print(sorted(myDict.keys()))
# ['C1', 'C2', 'C3']

print(sorted(myDict.values()))
# [[1, 2, 3], [5, 6, 7], [9, 10, 11]]

print(sorted(myDict.items()))
# [('C1', [1, 2, 3]), ('C2', [5, 6, 7]), ('C3', [9, 10, 11])]

# sorting is based on the keys of the dictionary. 
# sorted() yields a List.
# If you sort dict.items() of a dictionary, it will yield a list of tuples. Each tuple holds a key-value pair of the dictionary.

#//////////////////////////////////////////////////////////////////////////

my_dict = {'C1': [1, 2, 3], 'C2': [5, 6, 7], 'C3': [9, 10, 11]}

l = [[key] + value for key, value in sorted(my_dict.items())]

print(l)
# [['C1', 1, 2, 3], ['C2', 5, 6, 7], ['C3', 9, 10, 11]]

print(*[[key] + (value) for key, value in sorted(my_dict.items())])
# ['C1', 1, 2, 3] ['C2', 5, 6, 7] ['C3', 9, 10, 11]

x = list(zip(*[[key] + (value) for key, value in sorted(my_dict.items())]))

print(x)
# [('C1', 'C2', 'C3'), (1, 5, 9), (2, 6, 10), (3, 7, 11)]


for a, b, c in zip(*[[key] + (value) for key, value in sorted(my_dict.items())]):
  print(a, b, c)
  # C1 C2 C3
  # 1 5 9
  # 2 6 10
  # 3 7 11

#//////////////////////////////////////////////////////////////////////////

myDict = {'C1': [1, 2, 3], 'C2': [5, 6, 7], 'C3': [9, 10, 11]}

def func(C1, C2, C3):
  for n in range(len(C1)):
    print(C1[n], C2[n], C3[n])

func(**myDict)
# 1 5 9
# 2 6 10
# 3 7 11



