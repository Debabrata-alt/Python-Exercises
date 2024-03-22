# Write a Python program to sort a given mixed list of integers and strings using lambda. Numbers must be sorted before strings.
# Original list:
# [19, 'red', 12, 'green', 'blue', 10, 'white', 'green', 1]
# Sort the said mixed list of integers and strings:
# [1, 10, 12, 19, 'blue', 'green', 'green', 'red', 'white']

myList = [19, 'red', 12, 'green', 'blue', 10, 'white', 'green', 1]

# 1. First sort the list by its string elements (all string elements will be sorted lexicographically and will be placed after the integer elements).
# 2. Then sort the remaining elements of the list (which are all integers) in ascending order. 
# Thus, the list will be sorted and all integer elements will be placed before the string elements.
newList = sorted(myList, key=lambda el: (isinstance(el, str), el))

print(newList)
# [1, 10, 12, 19, 'blue', 'green', 'green', 'red', 'white']