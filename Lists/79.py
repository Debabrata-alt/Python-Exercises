# Write a Python program to append the same value/a list multiple times to a list/list-of-lists.

print("Add a value(7), 5 times, to a list:")

nums = []

nums += 5 * ['7']

print(nums) # ['7', '7', '7', '7', '7']

#//////////////////////////////////////

nums1 = [1, 2, 3, 4]

print("\nAdd 5, 6 times, to a list:")

nums1 += 6 * [5]

print(nums1) # [1, 2, 3, 4, 5, 5, 5, 5, 5, 5]

#//////////////////////////////////////////

print("\nAdd a list, 4 times, to a list of lists:")

nums1 = []

nums1 += 4 * [[1, 2, 5]]

print(nums1)
# [[1, 2, 5], [1, 2, 5], [1, 2, 5], [1, 2, 5]]

#///////////////////////////////////////////////

nums1 = [[5, 6, 7]]

print("\nAdd a list, 4 times, to a list of lists:")

nums1 += 4 * [[1, 2, 5]]

print(nums1) 
# [[5, 6, 7], [1, 2, 5], [1, 2, 5], [1, 2, 5], [1, 2, 5]]
