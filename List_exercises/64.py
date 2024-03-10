# Write a Python program to find the first even and odd number in a given list of numbers.
# Original list:
# [1, 3, 5, 7, 4, 1, 6, 8]
# First even and odd number of the said list of numbers:
# (4, 1)


nums = [1, 3, 5, 7, 4, 1, 6, 8]

def first_even_odd(nums):
  # Use 'next' to find the first even number, default to -1 if not found
  first_even = next((el for el in nums if el % 2 == 0), -1)
  # Use 'next' to find the first odd number, default to -1 if not found
  first_odd = next((el for el in nums if el % 2 != 0), -1)
  return first_even, first_odd


print(first_even_odd(nums)) # (4, 1)