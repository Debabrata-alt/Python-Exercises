# Write a Python program to remove sublists from a given list of lists that contain an element outside a given range.

my_list = [[2], [0], [1, 2, 3], [0, 1, 2, 3, 6, 7], [9, 11], [13, 14, 15, 17]]

left_range = 13
right_range = 17

def remove_list_range(input_list, left_range, right_range):
  # Use a list comprehension to filter sublists that meet the range criteria
  result = [i for i in input_list if (min(i) >= left_range and max(i) <= right_range)]
  return result

print(remove_list_range(my_list, left_range, right_range))
# [[13, 14, 15, 17]]
