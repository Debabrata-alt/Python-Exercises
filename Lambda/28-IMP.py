# Write a Python program to find the maximum value in a given heterogeneous list using lambda.
# Original list:
# ['Python', 3, 2, 4, 5, 'version']
# Maximum values in the said list using lambda:
# 5

myList = ['Python', 3, 2, 4, 5, 'version']

# Find the maximum value in 'myList' based on two criteria:
# 1. First, sort by whether the element is an integer or not (True for integers, False for non-integers).
# 2. Second, sort lexicographically by the elements themselves.

max_val = max(myList, key=lambda el: (isinstance(el, int), el))

print(max_val) # 5

#///////////////////////////////////

max_val = max(myList, key=lambda el: (type(el) == int, el))

print(max_val) # 5