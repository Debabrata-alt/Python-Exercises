# Write a Python program to add two given lists of different lengths, starting on the left.
# Original lists:
# [2, 4, 7, 0, 5, 8]
# [3, 3, -1, 7]
# Add said two lists from left:
# [5, 7, 6, 7, 5, 8]
# Original lists:
# [1, 2, 3, 4, 5, 6]
# [2, 4, -3]
# Add said two lists from left:
# [3, 6, 0, 4, 5, 6]

list1 = [2, 4, 7, 0, 5, 8]
list2 = [3, 3, -1, 7]

list3 = [1, 2, 3, 4, 5, 6]
list4 = [2, 4, -3]


def func(input_list1, input_list2):
  
  len_zip_list = len(list(zip(input_list1, input_list2)))
  
  return [el[0] + el[1] for el in zip(input_list1, input_list2)] + input_list1[len_zip_list: ] if len(input_list1) >= len(input_list2) else input_list2[len_zip_list: ]


print(func(list1, list2))
# [5, 7, 6, 7, 5, 8]

print(func(list3, list4))
# [3, 6, 0, 4, 5, 6]

