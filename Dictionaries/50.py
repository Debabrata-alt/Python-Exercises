# Write a Python program to filter even numbers from a dictionary of values.
# Original Dictionary:
# {'V': [1, 4, 6, 10], 'VI': [1, 4, 12], 'VII': [1, 3, 8]}
# Filter even numbers from said dictionary values:
# {'V': [4, 6, 10], 'VI': [4, 12], 'VII': [8]}
# Original Dictionary:
# {'V': [1, 3, 5], 'VI': [1, 5], 'VII': [2, 7, 9]}
# Filter even numbers from said dictionary values:
# {'V': [], 'VI': [], 'VII': [2]}

myDict1 = {'V': [1, 4, 6, 10], 'VI': [1, 4, 12], 'VII': [1, 3, 8]}
myDict2 = {'V': [1, 3, 5], 'VI': [1, 5], 'VII': [2, 7, 9]}

def func(inp_dict):
  return {k: list(e for e in v if e % 2 == 0) for k, v in inp_dict.items()}    

print(func(myDict1))
# {'V': [4, 6, 10], 'VI': [4, 12], 'VII': [8]}

print(func(myDict2))
# {'V': [], 'VI': [], 'VII': [2]}

#///////////////////////////////////////////////////////////////////

myDict1 = {'V': [1, 4, 6, 10], 'VI': [1, 4, 12], 'VII': [1, 3, 8]}
myDict2 = {'V': [1, 3, 5], 'VI': [1, 5], 'VII': [2, 7, 9]}

def func(inp_dict):
  return {k: list(filter(lambda x: x % 2 == 0, v)) for k, v in inp_dict.items()}    

print(func(myDict1))
# {'V': [4, 6, 10], 'VI': [4, 12], 'VII': [8]}

print(func(myDict2))
# {'V': [], 'VI': [], 'VII': [2]}

#///////////////////////////////////////////////////////////////////

def func(inp_dict):
  return dict((k, list(e for e in v if e % 2 == 0)) for k, v in inp_dict.items())   

print(func(myDict1))
# {'V': [4, 6, 10], 'VI': [4, 12], 'VII': [8]}

print(func(myDict2))
# {'V': [], 'VI': [], 'VII': [2]}

#///////////////////////////////////////////////////////////////////

def func(inp_dict):
  return dict([k, list(e for e in v if e % 2 == 0)] for k, v in inp_dict.items())   

print(func(myDict1))
# {'V': [4, 6, 10], 'VI': [4, 12], 'VII': [8]}

print(func(myDict2))
# {'V': [], 'VI': [], 'VII': [2]}

#///////////////////////////////////////////////////////////////////