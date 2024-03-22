# Write a Python program to check whether a specified list is sorted or not using lambda.
# Original list:
# [1, 2, 4, 6, 8, 10, 12, 14, 16, 17]
# Is the said list is sorted!
# True
# Original list:
# [1, 2, 4, 6, 8, 10, 12, 14, 16, 17]
# Is the said list is sorted!
# False

list1 = [1, 2, 4, 6, 8, 10, 12, 14, 16, 17]
list2 = [1, 2, 4, 6, 8, 10, 14, 12, 16, 17]

def func(myList):
  fn = lambda newList: newList == sorted(newList)
  return fn(myList)


print(func(list1)) # True
print(func(list2)) # false

#/////////////////////////////////////////////////////////////////////////////////////////////

nums1 = [1, 2, 4, 6, 8, 10, 12, 14, 16, 17]

nums2 = [2, 3, 8, 4, 7, 9, 8, 2, 6, 5, 1, 6, 1, 2, 3, 4, 6, 9, 1, 2]

# Define a function 'is_sort_list' that checks if a list 'nums' is sorted based on a specified 'key' function
def is_sort_list(nums, key=lambda x: x):
  # Iterate through the elements of the 'nums' list starting from the second element
  for i, e in enumerate(nums[1:]):
    # Compare the current element with the previous one based on the 'key' function
    if key(e) < key(nums[i]):
      # If the current element is smaller than the previous one, return False
      return False
  
  # If the loop completes without returning False, return True indicating the list is sorted
  return True

print(is_sort_list(nums1)) # True

print(is_sort_list(nums2)) # False

#/////////////////////////////////////////////////////////////////////////////////////////////

nums1 = [1, 2, 4, 6, 8, 10, 12, 14, 16, 17]

nums2 = [2, 3, 8, 4, 7, 9, 8, 2, 6, 5, 1, 6, 1, 2, 3, 4, 6, 9, 1, 2]

def is_sort_list(nums, key=lambda x: x):
  for i, e in enumerate(nums[1:]):
    if key(e) < key(nums[i]):
      return False
  return True


print(is_sort_list(nums1)) # True
print(is_sort_list(nums2)) # False
