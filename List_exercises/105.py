# Write a Python program to traverse a given list in reverse order, and print the elements with the original index.
# Original list:
# ['red', 'green', 'white', 'black']
# Traverse the said list in reverse order:
# black
# white
# green
# red
# Traverse the said list in reverse order with original index:
# 3 black
# 2 white
# 1 green
# 0 red

org_list = ['red', 'green', 'white', 'black']

for el in org_list[::-1]:
  print(el)
  
  # black
  # white
  # green
  # red


new_reversed_list = list((i, e) for i, e in enumerate(org_list))[::-1]

for el in new_reversed_list:
  print(el)
  
  # (3, 'black')
  # (2, 'white')
  # (1, 'green')
  # (0, 'red')


