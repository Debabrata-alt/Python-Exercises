# Write a Python program to find the maximum and minimum product of pairs of tuples within a given list.
# The original list, tuple :
# [(2, 7), (2, 6), (1, 8), (4, 9)]
# Maximum and minimum product from the pairs of the said tuple of list:
# (36, 8)


nums = [(2, 7), (2, 6), (1, 8), (4, 9)]

def tuple_max_val(nums):
  # Calculate the maximum product using list comprehension with abs
  result_max = max([abs(x * y) for x, y in nums])
  
  # Calculate the minimum product using list comprehension with abs
  result_min = min([abs(x * y) for x, y in nums])
  
  # Return the maximum and minimum product as a tuple
  return result_max, result_min


print(tuple_max_val(nums)) # (36, 8)