# Write a Python program to add two given lists of different lengths, starting on the left.
# Original lists:
# [2, 4, 7, 0, 5, 8]
# [3, 3, -1, 7]
# Add said two lists from left:
# [5, 7, 6, 7, 5, 8]
# Original lists:
# [1, 2, 3, 4, 5, 6]
# [2, 4, -3]
# Add said two lists from left:
# [3, 6, 0, 4, 5, 6]


def elementswise_left_join(l1, l2):
    # Calculate the difference in lengths between 'l1' and 'l2' and store it in 'f_len'.
    f_len = len(l1) - (len(l2) - 1)
    
    # Iterate over the indices of 'l2' using a 'for' loop.
    for i in range(0, len(l2), 1):
        # Check if 'f_len - i' is greater than or equal to the length of 'l1'.
        if f_len - i >= len(l1):
            # If the condition is met, exit the loop.
            break
        else:
            # Otherwise, element-wise add the corresponding elements of 'l1' and 'l2'.
            l1[i] = l1[i] + l2[i]
    
    # Return the modified 'l1' list after element-wise left join.
    return l1


nums1 = [2, 4, 7, 0, 5, 8]
nums2 = [3, 3, -1, 7]

print(elementswise_left_join(nums1, nums2))

nums3 = [1, 2, 3, 4, 5, 6]
nums4 = [2, 4, -3]

print(elementswise_left_join(nums3, nums4)) 
