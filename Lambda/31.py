# Write a Python program to count float values in a mixed list using lambda.
# Original list:
# [1, 'abcd', 3.12, 1.2, 4, 'xyz', 5, 'pqr', 7, -5, -12.22]
# Number of floats in the said mixed list:
# 3

myList = [1, 'abcd', 3.12, 1.2, 4, 'xyz', 5, 'pqr', 7, -5, -12.22]

floats_len = len(list(filter(lambda el: isinstance(el, float), myList)))

print(floats_len) # 3