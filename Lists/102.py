# Write a Python program to remove all strings from a given list of tuples.
# Original list:
# [(100, 'Math'), (80, 'Math'), (90, 'Math'), (88, 'Science', 89), (90, 'Science', 92)]
# Remove all strings from the said list of tuples:
# [(100,), (80,), (90,), (88, 89), (90, 92)]

org_list = [(100, 'Math'), (80, 'Math'), (90, 'Math'), (88, 'Science', 89), (90, 'Science', 92)]

x = [e for el in org_list for e in el if type(e) is int]

print(x)
# [100, 80, 90, 88, 89, 90, 92]

#/////////////////////////////////////////////////////////////////////

org_list = [(100, 'Math'), (80, 'Math'), (90, 'Math'), (88, 'Science', 89), (90, 'Science', 92)]

x = [tuple(e for e in el if not isinstance(e, str)) for el in org_list]

print(x)
# [(100,), (80,), (90,), (88, 89), (90, 92)]