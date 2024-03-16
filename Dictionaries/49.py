# Write a Python program to convert a dictionary into a list of lists.
# Original Dictionary:
# {1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}
# Convert the said dictionary into a list of lists:
# [[1, 'red'], [2, 'green'], [3, 'black'], [4, 'white'], [5, 'black']]
# Original Dictionary:
# {'1': 'Austin Little', '2': 'Natasha Howard', '3': 'Alfred Mullins', '4': 'Jamie Rowe'}
# Convert the said dictionary into a list of lists:
# [['1', 'Austin Little'], ['2', 'Natasha Howard'], ['3', 'Alfred Mullins'], ['4', 'Jamie Rowe']]

myDict1 = {1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}
myDict2 = {'1': 'Austin Little', '2': 'Natasha Howard', '3': 'Alfred Mullins', '4': 'Jamie Rowe'}

def func(inp_dict):
  return list([k, v] for k, v in inp_dict.items())

print(func(myDict1))
# [[1, 'red'], [2, 'green'], [3, 'black'], [4, 'white'], [5, 'black']]

print(func(myDict2))
# [['1', 'Austin Little'], ['2', 'Natasha Howard'], ['3', 'Alfred Mullins'], ['4', 'Jamie Rowe']]

#//////////////////////////////////////////////////////////////////////////////////////////

myDict1 = {1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}
myDict2 = {'1': 'Austin Little', '2': 'Natasha Howard', '3': 'Alfred Mullins', '4': 'Jamie Rowe'}

def func(inp_dict):
  result = list(map(list, inp_dict.items()))
  return result    


print(func(myDict1))
# [[1, 'red'], [2, 'green'], [3, 'black'], [4, 'white'], [5, 'black']]

print(func(myDict2)) 
# [['1', 'Austin Little'], ['2', 'Natasha Howard'], ['3', 'Alfred Mullins'], ['4', 'Jamie Rowe']]