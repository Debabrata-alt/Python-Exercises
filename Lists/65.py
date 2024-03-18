# Write a Python program to sort a given mixed list of integers and strings. Numbers must be sorted before strings.
# Original list:
# [19, 'red', 12, 'green', 'blue', 10, 'white', 'green', 1]
# Sort the said mixed list of integers and strings:
# [1, 10, 12, 19, 'blue', 'green', 'green', 'red', 'white']


mixed_list = [19, 'red', 12, 'green', 'blue', 10, 'white', 'green', 1]

def sort_mixed_list(mixed_list):
  # Extract and sort the integer part of the list
  int_part = sorted([i for i in mixed_list if type(i) is int])
  # Extract and sort the string part of the list
  str_part = sorted([i for i in mixed_list if type(i) is str])
  # Combine the sorted integer and string parts and return the result
  return int_part + str_part


print(sort_mixed_list(mixed_list))
# [1, 10, 12, 19, 'blue', 'green', 'green', 'red', 'white']