# Write a Python program to flatten a shallow list.

org_list = [[2, 4, 3], [1, 5, 6], [9], [7, 9, 0]]

newList = list(e for el in org_list for e in el)

print(newList) 
# [2, 4, 3, 1, 5, 6, 9, 7, 9, 0]

#//////////////////////////////////////////

newList = org_list[0] + org_list[1] + org_list[2] +  org_list[3]

print(newList)
# [2, 4, 3, 1, 5, 6, 9, 7, 9, 0]

#/////////////////////////////////////////////////////////////////////////////////////////////

# Import the 'itertools' module, which provides various functions for working with iterators
import itertools

original_list = [[2, 4, 3], [1, 5, 6], [9], [7, 9, 0]]

# Use 'itertools.chain' and the unpacking operator (*) to merge the sublists into a single flat list
new_merged_list = list(itertools.chain(*original_list))

print(new_merged_list)
# [2, 4, 3, 1, 5, 6, 9, 7, 9, 0]


#//////////////////////////////////////////////////////////////////////////////////////

original_list = [[2, 4, 3], [1, 5, 6], [9], [7, 9, 0]]

# unpacking operator (*)

print(*original_list)
# [2, 4, 3] [1, 5, 6] [9] [7, 9, 0]


def func(*args):
  print(args) # ([[2, 4, 3], [1, 5, 6], [9], [7, 9, 0]],)
  for arg in args[0]:
    print(arg)
    # [2, 4, 3]
    # [1, 5, 6]
    # [9]
    # [7, 9, 0]
  for arg in args[0]:
    for a in arg:
      print(a)
      # 2
      # 4
      # 3
      # 1
      # 5
      # 6
      # 9
      # 7
      # 9
      # 0


func(original_list)


#//////////////////////////////////////////////////////////////////////////////////////

original_list = [[2, 4, 3], [1, 5, 6], [9], [7, 9, 0]]

# unpacking operator (*)

print(*original_list)
# [2, 4, 3] [1, 5, 6] [9] [7, 9, 0]

def func(args):
  print(*args) # [2, 4, 3] [1, 5, 6] [9] [7, 9, 0]
  for arg in args:
    print(*arg)
    # 2 4 3
    # 1 5 6
    # 9
    # 7 9 0


func(original_list)