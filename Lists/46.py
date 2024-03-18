# Write a Python program to rotate a given list by a specified number of items in the right or left direction.
# original List:
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Rotate the said list in left direction by 4:
# [4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4]
# Rotate the said list in left direction by 2:
# [3, 4, 5, 6, 7, 8, 9, 10, 1, 2]
# Rotate the said list in Right direction by 4:
# [8, 9, 10, 1, 2, 3, 4, 5, 6]
# Rotate the said list in Right direction by 2:
# [9, 10, 1, 2, 3, 4, 5, 6, 7, 8]


nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# (1)
result = nums1[3:] + nums1[:4]

print(result) # [4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4]

# (2)
result = nums1[2:] + nums1[:2]

print(result) # [3, 4, 5, 6, 7, 8, 9, 10, 1, 2]

# (3)
result = nums1[-3:] + nums1[:-4]

print(result)  # [8, 9, 10, 1, 2, 3, 4, 5, 6]

# (4)
result = nums1[-2:] + nums1[:-2]

print(result) # [9, 10, 1, 2, 3, 4, 5, 6, 7, 8]
