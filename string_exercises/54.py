# Write a Python program to remove all consecutive duplicates of a given string.

from itertools import groupby 

# Function to remove consecutive duplicates
def remove_all_consecutive(str1):
  result_str = []

  # Group string into consecutive characters
  for (key, group) in groupby(str1):
    # Append only one instance of each character
    result_str.append(key)

  # Join characters into string  
  return "".join(result_str)


print(remove_all_consecutive("xxxxxyyyyy")) # xy
print(remove_all_consecutive("aaaaebbbb")) # aeb


#////////////////////////////////////////////////////////////////
# NOTE

str = "xxxxxyyyyy"

for (key, group) in groupby(str):
  print(key)
  print(group)
  print(list(group))

# x
# <itertools._grouper object at 0x00000246980A5C90>
# ['x', 'x', 'x', 'x', 'x']
# y
# <itertools._grouper object at 0x00000246980A64A0>
# ['y', 'y', 'y', 'y', 'y']