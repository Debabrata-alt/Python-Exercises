# Write a Python program to add three given lists using Python map and lambda.

nums1 = [1, 2, 3]
nums2 = [4, 5, 6]
nums3 = [7, 8, 9]

newList = list(map(lambda el: sum(el), zip(nums1, nums2, nums3)))

print(newList)
# [12, 15, 18]

#//////////////////////////////////////////////////////////////////////////////////

nums1 = [1, 2, 3]
nums2 = [4, 5, 6]
nums3 = [7, 8, 9]

newList = list(map(lambda x, y, z: x + y + z, nums1, nums2, nums3))

print(newList)
# [12, 15, 18]