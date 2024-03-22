# Write a Python program to find the intersection of two given arrays using Lambda.
# Original arrays:
# [1, 2, 3, 5, 7, 8, 9, 10]
# [1, 2, 4, 8, 9]
# Intersection of the said arrays: [1, 2, 8, 9]

list1 = [1, 2, 3, 5, 7, 8, 9, 10]
list2 = [1, 2, 4, 8, 9]

intersecn = lambda n1, n2: sorted(list(set(n1).intersection(set(n2))))

print(intersecn(list1, list2))
# [1, 2, 8, 9]

#/////////////////////////////////////////////////////////////////////////////////////////

list1 = [1, 2, 3, 5, 7, 8, 9, 10]
list2 = [1, 2, 4, 8, 9]

intersecn = lambda n1, n2: [e for e in n1 if e in n2]

print(intersecn(list1, list2))
# [1, 2, 8, 9]

#/////////////////////////////////////////////////////////////////////////////////////////

list1 = [1, 2, 3, 5, 7, 8, 9, 10]
list2 = [1, 2, 4, 8, 9, 12]

intersecn = list(filter(lambda el: el in list1, list2))

print(intersecn)
# [1, 2, 8, 9]