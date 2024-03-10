# Write a Python program to create a list taking alternate elements from a given list.
# Original list:
# ['red', 'black', 'white', 'green', 'orange']
# List with alternate elements from the said list:
# ['red', 'white', 'orange']
# Original list:
# [2, 0, 3, 4, 0, 2, 8, 3, 4, 2]
# List with alternate elements from the said list:
# [2, 3, 0, 8, 4]

list1 = ['red', 'black', 'white', 'green', 'orange']
list2 = [2, 0, 3, 4, 0, 2, 8, 3, 4, 2]

def func(input_list):
  new_list = []
  # Loop over elements in 'list_data' with a step of 2 (alternate elements)
  for el in input_list[::2]:
    new_list.append(el)
  return new_list


print(func(list1))
# ['red', 'white', 'orange']

print(func(list2))
# [2, 3, 0, 8, 4]