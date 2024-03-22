# Write a Python program to extract a specified size of strings from a given list of string values using lambda.
# Original list:
# ['Python', 'list', 'exercises', 'practice', 'solution']
# length of the string to extract:
# 8
# After extracting strings of specified length from the said list:
# ['practice', 'solution']

myList = ['Python', 'list', 'exercises', 'practice', 'solution']

newList = list(filter(lambda el: len(el) == 8, myList)) 

print(newList)
# ['practice', 'solution']