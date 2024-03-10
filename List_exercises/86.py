# Write a Python program to remove the None value from a given list.
# Original list:
# [12, 0, None, 23, None, -55, 234, 89, None, 0, 6, -12]
# Remove None value from the said list:
# [12, 0, 23, -55, 234, 89, 0, 6, -12]


nums = [12, 0, None, 23, None, -55, 234, 89, None, 0, 6, -12]

def remove_none(nums):
  result = [x for x in nums if x is not None]
  return result

print(remove_none(nums))
# [12, 0, 23, -55, 234, 89, 0, 6, -12]