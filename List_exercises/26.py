# Write a Python program to find the list in a list of lists whose sum of elements is the highest.

num = [[1, 2, 3], [4, 5, 6], [10, 11, 12], [7, 8, 9]]

# The 'key' argument specifies a lambda function that calculates the sum of each sublist
# The 'max' function returns the sublist with the maximum sum

print(max(num, key = sum)) # [10, 11, 12]


#///////////////////////////////////////////////////////////////////////////////
# sum() function

print(sum([1, 2, 3])) # 6

print(sum([1, 2, 3, 4, 5, 6])) # 21