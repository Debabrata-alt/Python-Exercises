# Write a Python program to count the same pair in three given lists.
# Original lists:
# [1, 2, 3, 4, 5, 6, 7, 8]
# [2, 2, 3, 1, 2, 6, 7, 9]
# [2, 1, 3, 1, 2, 6, 7, 9]
# Number of same pair of the said three given lists:
# 3

nums1 = [1, 2, 3, 4, 5, 6, 7, 8]
nums2 = [2, 2, 3, 1, 2, 6, 7, 9]
nums3 = [2, 1, 3, 1, 2, 6, 7, 9]

def count_same_pair(nums1, nums2, nums3):
  # Use a generator expression within the 'sum' function to count the same pairs
  result = sum(m == n == o for m, n, o in zip(nums1, nums2, nums3))
  return result

print(count_same_pair(nums1, nums2, nums3)) # 3