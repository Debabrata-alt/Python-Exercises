# Write a Python program to remove all consecutive duplicates of a given string.

def func(inp_str):
  final_str = ""
  previous_char = None
  for char in inp_str:
    if char != previous_char:
      final_str += char
    previous_char = char
  return final_str

print(func("xxxxxyyyyy")) # xy

print(func("aaaaebbbb")) # aeb

print(func("aaesbbbbcyggsss")) # aesbcygs

#//////////////////////////////////////////////////////////////////

def func(inp_str):
  p = inp_str[0]
  i = 1
  j = len(inp_str)
  while i < j:
    if inp_str[i] == inp_str[i - 1]:
      i += 1
    else:
      p += inp_str[i]
      i += 1
  return p

print(func("xxxxxyyyyy")) # xy

print(func("aaaaebbbb")) # aeb

print(func("aaesbbbbcyggsss")) # aesbcygs

#////////////////////////////////////////////////////////////////////////////////////////////

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