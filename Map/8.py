# Write a Python program to convert a given list of integers and a tuple of integers in a list of strings.

nums_list = [1, 2, 3, 4]
nums_tuple = (0, 1, 2, 3)

result_list = list(map(str, nums_list))

result_tuple = tuple(map(str, nums_list))

print(result_list)
# ['1', '2', '3', '4']
print(result_tuple)
# ('1', '2', '3', '4')