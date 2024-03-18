# Write a Python program to find the smallest window that contains all characters in a given string.
# asdaewsqgtwwsa
# daewsqgt

from collections import Counter

def func(inp_string):
  indices_list = []
  
  unique_chars_dict = Counter(inp_string)
  
  print(unique_chars_dict)
  # Counter({'a': 3, 's': 3, 'w': 3, 'd': 1, 'e': 1, 'q': 1, 'g': 1, 't': 1})
  
  unique_chars_list = [key for (key, count) in unique_chars_dict.items()]
  
  print(unique_chars_list) # ['a', 's', 'd', 'e', 'w', 'q', 'g', 't']
  
  for el in unique_chars_list:
    # First occurance of el in the original string
    index = inp_string.index(el)
    indices_list.append(index)
  
  # Sort elements in ascending order
  indices_list.sort()
  
  print(indices_list) # [0, 1, 2, 4, 5, 7, 8, 9]
  
  new_string = inp_string[indices_list[0]: (indices_list[-1] + 1)]
  
  print(new_string) # asdaewsqgt
  
  new_set = {s for s in new_string if new_string.count(s) > 1}
  new_list = list((new_set))
  print(new_list) # ['a', 's']
  
  for el in new_list:
    new_string = new_string.replace(el, "", (new_string.count(el) - 1))
  
  return new_string


print(func("asdaewsqgtwwsa")) # daewsqgt

