# Write a Python program to find the first appearance of the substrings 'not' and 'poor' in a given string. If 'not' follows 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string.
# Sample String : 'The lyrics is not that poor!'
# 'The lyrics is poor!'
# Expected Result : 'The lyrics is good!'
# 'The lyrics is poor!'

import sys

my_str = input("Enter the string: ")  # The lyrics is not that poor!
final_str = ""

if "not" in my_str and "poor" in my_str:
  index1 = my_str.index("not")
  index2 = my_str.find("poor")
  print(index1, index2) # 14, 23
else: 
  print(my_str)
  # sys.exit("Thank you")
  sys.exit()


if index2 > index1:
  str_for_replace = my_str[index1: index2 + len("poor")]
  print(str_for_replace) # not that poor
  final_str = my_str.replace(str_for_replace, "good")
else:
  final_str = my_str

print(final_str) # The lyrics is good!
