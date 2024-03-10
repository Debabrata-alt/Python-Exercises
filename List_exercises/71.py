# Write a Python program to generate a number in a specified range except for some specific numbers.
# Generate a number in a specified range (1, 10) except [2, 9, 10]
# 7
# Generate a number in a specified range (-5, 5) except [-5,0,4,3,2]
# -4

from random import choice

nums1 = [2, 9, 10]
nums2 = [-5,0,4,3,2]

def func(nums, start_range, end_range):
  return choice([i for i in range(start_range, end_range + 1) if i not in nums])


# Each time a random number that matches the above condition will be outputted in the console.
print(func(nums1, 1, 10))
print(func(nums2, -5, 5))
