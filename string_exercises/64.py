# Write a Python program to find the smallest window that contains all characters in a given string.
# asdaewsqgtwwsa
# daewsqgt

from collections import Counter

def func(string):
  indices_list = []
  
  unique_chars_dict = Counter(string)
  unique_chars_list = [key for (key, count) in unique_chars_dict.items()]
  print(unique_chars_list)
  
  for el in unique_chars_list:
    # First occurance of el
    index = string.index(el)
    indices_list.append(index)
  
  indices_list.sort()
  print(indices_list)
  
  new_str = string[indices_list[0]: (indices_list[-1] + 1)]
  
  new_set = {s for s in new_str if new_str.count(s) > 1}
  new_list = list((new_set))
  print(new_list)
  
  for el in new_list:
    new_str = new_str.replace(el, "", (new_str.count(el) - 1))
  
  return new_str


print(func("asdaewsqgtwwsa")) # daewsqgt
