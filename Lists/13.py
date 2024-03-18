# Write a Python program to calculate the difference between the two lists.

list1 = [1, 3, 5, 7, 9]

list2 = [1, 2, 4, 6, 7, 8]

# Calculate the difference between 'list1' and 'list2' by converting them to sets and subtracting the sets
diff_of_list1_and_list2 = list(set(list1) - set(list2))

# Calculate the difference between 'list2' and 'list1' by converting them to sets and subtracting the sets
diff_of_list2_and_list1 = list(set(list2) - set(list1))

# Concatenate the differences 'diff_list1_list2' and 'diff_list2_list1' to obtain a list of all unique differences
total_diff = diff_of_list1_and_list2 + diff_of_list2_and_list1

# Print the total difference, which represents elements that are unique to each list
print(total_diff)
# [9, 3, 5, 8, 2, 4, 6]
