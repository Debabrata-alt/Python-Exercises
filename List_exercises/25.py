# Write a Python program to move all zero digits to the end of a given list of numbers.


nums = [3, 4, 0, 0, 0, 6, 2, 0, 6, 7, 6, 0, 0, 0, 9, 10, 7, 4, 4, 5, 3, 0, 0, 2, 9, 7, 1]

def func(list):
  # Sort the list based on the key provided by the lambda function
  # The key function returns 'True' for non-zero elements and 'False' for zero elements
  result = sorted(list, key=lambda x: not x) 
  return result


print(func(nums))
# [3, 4, 6, 2, 6, 7, 6, 9, 10, 7, 4, 4, 5, 3, 2, 9, 7, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
