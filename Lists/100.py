# Write a Python program to shift last element to first position and first element to last position in a given list.
# Original list:
# [1, 2, 3, 4, 5, 6, 7]
# Shift last element to first position and first element to last position of the said list:
# [7, 2, 3, 4, 5, 6, 1]
# Original list:
# ['s', 'd', 'f', 'd', 's', 's', 'd', 'f']
# Shift last element to first position and first element to last position of the said list:
# ['f', 'd', 'f', 'd', 's', 's', 'd', 's']

list1 = [1, 2, 3, 4, 5, 6, 7]
list2 = ['s', 'd', 'f', 'd', 's', 's', 'd', 'f']

def func(inp_list):
  temp = inp_list[:1]
  inp_list[:1] = inp_list[-1:]
  inp_list[-1:] = temp
  return inp_list


print(func(list1)) 
# [7, 2, 3, 4, 5, 6, 1]

print(func(list2))
# ['f', 'd', 'f', 'd', 's', 's', 'd', 's']

#//////////////////////////////////////////////////////////

# Swap values

# a, 4, b = 5

# temp = a 
# a = b
# b = temp